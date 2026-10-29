---
titre: Enforcement vs evidence: why OWASP ACS and NIST agent identity still need a journal
resume: 2026 shipped serious enforcement for AI agents, OWASP ACS, NIST's agent identity work, KedgeFlow's control plane. Their own evaluations admit what they can't do: prove what was decided, afterwards, to someone who doesn't trust you. That's a different layer.
date: 2026-10-22
themes: agents, preuve
source: https://genai.owasp.org/resource/agent-control-standard-acs/
image: https://blog.noirebox.eu/img/enforcement-vs-evidence.jpg
image_alt: Un poste de garde à l'entrée d'un bâtiment (contrôle) face à une boîte noire d'avion scellée (preuve), style manuel d'ingénierie.
---

2026 was the year agent enforcement got serious. Three efforts worth reading, none of them vapor:

- **[OWASP Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/)** (September 2026), portable runtime policy enforcement and visibility across agent platforms.
- **NIST's concept paper on software and AI agent identity** (February 2026), identity, authorization, auditing: the right vocabulary, finally.
- **[KedgeFlow](https://arxiv.org/abs/2610.14810)** (October 2026), a programmable control plane with signed, single-use allowances and a grant–claim–dispatch linkage; their evaluation includes 6,560 concurrent claim attempts producing exactly one successful claim per allowance. This is real infrastructure engineering.

We like all three, and we build none of them, NoireBox doesn't enforce anything at execution time. But read their own evaluations carefully, because each one names the same missing layer:

KedgeFlow's paper, in the limitations section, reports that **a permissive policy still authorized an undesirable effect**, execution authorization alone has limits, by their own measurement. OWASP ACS controls decide and act; nothing in the standard makes the decision sequence tamper-evident afterwards. And UAI-BLOCK's 18 October progress disclosure states its gap verbatim: *no tamper-resistant audit records, no independent verification.*

## Enforcement and evidence answer different questions

Enforcement answers: **"may this happen, now?"** It runs at the moment of action, inside your infrastructure, under your policy.

Evidence answers: **"what happened, and can you prove it to me if I don't trust you?"** It runs after the fact, on records the agent, and the operator, cannot quietly rewrite.

You need both, and they compose cleanly: every allow/deny a gate produces can be sealed as a signed event in a hash-chained journal, agent identity *as verified at execution time* (an OS credential, not a claimed name), the action, the resource, the warrant behind an allow. Then "our gate never approved an unauthorized request" stops being a claim and becomes a replay: the auditor re-runs the sealed sequence and checks.

The audit-grade version of KedgeFlow's race test is not "the gateway committed one effect", it's "*here is the sealed, verifiable record that it committed exactly one, and you can check that yourself offline*."

## The honest part

This composition is a claim, and claims need evidence too. Our evidence layer has its own open gaps, we haven't benchmarked journal throughput at production scale, and out-of-band anchoring (TSA / public commit pin) isn't wired yet. We keep that score public in [docs/RELATED-WORK.md](https://github.com/noirebox/noirebox/blob/main/docs/RELATED-WORK.md), next to the same map of the enforcement stack.

If you're building the gate: good, please build it well. Just don't let it be the only witness. Gates get misconfigured, bypassed, and inherited. The journal is the one that testifies afterwards, and it should be built by someone whose only job is being believable.
