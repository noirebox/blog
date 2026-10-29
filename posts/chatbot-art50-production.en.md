---
titre: Your chatbot must say it's a chatbot: Article 50, tested in production
resume: Transparency obligations for AI interactions, synthetic content and deepfakes applied in August 2026, and the transition for systems already on the market closes on 2 December 2026. What "machine-readable marking" means when someone screenshots it.
date: 2026-10-22
themes: ai-act, agents
source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/chatbot-art50-production.jpg
image_alt: Une conversation de chatbot affichée sur mobile avec un badge « IA » visible, à côté d'un même contenu dont le badge a disparu après recadrage.
---

Article 50 is the part of the AI Act your users can actually see, and it has applied since **2 August 2026**. Generative systems placed on the market earlier got one narrow transition, until **2 December 2026**, and it's closing. Here's what the article actually demands, split into the four things people confuse:

1. **Interacting with AI? Say so** (art. 50(1)). If a person interacts with an AI system, the system must make itself known, unless it's obvious to a reasonable person. Your support chatbot with a human name and no disclosure: that's the target case.
2. **Synthetic output must be marked, machine-readably** (art. 50(2)). Text, image, audio, video, the provider must mark generated content in a format machines can detect, and disclose artificiality to whoever sees it.
3. **People exposed to emotion recognition or biometric categorization must be informed** (art. 50(3)), the exposed persons, not just the operator.
4. **Deepfakes must be disclosed** (art. 50(4)), artificial images, audio or video "generated or manipulated with AI" carry a disclosure obligation.

## The test that matters

Disclosure is easy to demo and easy to lose. The failure mode isn't "we never marked it", it's **the marking that doesn't survive contact with the real internet**: a screenshot strips nothing, but a crop, a recompression, a copy-paste of text, a platform re-encoding, each transformation is a chance the machine-readable layer dies while the content lives on.

So the question to engineering is not "do we call the marking SDK?" but: **does the marking survive reasonable transformations, and can we prove it did?** Two checks we run:

- **Survival across transformations**, re-encode the image, recompress, crop; the marker must still be detectable. If your marking only survives the happy path, it doesn't survive.
- **Coverage, sealed**, for every generation, a signed receipt binding the output's digest to its marking status. The audit question becomes mechanical: *show me one generation without a matching receipt.* Either the journal has a sealed answer, or you have a finding you can't argue with.

## The part teams get wrong first

Teams implement 50(2), the marking, and forget 50(1) and 50(3) are user-facing obligations with no SDK: the chatbot's first message, the badge in the UI, the notice to people whose emotions are being categorized. Those are configuration and copywriting, they're auditable in five minutes, and they're the fastest compliance wins in the whole regulation.

Then the deeper trap: the evidence log that comes bundled with your marking SDK is your own database. Editable by whoever holds it. The receipt that survives an audit lives outside the artifact, signed, append-only, that's the difference between marking and being able to prove you marked ([previous post](https://blog.noirebox.eu/en/label-stripped-receipt-cant)).

December 2nd is weeks away. The badge costs you an afternoon. Do that one today.
