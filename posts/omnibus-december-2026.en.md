---
titre: The AI Act wasn't postponed: five things that still bite on 2 December 2026
resume: The Digital Omnibus deferred most high-risk obligations, and the internet concluded "the AI Act is postponed". It isn't. Fact-checked against the consolidated texts: what moved to December 2027, what didn't move at all, and what lands in six weeks.
date: 2026-10-22
themes: ai-act, conformité
source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/omnibus-december-2026.jpg
image_alt: Calendrier du 2 décembre 2026 entouré en rouge sur un bureau d'auditeur, avec le texte consolidé de l'AI Act et le règlement Omnibus 2026/1744 posés à côté.
---

Since the Digital Omnibus entered into force on **27 July 2026**, one line keeps getting reshared: *the AI Act has been postponed*. I went back to the consolidated texts, the ones we version-pin in our own corpus, and checked what actually moved. Verdict: **most Annex III high-risk obligations moved to 2 December 2027. Everything else didn't.** And the things that didn't move are the ones that bite first.

## What moved (and to where)

For Annex III high-risk systems, the deferral is real and significant: automatic event logging (Article 12) and its six-month retention now bite on **2 December 2027** instead of the original schedule. If your planning assumed 2026, you got a year. Use it, more on that in a minute.

## What did NOT move

**1. Prohibited practices (Article 5), enforcement wave from 2 December 2026.** Social scoring, emotion inference in workplaces and schools, untargeted face-scraping databases: banned since February 2025, and the enforcement wave on the new prohibitions starts **in six weeks**. If your product or your customer's product touches a prohibition, 2027 is not your deadline. There is no deadline that helps you.

**2. Serious-incident reporting (Article 73).** Not deferred. A serious incident gets reported in days, not quarters, 15 days at most after awareness under the Article 73 mechanism. Incident reporting is an operational muscle: if you build it when you need it, you're late.

**3. GDPR Article 5.2, accountability.** Never part of the AI Act, never paused. Every processing decision you document "because the AI Act will require it", you were already required to under the GDPR. This is the obligation companies keep rediscovering during audits.

**4. Marking transition (Article 111(4), recital 38).** Generative systems placed on the market before 2 August 2026 got one narrow transition: until **2 December 2026**, this year, to comply with the Article 50(2) marking obligations. That's the four-month window, and it closes in six weeks.

**5. GPAI obligations.** Applied since 2 August 2025. Untouched by the deferral. Providers have been living under them for over a year.

**6. AI literacy (Article 4).** Applied since February 2025: a documented staff-training policy. Still the cheapest compliance item on the list, still the most common zero.

## What to do with the extra year

The deferral of Article 12 is the trap. A six-month, tamper-evident, automatic event log is not a feature you bolt on in November 2027, it's a data model, a retention mechanism, and an audit habit. Teams that treat 2 December 2027 as the start date will ship a log. Teams that treat it as the *deadline* will ship evidence.

We put the full date-by-date table in the open compliance dossier ([docs/COMPLIANCE-EU.md](https://github.com/noirebox/noirebox/blob/main/docs/COMPLIANCE-EU.md)), checked against the consolidated text. Read it before you forward the next "AI Act postponed" post.

*Every date in this article was checked against the versioned EUR-Lex consolidations our engine runs on (AI Act 02024R1689-20260727, GDPR 02016R0679-20160504). Sources, not vibes.*
