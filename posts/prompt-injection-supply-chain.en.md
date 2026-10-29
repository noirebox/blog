---
titre: Prompt injection is a supply-chain problem now
resume: Your agents consume web pages, tickets and emails written by strangers. That makes prompt injection a dependency vulnerability, and like every supply-chain risk, it's managed with SBOMs, replayed attack catalogs and evidence, not with hope.
date: 2026-10-22
themes: agents, sécurité
source: https://github.com/noirebox/noirebox
image: https://blog.noirebox.eu/img/prompt-injection-supply-chain.jpg
image_alt: Une chaîne d'approvisionnement stylisée dont un maillon est un e-mail hostile, tenant en otage les maillons suivants, style schéma d'audit.
---

Nobody asks whether your web framework "resists" malicious HTTP requests as a matter of hope; you run a WAF, patch CVEs, and audit dependencies. Prompt injection deserves the same boring treatment, because the exposure is the same shape: **your agents consume content written by strangers**, pages, tickets, emails, PDFs, and any of it can carry instructions aimed at the agent instead of the reader.

Treating that seriously means borrowing the supply-chain playbook:

## 1. The attack catalog is an asset, not an anecdote

"We tested against some famous injections" is the security equivalent of "we updated our dependencies sometimes". The working form is a **versioned catalog of attack fixtures**, each a real injection pattern with an expected outcome, replayed **in CI** on every change, the wayCVE regression tests work. When a new technique is published, it becomes a fixture; from then on, every build proves it stays defeated. The catalog grows monotonically; defenses can't silently rot.

## 2. Tiers, because cost follows every request

Scanning every transcript with a large model is the "rewrite it in Rust" of guardrails: true and unaffordable. The working architecture is tiered, cheapest first: **regex** for the obvious (deterministic, testable, free), a **small local model** (our French one is 293 KB, small enough to run on everything, trained on a versioned French corpus) for paraphrases, and an **LLM judge** only for the ambiguous residue. The format is unified across tiers, positions and category, so the tier is an implementation detail, not a schema change.

## 3. The guardrail itself needs evidence

Here's the part that turns security into compliance: a guardrail that blocked an attack is a nice story; a guardrail whose block is **a sealed, signed event**, pattern, positions, category, timestamp, is an audit fact. And its complement matters just as much: every admitted transcript should be sealed too, so the eventual question "did the guardrail see this input?" has a journal answer instead of a shrug.

Why both sides? Because incidents are disputes. The customer says the agent leaked; you say the guardrail held. Two sealed event streams, blocks and admissions, turn the dispute into a query.

## 4. Yes, we rejected the big vendor model, measured

The tempting shortcut is a famous open-weights injection classifier. We evaluated one, the industry's standard, and rejected it on measured criteria: English-trained while our transcripts are French; binary output where an audit needs categories and positions; a gated license where a product needs a frictionless artifact. The evaluation is written down as an ADR, which is the real point, **rejections with reasons are institutional memory; vibes are churn.**

Prompt injection won't be "solved". It will be *managed*, cataloged, replayed, tiered, and evidenced, exactly like every supply-chain risk before it. The teams that start keeping the evidence now will be the ones with answers when the first serious incident lands in someone's jurisdiction.
