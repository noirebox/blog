---
titre: Proving what your agent was never told
resume: "The agent used information it was never given" — until now, that accusation was unprovable in either direction. Admission receipts seal the moment outside context enters an agent's state, with the four invalid promotions and the laundering vocabulary refused at seal time.
date: 2026-10-22
themes: agents, preuve
source: https://github.com/noirebox/noirebox/blob/main/docs/ADRs.md
image: https://blog.noirebox.eu/img/proving-what-agent-was-never-told.jpg
image_alt: Une enveloppe scellée glissée par une fente dans une chambre forte, alors qu'un flux de documents passe à côté sans y entrer.
---

The hardest dispute in agent auditing has two versions. The accuser's version: *"the agent recommended our client's confidential figures — it must have read the private deal room."* The operator's version: *"it never saw that data; it inferred from public filings."* Until recently, both were faith positions. Nobody could prove what an agent had or hadn't taken into its state.

That's the problem admission receipts attack — not what the agent *did*, but the earlier, quieter event: **the moment something outside its context was admitted into it.**

## The receipt is for the promotion, not the act

You-An Lin's framework gives the vocabulary: capability is not authority, and the dangerous move is the *promotion* — when the mere presence, relevance or plausibility of information gets silently promoted into "the agent may use this". An admission receipt seals that promotion as its own signed event:

- **who** admitted it, **from where**, and on **which surface** it arrived;
- **which transition** occurred — one of four invalid promotions, named: *visibility→admission, capability→move, relevance→payload, style→stance*;
- the **basis**: the independent warrant — a user instruction, a prior receipt, an explicit scope grant;
- the **decision**, failing closed: `admitted | denied | admission_undecidable | admission_check_not_run`. Undecidable is never clean, and a check that didn't run is recorded as skipped — no silent passing.

Then the refusal that gives the receipt its teeth: four things are **never a basis** — the material's *presence*, *relevance*, *plausibility*, *usefulness*. "It was in the thread", "it seemed relevant", "it looked plausible", "it would help the user" — those are the laundering vocabulary, and the sealer rejects them by name. The field that exists to carry an independent warrant refuses to carry the thing it exists to refuse.

## Why accusers benefit too

This is not a shield for operators; it cuts both ways. When admissions are sealed, the accusation "it read the deal room" becomes checkable: replay the sealed sequence. Either there's an admission receipt with a legitimate basis — the operator shows it — or there isn't — the accuser's theory loses its mechanism. **Both false accusations and true ones become decidable.** That's what "tamper-evident" buys: not protection from audit, but an end to unfalsifiable ones.

Paired with decision receipts — which seal the model engine's full probability distribution over its allowed answers, plus the engine's own expressed doubt, bound to a sealed question-set spec — you can reconcile after the fact whether the decision could have been made without the admitted material. The reconciliation has named findings, and one of them is exactly this shape.

"Provable, not assumed" is the whole product thesis in four words. The admission receipt is where it matters most, because the admission is where an agent stops being a tool and starts being a witness.
