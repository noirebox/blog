---
titre: The auditor's question is "did it happen?", not "was it allowed?"
resume: Decision-outcome reconciliation is the boring mechanism that finds what dashboards hide: decisions with no outcome, outcomes nobody authorized, outcomes that outran their deadline, and a denominator that lied.
date: 2026-10-22
themes: preuve, conformité
source: https://github.com/noirebox/noirebox/blob/main/docs/ADRs.md
image: https://blog.noirebox.eu/img/did-it-happen-reconciliation.jpg
image_alt: Deux colonnes de registre comparées à la loupe sur un bureau d'auditeur, une ligne encerclée en rouge.
---

Every compliance program has two dashboards: the one about *permission* (is the policy right, is the gate configured?) and the one about *fact* (for each decision, did the promised thing actually happen, on time?). The second is where audits are lost, and almost nobody builds it.

The mechanism is unglamorous — **reconciliation**. For every sealed decision (an agent was authorized to act, a payment was approved, a generation was promised with marking), wait the declared deadline, then look for the matching sealed outcome. What you find sorts into named states, and the names are the whole point, because unnamed findings get argued away:

- **matched** — decision and outcome, both sealed. Fine.
- **late** — both sealed, but the outcome came after the deadline. Process exists, discipline doesn't.
- **pending** — decision sealed, window not yet passed. Nothing to see yet.
- **unconfirmed** — decision sealed, deadline passed, **no outcome**. The promise evaporated. This is the state auditors search for first.
- **open_gap** — a decision with **no deadline at all**. Someone authorized an action and nobody defined when it should complete. That's not a process; it's a hope.

And two findings that require looking across the whole ledger, not at single rows:

- **unauthorized** — an outcome explicitly flagged `unauthorized: true`. "Never authorized" — auditors search for the flag; the point of sealing it is that it can't be quietly cleaned up later.
- **unlogged_attempt** — an outcome with no decision sealed before it. This is the denominator lying: more outcomes than attempts means some attempts went through unrecorded. The count itself is the alarm.

## Why "did it happen" beats "was it allowed"

Permission-based compliance is checkable in a slide deck: show the policy, the config, the training certificate. Fact-based compliance can't be faked with documents, because it's a join over two independently sealed records — decision and outcome — and the join produces numbers. Number of unconfirmed. Number of open gaps. Number of lies in the denominator.

Those numbers are also the difference between governance theater and governance: any organization can state a policy; only one with reconciliation can state its **unconfirmed rate**. And once stated, it can only go down in public.

Reconciliation is not a NoireBox invention — it's how banks close their books and how double-entry accounting has worked for five centuries. The innovation, such as it is, is refusing to let agent decisions be the one corner of the company that runs on unverifiable narration.
