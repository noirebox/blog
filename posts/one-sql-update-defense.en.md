---
titre: One SQL UPDATE against your AI agent's alibi, and the defense that catches it in 458 ms
resume: The product-side answer to the attack lab published on my personal logbook: exactly what NoireBox does when someone rewrites a decision in the journal, SHA-256 chain, Ed25519 signatures, a pinpointed verdict in 458 ms, and third-party verification that doesn't need to trust you.
date: 2026-10-22
themes: agents, preuve
source: https://blog.slabb.dev/en/one-sql-update-your-ai-agents-alibi-destroyed-and-caught-in-458-ms
image: https://blog.noirebox.eu/img/one-sql-update-defense.jpg
image_alt: SQLite database bound by a golden hash chain, one link broken at event 2; terminal showing the SQL UPDATE; "DETECTED" verdict in 458 ms.
---

[The attack lab is out on my personal logbook](https://blog.slabb.dev/en/one-sql-update-your-ai-agents-alibi-destroyed-and-caught-in-458-ms): we seal an agent's journal with NoireBox, hand the attacker a SQLite console, and a single line rewrites history, "the client VALIDATES the quote" becomes "the client REFUSES, no action required". Verdict: event 2, invalid hash, 458 ms to pinpoint it among a thousand. This post is the defense-side answer: what happened on the inside, why it's built that way, and, this matters, where it stops.

## Why a single line doesn't pass

Every event in the journal carries the hash of the one before it:

```json
{
  "seq": 2,
  "type": "llm_output",
  "payload": {"summary": "The client VALIDATES the quote, next step: signature."},
  "prev_hash": "5f164b1ab574fb89e84d2f88d93bdd5a1a80282ae4710fda89fb92282ca33c59",
  "event_hash": "37093f3e23b64c1c7f3ed621ce448c9eba178b5a732ee57f4ad1d0c47b0850e8",
  "signature": "2ecfdb1233a43d08d8bf836db494dc5cbaf2c53674eae409ed…"
}
```

`event_hash` is a SHA-256 over the whole event, seq, timestamp, type, payload **and the previous event's hash**, and the signature is Ed25519 under the instance key. History isn't stored, it's *committed to*. The attack is one line:

```sql
UPDATE events SET payload = '{ "summary": "The client REFUSES the quote, no action required." }'
WHERE seq = 2;
```

```text
[✗] DETECTED, event 2: invalid hash (content was modified)
```

Not "something changed somewhere", **event 2, content modified**. Patching it without the key means redoing the entire tail of the journal, rehashing half the chain, per attempt. Across a thousand events: 242 ms to verify an intact journal, 458 ms to point at event 500 forged dead center.

## The actual function: being believed by someone who doesn't trust you

On 21 October 2026, OpenAI disclosed that its own agents had weakened the internal system meant to monitor them, and that one of them denied doing it. The lesson generalizes: when the watched actor can touch the watching instrument, the proof must live out of its reach. In practice, "out of reach" means: a verifiable export on a third party's machine.

```bash
curl -s http://127.0.0.1:8768/api/v1/export > export.json
python3 verifier/verifier.py export.json
```

```text
[✓] INTACT, 3 events verified, attestation valid   exit 0
[✗] TAMPERING DETECTED, event 2: invalid hash      exit 1
```

No dashboard, no call back home, no "trust me, the logs are fine". The verifier recomputes the entire chain from the file: exit 0 or exit 1.

## What this is not

The easy marketing would stop here. An honest product states its limits:

- **Tamper-evident is not tamper-proof.** The seal holds against anyone who doesn't hold the instance key, key custody is the real security boundary.
- **The sophisticated version of the attack** wipes everything and replays history, re-signed. That's what RFC 3161 anchoring answers: periodically, the journal seals its own head hash with an external timestamping authority, as an event inside the journal. Replay the past and the anchors stop matching.
- **Deleting the store deletes the evidence.** Exports and anchors kept outside, an operational discipline, not a line of code.
- **It is not a certification.** NoireBox doesn't make anything "compliant"; it makes claims *checkable*, which is what any compliance starts from.

## So your agents have it by default

The same four operations ship as an MCP server (`noirebox-mcp`): `noirebox_scan` (guardrail on incoming transcripts), `noirebox_log_event`, `noirebox_verify`, `noirebox_attestation`. Any MCP-speaking agent gets a black box the way it gets a filesystem, infrastructure it can't opt out of.

## Run it

```bash
pip install noirebox            # 0.24.0 · MIT
git clone https://github.com/noirebox/noirebox
cd noirebox && .venv/bin/python demo/demo_tamper.py    # the chain explodes
python3 verifier/verifier.py export.json               # exit 0 / 1 / 2
```

The full attack lab, with context and numbers: [my personal logbook](https://blog.slabb.dev/en/one-sql-update-your-ai-agents-alibi-destroyed-and-caught-in-458-ms). The threat model, unfiltered: [docs/THREAT-MODEL.md](https://github.com/noirebox/noirebox/blob/main/docs/THREAT-MODEL.md).

Who watches the watcher when the watcher is a file next to the agent? The answer was never "a better file". It's a structure whose key lives outside the reach of the thing being watched.
