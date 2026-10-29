---
titre: The 2 December 2027 logging deadline: a 90-day engineering plan
resume: Annex III teams got a year to implement Article 12, automatic event logging, six-month retention, tamper-evidence. Here is the plan that fits in one quarter, so the deadline becomes a formality instead of a fire drill.
date: 2026-10-22
themes: ai-act, conformité
source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/logging-90-day-plan.jpg
image_alt: Un planning de 90 jours épinglé au mur d'une salle d'ingénierie, trois colonnes de post-its verticales, une échéance surlignée au stabilo jaune.
---

Article 12, automatic event logging over the system's lifetime, with six-month retention for deployers, now bites on **2 December 2027** for Annex III high-risk systems. A year sounds like a lot. It isn't, for one reason: logging is not a feature. It's a contract between your system and every future audit, and contracts need design time.

The good news: the engineering fits in **90 days**. Here's the quarter, in three moves.

## Days 1–30: define the event contract

The obligation says "automatic recording of events", the regulation deliberately doesn't define your vocabulary; that's your job, and it's where most of the value hides.

- **Inventory the events that matter**: inputs, outputs, references to source data (per Article 12(1)'s traceability purpose), human interventions, overrides, errors, and, if you take Article 26 seriously, the moments human oversight actually happened.
- **Fix the schema**: one event type = fixed fields. Free-form strings don't audit; typed fields do.
- **Timestamps**: UTC only, fixed precision, generated at the source. An audit log mixing local times with daylight saving is unusable, and auditors check.
- **Decide what the log must NOT contain**: Article 12 logs are personal data under the GDPR. Digests and references, not raw content, is the pattern that keeps both laws happy.

## Days 31–60: make it automatic and tamper-evident

This is where "automatic" (Article 12(2)'s actual word) becomes architecture:

- **Emit at the source**, logging inside the request path, not a nightly export. If a human must remember, it isn't Article-12-grade.
- **Append-only storage**, the log must not be writable by the application that produces it. SQLite in append-only mode, a WORM store, or a journal with hash chaining: the requirement is that deletion and edit are *detectable*, not merely forbidden by policy.
- **Chain and sign**, each entry carries the hash of the previous one; batches get signed. Now yesterday's record can't be quietly improved.
- **Retention mechanics**, six months means a retention policy *and* proof of retention: the test is "show me the events from March", not "we keep everything".

## Days 61–90: rehearse the audit

- **Run the query an auditor will run**: "all actions on this decision, all overrides this quarter, six-month retention proof for this window." If answering takes a week of engineering, you don't have a log, you have archaeology.
- **Attack your own log**, try to edit an entry without detection. If you succeed, the tamper-evidence is decorative.
- **Write the one-pager**: where logs live, how long, who accesses, how integrity is verified. The document auditors read first.

## The catch

Every day of this plan deferred to 2027 costs more than today: retrofitting logging into a running high-risk system while it faces its first enforcement cycle is the most expensive engineering there is. Ninety days now buys you the only position that matters at a deadline: **bored**.
