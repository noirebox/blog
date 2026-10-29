---
titre: In six weeks, your AI becomes a strictly liable product, and the court can order your logs disclosed
resume: While everyone watches the AI Act's December dates, the new Product Liability Directive (EU) 2024/2853 quietly applies on 9 December 2026: software and AI systems are now "products", liability is strict across the whole chain, and courts can compel you to disclose your evidence.
date: 2026-10-29
themes: ai-act, preuve
source: https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng
image: https://blog.noirebox.eu/img/product-liability-december-2026.jpg
image_alt: Un marteau de juge posé sur un clavier, à côté d'un journal scellé remis dans une pochette de procédure estampillée « disclosure ».
---

Two December dates are hogging every AI-compliance calendar: the Omnibus transitions and the enforcement wave on **2 December 2026**. The date that should worry product teams more arrives **one week later, in near-total silence**.

From **9 December 2026**, the new Product Liability Directive, **[Directive (EU) 2024/2853](https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng)**, applies to products placed on the market or put into service from that date. It replaces a 1985 text written for physical goods. The 2026 version has read the last decade:

- **Software and AI systems are explicitly "products."** Not an extension by analogy, the directive names them. A defective model update, a hallucinating agent, a screening tool with a built-in bias: strict liability territory.
- **The whole chain is on the hook.** Manufacturer, component maker, importer, fulfilment provider, the claimant picks whom to sue. In a multi-vendor agent stack, that means the liability conversation reaches everyone who touched the pipeline.
- **Damages include data loss and corruption**, alongside personal injury and recognized psychological harm. Yes: the integrity of your records is itself a compensable interest.

## The part nobody reads out loud

Defect is one thing; proving it is another, and here the directive does something unusual for claimants facing opaque systems: **courts can order the party holding the evidence to disclose it**, and where disclosure is refused or incomplete, the burden of proof shifts by presumption toward the defendant.

Read that twice, because it rewrites what your logs *are*.

Until now, "we keep internal logs" was a cost line. From 9 December, in a product-liability dispute over an AI system, the log is **the discovery corpus**. The court doesn't ask whether you kept records; it can compel you to produce what you have, and if what you have is editable, retrospective, or conveniently incomplete, the *absence of integrity becomes the other side's argument*. The directive's easing of the claimant's burden is aimed precisely at systems whose inner workings are hard to probe: your opacity is their presumption.

## Where this meets the journal

This is the loop closing on everything this blog argues. A disclosure order makes the integrity of your records a **litigation property**:

- A hash-chained, append-only, signed journal can be handed over **with proof of its own integrity**, the recipient verifies the chain instead of trusting your word.
- An editable log handed over the same way is a liability multiplier: whatever it says, the counterparty's expert will establish it could have said anything.
- And the reconciliation layer, decisions joined to outcomes, with named states, turns "what actually happened" from a narration into a query. In a strict-liability regime, the party with the coherent narrative wins the room.

The 1985 directive made product manufacturers keep records; nobody much cared what they looked like. The 2026 one makes the *quality of your evidence* part of your legal position.

## What to do in the next six weeks

1. **Inventory what your AI systems decide and do**, that inventory is your future disclosure corpus. If a decision class isn't recorded, you'll be disclosing its absence.
2. **Start sealing decisions and outcomes now**, with the timestamps that matter (the directive's claims window runs a decade from placement on market, your logs need to outlive your memory of the product).
3. **Treat log integrity as a legal requirement, not an ops nicety**: append-only, chained, signed, verifiable by a third party who wasn't in the room.

The AI Act tells you what to log. The Product Liability Directive decides what your logs are worth in court. One regulates the machine; the other prices its failures. Build for both, and December stops being scary.
