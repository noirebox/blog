---
titre: A label can be stripped. A receipt can't.
resume: Article 50(2) wants machine-readable marking on AI-generated content. Every marking SDK shipping this winter has the same blind spot: the label lives inside the artifact and dies with it. The proof that you marked an output needs to live somewhere else.
date: 2026-10-22
themes: preuve, ai-act
source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/label-stripped-receipt-cant.jpg
image_alt: Une image générée par IA dont le filigrane se détache comme un autocollant, à côté d'un reçu scellé à cachet de cire rouge intact.
---

Article 50(2) of the AI Act requires providers of generative systems to mark synthetic output in a **machine-readable way** — and since the Omnibus, generative systems already on the market before 2 August 2026 have until **2 December 2026** to comply. A wave of marking SDKs is shipping for that date. Every one of them shares the same blind spot, and almost nobody names it:

**the label lives inside the artifact — and dies with it.**

Strip the watermark, re-encode the image, crop the header, run the text through a paraphraser: the marking is gone, and a stripped label is indistinguishable from one that never existed. Meanwhile, the "evidence log" that hosted SDKs offer is the operator's own database — editable by whoever holds it. You marked your outputs; the *proof that you did* is one `UPDATE` away.

## The receipt is what survives

This is exactly the gap our v0.24.0 marking receipts close. The receipt is a signed event in an append-only, hash-chained journal, bound to:

- the **sha256 digest of the output as delivered** — the digest, never the content, so no personal data or IP leaks into the journal;
- its **modality** (text, image, audio, video — Article 50(2)'s four);
- the **methods applied** — a closed set, and if you used a C2PA manifest, the manifest digest is bound *both ways*: the receipt names it, the manifest's absence breaks the check;
- a **fail-closed status**: `marked | not_marked | exempt` — and an exemption must name which of the Article 50 carve-outs it claims. A bare "exempt" is refused at seal time.

Then the part that turns records into an audit: **coverage**. Every generation event carrying an output digest must meet a `marked` or `exempt` receipt for that digest. A `not_marked` receipt *is* the gap, sealed — and a later mark does not erase it. The auditor doesn't ask "do you mark your outputs?"; they ask "show me one generation without a matching receipt." Either you have a sealed answer or you have a finding.

## Why this matters more than the deadline

The 2 December 2026 transition applies to systems already on the market. The SDK you ship with will handle the label. What it won't handle is the day a client, a regulator, or a court asks: *prove that this specific output was marked, at generation time, under the rules you claim to follow.*

A watermark answers "is this marked?" — until someone strips it. A receipt answers "did you mark it?" — permanently, and verifiable offline by someone who doesn't trust you.

That's the difference between complying and being able to prove you complied. Only one of them survives contact with an audit.

*The marking receipt is real, shipped, and tested: [noirebox v0.24.0](https://github.com/noirebox/noirebox) (MIT), with the coverage check and the C2PA bridge — the act of complying is not a media edit, so our seals speak the Content Credentials namespace, not the other way around.*
