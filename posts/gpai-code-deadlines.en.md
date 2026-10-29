---
titre: GPAI providers: the Code of Practice deadlines that came and went
resume: The GPAI Code of Practice isn't law, but it's what the Commission reads your Article 53-55 compliance against. Crawler permissions, 14-day downstream notices, incident reporting in days, model documentation every six months. Most providers miss at least two.
date: 2026-10-22
themes: ai-act, conformité
source: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai-ai-act
image: https://blog.noirebox.eu/img/gpai-code-deadlines.jpg
image_alt: Un cahier des dates d'échéance barrées (robots.txt, 14 jours, 6 mois, 2/5/10/15 jours) posé sur un rack serveur, tampon Commission européenne.
---

General-purpose AI providers have been living under Article 53–55 obligations since **2 August 2025**, untouched by the Omnibus deferral, which only moved high-risk dates. And the practical reference for "how do I show I comply?" is the **GPAI Code of Practice**. Important distinction, often blurred: the Code is not the law. But it's the framework the Commission recognizes, and deviating means explaining yourself with equal evidence. Here are the four deadlines that keep being missed.

## 1. Crawler permissions, the robots.txt commitment

The Code commits signatories to respect robots.txt-style crawler permissions for their training crawlers. This is the one obligation where compliance is **externally verifiable in minutes**: point any crawler auditor at your user-agents and see whether they honor disallow rules. If your data pipeline predates your compliance team, this is the place they've never looked.

## 2. Downstream information, the 14-day notice

When something material changes (documentation, capabilities, safety-relevant updates), downstream providers integrating your model get a **14-day** notice commitment. In practice this means your release process needs a notification step *before* the weights or API change lands, not a changelog after. Teams with a weekly ship cadence discover this requirement the hard way.

## 3. Incident reporting, 2, 5, 10, 15 days by severity

The Code's incident timeline is severity-tiered: roughly **2 days** for the most critical incidents, scaling to 5, 10 and 15 days down the scale. Compare with what most providers have, an email alias nobody owns. The obligation isn't the hard part; having someone accountable for the clock is.

## 4. Model documentation, refreshed every six months

The Model Documentation Form isn't a one-time filing. The commitment is to keep it **current on a six-month cycle**. Put a recurring calendar entry on it today; the providers who will fail this are the ones for whom the Form was a launch-day artifact that now describes a model that no longer exists.

## The pattern behind all four

None of these are research problems. They're **process obligations with clocks**, and clocks are what paper compliance dies on. The interesting engineering question is the one we keep coming back to on this blog: when you claim you reported in 2 days or notified in 14, *what makes that provable afterwards?* An email in your own sent folder is your word. A sealed, timestamped event in a journal neither you nor we can quietly edit is evidence.

The Code is voluntary. Being believable isn't.
