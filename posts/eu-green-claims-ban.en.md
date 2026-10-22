---
titre: The EU really did ban "eco-friendly" — just not quite the way you were told
resume: True: since 27 September 2026, Directive 2024/825 bans generic green claims and offset-based carbon neutrality. Fact-checked line by line against the official EUR-Lex text, plus a 20-minute landing-page audit.
date: 2026-10-22
themes: preuve, web
source: https://eur-lex.europa.eu/eli/dir/2024/825/oj
image: https://blog.noirebox.eu/img/eu-green-claims-ban.jpg
image_alt: Directive (EU) 2024/825 on a desk: stickers reading "eco-friendly", "climate neutral" and "green" crossed out by a prohibition symbol, gavel, EU flag and a landing-page audit on screen.
---

A widely shared [dev.to post](https://dev.to/shuttlewright/the-eu-banned-eco-friendly-on-27-september-check-your-landing-page-3855) claims the EU banned "eco-friendly" on 27 September, with "no grace period", and offers a 20-minute sweep of your landing page. Exactly the kind of title people reshare before checking — and the post itself cites no sources. So I went and read [the official text on EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L0825). Verdict: **the core claim is true**, but three nuances change what you actually need to do.

## What's true, checked against the text

Directive (EU) 2024/825 of 28 February 2024 — the "EmpCo" directive, *Empowering Consumers for the Green Transition* — amends the Unfair Commercial Practices Directive (2005/29/EC). Its Article 4 required Member States to transpose it by **27 March 2026** and apply the measures **from 27 September 2026**. This is neither a rumour nor a proposal: the date is in the text, and it has passed.

In practice, three families of practices become banned unfair commercial practices:

**1. Generic environmental claims.** Recital 9 names 'environmentally friendly', 'eco-friendly', 'green', 'nature's friend', 'climate friendly', 'biodegradable', 'biobased' and the like. Banned **unless** you demonstrate "recognised excellent environmental performance" relevant to the claim — recital 10 spells it out: the EU Ecolabel (Regulation 66/2010), an EN ISO 14024 type-I label recognised by a Member State, or class A under energy labelling rules — **or** the specification is provided "in clear and prominent terms on the same medium". The directive's own example: 'climate friendly packaging' = generic, banned; '100 % of the energy used in the production of this packaging comes from renewable sources' = specific, allowed.

**2. Neutrality bought with offsets.** Recital 12: claims that a product has a neutral, reduced or positive environmental impact "based on the offsetting of greenhouse gas emissions" are to be banned "in all circumstances". The directive lists the targeted phrasings: 'climate neutral', 'CO2 neutral certified', 'carbon positive', 'climate net zero', 'climate compensated'. The only real exception: a claim based on the actual life-cycle impact of the product — not carbon credits bought outside your value chain. On this point the dev.to post ("banned outright, cannot be fixed by wording") is correct.

**3. Self-made labels.** An "Eco certified" badge designed in-house is an unfair practice, unless it rests on a certification scheme meeting the directive's transparency and verifiability criteria, or is established by a public authority (recital 7).

The same text covers three cases people forget: a claim about the entire product when it only concerns one aspect ('made from recycled materials' when only the packaging is) is misleading (recital 11); presenting a legal requirement as a distinctive selling point is too (recital 15); and a promise of future environmental performance requires a measurable implementation plan verified by an independent third party (Article 6).

## What the viral post oversimplifies

**"No grace period"** — false by omission. The directive dates from 28 February 2024: industry had two and a half years to prepare, and Member States two years to transpose. What is true: after 27 September 2026 there is no further reprieve.

**"The words are banned"** — not absolutely. The word is not the offence; the offence is the generic, unverifiable character. Two escape hatches exist (recognised excellent performance, or a clear specification on the same medium). And 'sustainable', 'responsible', 'conscious' are worse than 'eco-friendly': recital 10 explicitly says they cannot even be justified by excellent environmental performance alone, because they also cover social characteristics.

**"Offsetting is banned"** — no: communicating about offsetting is not. You can still say you fund offsetting projects. What is banned is inferring from that that your product is "neutral".

Two scope notes. First, this is consumer law: it targets **B2C** commercial practices aimed at consumers in the EU, on any medium — website, ads, transactional emails, PDF invoices, packaging, checkout. A consumer-facing SaaS landing page is in scope; the technical docs of a strictly B2B offer are not. Second, don't confuse this with the "Green Claims Directive" (up-front verification of every explicit claim): that proposal was withdrawn by the Commission in June 2025. The 2024/825 one is adopted and in force.

Enforcement sits with national consumer protection authorities (in France, the DGCCRF), under the unfair-practices sanctions regime — fines of at least up to 4 % of annual turnover for widespread infringements. And expect the first report to come from a competitor or an NGO, not a regulator.

## The 20-minute audit, developer edition

One grep covers the first pass:

```bash
grep -rniE "eco[- ]?friendly|environmentally[- ]?friendly|climate[- ]?neutral|carbon[- ]?neutral|net[- ]?zero|sustainable|green|biodegradable|biosourcé|écologique|éco[- ]?responsable|neutre en CO2|compensé" \
  src content emails public \
  --include="*.html" --include="*.md" --include="*.js" --include="*.ts" \
  --include="*.tsx" --include="*.jsx" --include="*.json" --include="*.yaml"
```

Cover every surface, not just the repo: i18n files, metadata (`og:description`, JSON-LD, sitemap), email templates, generated PDFs, badges baked into CSS backgrounds — and the deployed site, which may serve a cached older version. Every hit follows the same rule: backed by a recognised label, made specific with figures and a source, or removed.

| Banned (generic) | Allowed (specific and verifiable) |
| --- | --- |
| "Green hosting" | "Hosted in Sweden, a region running on 97 % hydro (2025 energy mix, public source)" |
| "Climate neutral" (via offsets) | "−38 % scope 1+2 emissions since 2022, audited" — and drop the neutrality claim |
| In-house "Eco certified" badge | A recognised label (EU Ecolabel, ISO 14024 type I)… or nothing |

Document the change: commit, dated screenshot, before/after page. If an investigation reaches back to the 26 September version, being able to show the fix and its date matters.

## The real lesson

The biggest change isn't the word list — it's the inversion of the burden. A green claim is now, legally, an assertion you must be able to prove at the moment you publish it: figures, scope, source. It's a proof problem before it's a marketing problem. And if you have nothing to show, that's one less word to write — the fastest audit in the world.

Sources: Directive (EU) 2024/825 — [English text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L0825) and [French text](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024L0825) on EUR-Lex.
