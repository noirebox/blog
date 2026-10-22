---
titre: Capability is not authority — and logs are not evidence
resume: Two good papers made "capability ≠ authority" famous. Almost nobody asks the follow-up: what makes a record evidence? A working paper's four tests — accountability, auditability, scale, durability — plus an honest scorecard.
date: 2026-10-22
themes: agents, preuve
source: https://futurium.ec.europa.eu/en/apply-ai-alliance/community-content/declared-governance-demonstrable-governance-why-current-ai-governance-fails-four-tests-ssrn-working
image: https://blog.noirebox.eu/img/logs-are-not-evidence.jpg
image_alt: Un carnet de bord manuscrit raturé face à une chaîne de blocs métallique scellée, sur une table d'expertise.
---

Two ideas went viral in the AI-governance corner of 2026. You-An Lin's *Capability Is Not Authority*: an agent that *can* send the email hasn't earned the authority to send it — tools, documents and past successes don't confer warrant. And a working paper floating on the EU's Apply AI Alliance platform, *From Declared Governance to Demonstrable Governance*, judges governance claims on four tests: **accountability, auditability, scale, durability**.

Both are right, and both stop one step short of the engineering question:

**what turns a record into evidence?**

## Logs are not evidence

Every agent framework ships logs. Here's the difference between a log and evidence, stated as tests:

- **Tamper-evidence** — can the holder of the log (which is you, the operator) silently change yesterday's entry? If yes, it's a diary, not a record. Hash chaining plus signatures makes edits *detectable*, which changes the economics of lying.
- **Attribution** — does the record identify who acted by a *verified* identity, or by a name the software claimed for itself?
- **Independent verification** — can a third party check the record's integrity **offline**, without trusting your infrastructure, your uptime, or your word?
- **Adversarial testing** — has the mechanism been attacked on purpose? A lock that has never met a lockpick is a hypothesis.

Ask those four questions about any "audit trail" in your stack — including the one inside the compliance platform you bought. Most are diaries.

## The four governance tests, self-scored

Dr. Bunic's paper names its own bar, so we ran ourselves against it, publicly:

| Test | Where we stand |
|---|---|
| Accountability | Decision receipts and admission receipts seal who decided, on what basis — attribution by signature, not by claimed name |
| Auditability | Hash-chained journal, Ed25519-signed events, offline `verify`, a public catalog of attack fixtures replayed in CI |
| Scale | **Open gap.** Journal throughput at production volume is unbenchmarked. Saying so is cheaper than being caught |
| Durability | **Open gap.** Append-only SQLite + signed attestations, but no out-of-band anchoring (TSA / public commit pin) yet — a compromised host could truncate the tail |

Two greens, two ambers — published. That's the point of a bar: you measure, you publish the number, you close the gap. "Demonstrable governance" that only shows its green rows is just declared governance wearing a lab coat.

The uncomfortable corollary for everyone: if your governance page has no measured, dated, self-critical numbers on it — it's marketing.
