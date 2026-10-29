---
titre: Six months of logs: the obligation nobody is engineering for
resume: Article 12 requires automatic event logging with six-month retention on high-risk systems. The deferral to December 2027 reads like permission to wait. It isn't, "automatic" has a technical meaning, and a log you can edit is not a log.
date: 2026-10-22
themes: ai-act, conformité
source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/six-months-of-logs.jpg
image_alt: Un journal de bord scellé posé sur un clavier, face à un terminal affichant un log effaçable, éclairage de salle serveur.
---

Article 12 of the AI Act is the most engineering-shaped obligation in the whole regulation, and it just got deferred to **2 December 2027** for Annex III systems. Reading the coverage, you'd think that was a pardon. It reads more like a countdown.

## What the text actually requires

Two paragraphs, two obligations:

- **Article 12(2)**, high-risk systems must technically allow **automatic** recording of events (logs) over the entire lifetime of the system. Not "logging you can toggle". Not "logs you export manually at audit time". *Automatic recording*, built in.
- **Article 12(6)**, deployers must keep the logs **at least six months** by default, unless other law says otherwise.

Now the word everyone skims past: *automatic*. It has a technical meaning, and it's adversarial. If producing the log requires a human to remember, a cron job someone owns, or an export someone runs before an audit, a failure at any of those steps produces silence, and silence is indistinguishable from compliance. The obligation is written so that the absence of a log is itself evidence of a failure. That's the design.

## The three questions an auditor will actually ask

Not "do you have logs?", everyone says yes. The questions that end careers:

1. **What's in an event?** If you can't produce a fixed event vocabulary (what happened, to what, when, with what reference), your log is a pile of strings. Strings don't audit.
2. **Can it be edited?** A log stored where the application can write freely is the operator's own story. The technical question is: what makes tampering *detectable*, hash chaining, signatures, append-only storage?
3. **Prove six months.** Retention isn't "we keep everything" (that's a GDPR problem) or "we rotate after 30 days" (that's a gap). Six months, per event, provable.

And the GDPR doesn't pause while you figure this out: those logs are personal data. Retention discipline and access control apply *to the log itself*.

## What the deferral is for

2 December 2027 is not "start then". It's "be able to prove it then". A year is exactly enough to do this properly: define the event vocabulary, wire automatic recording into the system's actual operations, put the log on tamper-evident storage, and run one full audit cycle as a rehearsal.

Teams that start in September 2027 will ship a log. Teams that start now will ship **evidence**, and the difference is the same one that separates a black box recorder from a pilot's diary.

We build exactly this (append-only, hash-chained, signed, offline-verifiable, [noirebox](https://github.com/noirebox/noirebox), MIT), and the date-by-date obligation table is open in [docs/COMPLIANCE-EU.md](https://github.com/noirebox/noirebox/blob/main/docs/COMPLIANCE-EU.md). Six months of logs is not a storage problem. It's an honesty architecture.
