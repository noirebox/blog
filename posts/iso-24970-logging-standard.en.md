---
titre: The logging standard just found its shape: EN ISO/IEC 24970 is in final draft
resume: The harmonised standard for Article 12 record-keeping, AI system logging, with an information model and integrity requirements, reached final draft (FprEN) on its way to EN ISO/IEC 24970:2026. Here's what it means for your 2 December 2027 deadline, and the one honest gap we owe you.
date: 2026-10-23
themes: ai-act, conformité
source: https://www.iso.org/standard/88723.html
image: https://blog.noirebox.eu/img/iso-24970-logging-standard.jpg
image_alt: La couverture d'un standard ISO/IEC 24970 en cours d'impression, posée sur un registre chaîné et cadenassé, avec un calendrier décembre 2027 en arrière-plan.
---

For a year, every honest guide to Article 12 of the AI Act ended the same way: *the regulation requires automatic event logging, but doesn't define your event vocabulary, the harmonised standards are still coming.* That asterisk just shrank. **EN ISO/IEC 24970, *Artificial intelligence, AI system logging*, has reached its final draft stage (FprEN/FDIS)** on its way to publication as EN ISO/IEC 24970:2026, and it is the CEN-CENELEC candidate **harmonised standard for Article 12's record-keeping obligations**.

## Why "harmonised" is the word that matters

Anyone can write a logging standard. A *harmonised* standard is different: building on it gives you the **presumption of conformity** with the obligation it supports. That converts the Article 12 conversation from "prove your logging is adequate", an argument, into "we implemented EN ISO/IEC 24970", a citation. For the teams facing the 2 December 2027 deadline for Annex III systems, that's the difference between defending a design and referencing one.

## What's in it (from the public record)

The scope, per ISO's own listing: **common capabilities, requirements, and a supporting information model for logging of events in AI systems**, supporting transparency and accountability, designed to work with your risk management framework (ISO/IEC 42001, ISO/IEC 23894). Analysts following the draft map its coverage to the Article 12 pain points: **what events to log, how, retention, and integrity/immutability of the records**. In other words: the event vocabulary question we told you was "yours to answer" is being answered, as a formal information model.

## Three consequences for your logging plan

**1. Don't invent a private format now.** If your 90-day plan (we published one) starts with "fix the schema", anchor that schema's shape on the 24970 information model, even from the draft. A bespoke event format that predates the harmonised standard is a migration project in 2027.

**2. Integrity is going from good practice to cited requirement.** Hash-chained, append-only, tamper-evident records, the things this blog keeps insisting on, are exactly what "integrity/immutability" in a logging standard means operationally. The standard legitimizes the architecture; it doesn't change it.

**3. The presumption works forward, not backward.** Compliance for Annex III systems bites 2 December 2027; the standard's publication plus citation will be the smoothest path *at* that date. Late adopters who built logging in 2027 will retrofit to the information model under time pressure, the expensive kind of archaeology.

## The honest part

We haven't audited our own journal against the final text, because the final text isn't public yet. What we can say: a typed event vocabulary, hash chaining, and signed events are exactly the species of requirement the draft is reported to contain, which is why we built them before there was a number to cite. **When EN ISO/IEC 24970:2026 publishes, we'll do this properly: a public, line-by-line mapping table between the standard's requirements and the journal's behavior**, including the rows where we don't comply yet.

That's the follow-up to watch. The standard found its shape; the deadline hasn't moved. Teams that read it now will be citing it in 2027. Teams that wait will be reconstructing their logs to match it.

This is the third piece in our logging series, with [the six-month obligation nobody engineers for](https://blog.noirebox.eu/en/six-months-of-logs) and [the 90-day plan](https://blog.noirebox.eu/en/logging-90-day-plan).
