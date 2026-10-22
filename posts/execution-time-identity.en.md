---
titre: Who did this, really? Execution-time identity for AI agents
resume: Your journal says "agent-7 did it". Who is agent-7 — a verified OS credential, or a name the software made up? The difference decides whether your audit trail proves anything, and 2026's broker experiments finally show how to close it.
date: 2026-10-22
themes: agents, preuve
source: https://futurium.ec.europa.eu/en/apply-ai-alliance/community-content/uai-block-ai-governance-principles-tested-access-controls-technical-progress-and-international
image: https://blog.noirebox.eu/img/execution-time-identity.jpg
image_alt: Un badge d'accès plastifié « agent-7 » posé à côté d'une empreinte digitale scannée sur un lecteur, lumière froide de datacenter.
---

Ask a compliance officer who performed an action in their systems and you'll get a name. Ask the system and you'll usually get a string: `agent-7`, `assistant`, `user`. The gap between those two answers is where most agent "accountability" quietly dissolves — because **a name the software claims for itself is not an identity.**

## The 2026 lesson: brokers verify, agents claim

The year's most instructive experiments came from an unexpected place: an independent researcher's broker prototypes. UAI-BLOCK's T04-v06 test did one small thing well — it gave the simulated agent and the broker **separate Linux identities**, then let the agent reach a protected file *only* through a Unix-domain socket where the broker could verify the peer credential (`SO_PEERCRED`). The agent could get the approved resource through the gate; it could not read the file directly. NIST's concept paper on software and AI agent identity points the same direction at standards level: identity and authorization belong to infrastructure, not to the agent's self-description.

The pattern generalizes beyond operating systems. Verified-at-execution identity can be an OS uid, a TLS client certificate, a workload credential — what matters is that the *gate* checks something the agent cannot forge, and that the check's result travels with the decision.

## Sealing the check, not the claim

Here's where this meets the journal. An authorization receipt — what we added to NoireBox this month — records one gate decision, and its first field is deliberately named to force the distinction:

- `agent`: the requester identity **as verified at execution time** — `os:uid=942 via SO_PEERCRED`, not "agent-7";
- `action` and `resource`: what was requested on what;
- `decision`, fail-closed: `allowed | denied | gate_error` — a failed gate is *named*, never silently retried into an allow;
- and for every allow, a **warrant**: the independent authority it leaned on (a user instruction, a prior receipt, an explicit grant).

The seal-time refusals are where the honesty lives: an allow without a warrant is rejected. A warrant that says the resource was "relevant" or "plausible" — the resource's own pull, the laundering vocabulary — is rejected by name. You wanted to allow it because it was *there*? The journal refuses to write that as authority.

Then the audit pass (`replay`) catches what got sealed around the refusals: allows without warrants, laundered warrants, and **gate flips** — a triple that was denied early in the sequence and allowed later. Either the warrant legitimately changed (seal the new one) or your gate is inconsistent. Both findings are better discovered by a replay than by a journalist.

## The uncomfortable test for your own stack

Find the last incident report your agent platform produced. Does the "who" field contain a credential an infra component verified — or a string the agent supplied? If it's the latter, you don't have accountability; you have autobiography.

The fix isn't exotic. Separate identities. Verify at the gate. Seal the decision with the verification attached, so the record carries its own proof. Everything else is naming conventions.
