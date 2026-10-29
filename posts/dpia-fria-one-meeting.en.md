---
titre: DPIA and FRIA: one meeting, two laws
resume: If you deploy a high-risk AI system in the EU, you owe both a GDPR data protection impact assessment and an AI Act fundamental rights impact assessment. They overlap about 70%, and teams that run them separately do the work twice.
date: 2026-10-22
themes: ai-act, conformité
source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/dpia-fria-one-meeting.jpg
image_alt: Deux grilles d'analyse superposées en transparence sur une table de réunion, les cases communes surlignées dans la même couleur.
---

If your organization deploys high-risk AI systems, CV screening, credit scoring, anything in Annex III, you are standing in the overlap of two assessment regimes: the **GDPR's Data Protection Impact Assessment** (Article 35) and the **AI Act's Fundamental Rights Impact Assessment** (Article 27). They have different names, different legal bases, and about 70% shared content. Most teams discover this after writing both from scratch.

## Who owes what

- **DPIA (GDPR art. 35)**, the *controller*, before processing likely to result in high risk to individuals. This isn't new: the CNIL's 2018-326 deliberation published trigger lists years ago, and automated decision-making with legal effects has been a classic trigger since 2018. AI Act high-risk processing is, in practice, always DPIA territory.
- **FRIA (AI Act art. 27)**, the *deployer* of a high-risk system that is a public-body or private provider of public services, or subject to certain banking/insurance rules, before first use. New as of the AI Act's application dates; it asks about the *fundamental rights* side, which rights are affected, for which categories of persons, what human oversight measures, what remedies.

Note the subjects differ: the DPO/data controller owns the DPIA; the deploying organization owns the FRIA. Same building, different signatures.

## What overlaps (do it once)

Process description, system purpose, categories of affected persons, risk identification and severity, mitigation measures, human oversight arrangements, residual risk sign-off. If your DPIA template is worth anything, the FRIA can be *assembled* from it plus an Article 27-specific annex, not written from zero.

## What does NOT overlap (the traps)

- **FRIA's rights catalogue is broader than data protection**, non-discrimination, access to justice, freedom of expression, human dignity. A DPIA can be "no personal data, no problem"; a FRIA cannot.
- **The cadence commitments**: we hold both to *at least annual re-examination*, DPIA reassessed when risk changes, FRIA re-evaluated yearly and before material changes. Assessments are processes, not PDFs.
- **Evidence**: both assessments produce obligations with dates (publish a trigger list, document the process, keep decisions reviewable). An assessment whose conclusions can't be shown to have shaped the deployment is a shelf document, and both laws increasingly ask for the receipts, not the shelf.

## The one-meeting structure

Run them as one investigation with two reporting templates: the same inventory session feeds both, with a mapping table in the middle (DPIA section ↔ FRIA section) so nothing is double-authored and the non-overlaps are visible. Organizations that do this ship both assessments in the time it used to take to schedule the second meeting.

And the 2027 corollary: when Article 12 logging arrives for these systems, the assessment says what *should* have been logged; the journal says what *was*. Auditors read both, and the distance between them is your real compliance score.
