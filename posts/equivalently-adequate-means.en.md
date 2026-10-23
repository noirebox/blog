---
titre: Didn't sign the marking Code of Practice? The Commission has one word for you: prove it
resume: The Commission just published its Article 50 guidelines and a marking Code of Practice — with a fork hidden in one sentence. Sign the Code, or demonstrate "alternative equivalently adequate means". Nobody defines what that means. Here's the engineering reading.
date: 2026-10-23
themes: ai-act, preuve
source: https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations
image: https://blog.noirebox.eu/img/equivalently-adequate-means.jpg
image_alt: Une fourche stylisée à deux chemins — d'un côté un cahier de charges signé par plusieurs mains, de l'autre un reçu scellé à cachet de cire avec une loupe d'auditeur — sous un panneau « Article 50 » aux étoiles européennes.
---

Two quiet publications just redrew the marking landscape for anyone shipping generative AI in the EU: the Commission's **[guidelines on Article 50 transparency obligations](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)** (shaped by a public consultation on marking), accompanied by a **Code of Practice on the Transparency of AI-generated Content**. Article 50 applies since 2 August 2026, and the transition for systems already on the market closes on **2 December 2026** — weeks from now.

Buried in the guidelines is one sentence that matters more than the rest of the document combined. Providers and deployers of generative AI who do not sign the Code of Practice:

> "will have to demonstrate compliance with obligations for marking and labelling of AI-generated content through **alternative equivalently adequate means**."

Read that again. The Commission drew a fork: **sign the Code and inherit its safe harbor, or stay out and *demonstrate* that whatever you do instead is equivalently adequate.** What it did not do — deliberately — is define what "demonstrate" means. No format is pinned, no certification path exists, standards are still pending. The freedom of means comes with the full burden of proof.

## "Equivalently adequate" is an engineering spec in disguise

Adequate compared to what? To the bar the Code sets for its own signatories. So the non-signatory's job is to demonstrate, about their own marking regime, the four things any auditor will probe:

**1. The marking survives reasonable transformations.** A watermark that dies on re-encode, crop, or screenshot demonstrates nothing — the Code's bar is detection after real-world handling, and "equivalently adequate" means meeting that same bar, not declaring it.

**2. Every generation is evidenced.** Not "we mark our outputs" — *this* output, digest-bound, timestamped, sealed at generation time. The claim lives per artifact, not per policy page.

**3. Coverage is provable.** The demonstration that kills: *show me one generation without a matching proof.* If your evidence is a log your own application can edit, the auditor is reading your diary. If it's an append-only, hash-chained, signed record where a generation without its receipt is a named, sealed finding — the question answers itself.

**4. A third party can check offline.** Equivalence to a Code that anyone can read means your proof must be verifiable by someone who doesn't trust your infrastructure, your uptime, or your willingness to hand over logs.

That's not a legal memo. It's a systems specification — and it happens to be the exact shape of the marking receipts we shipped in [noirebox v0.24.0](https://github.com/noirebox/noirebox): sha256 digest of the output as delivered (never the content), modality closed to Article 50(2)'s four, methods as a closed set with the C2PA manifest digest bound both ways, fail-closed status (`marked | not_marked | exempt` — an exemption must name its carve-out), and a coverage join where a `not_marked` receipt *is* the sealed gap and a later mark erases nothing.

## The other thing the guidelines settled — and left open

Two details worth noting. The guidelines confirm the deployer-side duties people forget: deepfake disclosure, notices to people exposed to emotion recognition and biometric categorization, and AI-published text on public-interest matters without human editorial control. And they give the contour of the exemptions — "standard editing" is treated as out of scope. But on the marking *how*, the Commission stayed silent on purpose: formats and robustness testing belong to future standardization. Which means the window for defining what "adequate demonstration" looks like is **open right now** — and the first organizations that publish credible, verifiable proof regimes are writing the de facto standard for everyone behind them.

## The clock

Six weeks to the 2 December 2026 transition close. The fork costs you either way: signing means adopting the Code's practices; not signing means building the demonstration. Both take longer than the deadline suggests. But only one of them leaves you with something you can hand to any auditor, in any jurisdiction, forever — regardless of what the next Code revision says.

We wrote about the underlying trap before — [a label can be stripped, a receipt can't](https://blog.noirebox.eu/en/label-stripped-receipt-cant) — and about the [chatbot-side duties teams forget](https://blog.noirebox.eu/en/chatbot-art50-production). The guidelines just turned that trap into official policy: compliance by declaration is over for anyone outside the Code. Proof is the remaining path.
