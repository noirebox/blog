# TOPICS.md, vivier de sujets (blog.noirebox.eu)

Sujets calibrés sur le ton maison (green-claims) : un titre qui corrige une
croyance, un verdict vérifié ligne à ligne contre le texte officiel (EUR-Lex
consolidé, notre corpus, pins versionnées), et un « quoi faire concrètement ».
Chaque sujet = paire `posts/<slug>.en.md` + `.fr.md`, thèmes dans le vocabulaire
existant. ★ = prochain à écrire (pourquoi : fenêtre de calendrier).

---

## Pilier A, AI Act : ce que le texte dit vraiment (calendrier)

### 1. ★ "Omnibus: what actually still bites on 2 December 2026"
- **Angle** : le Digital Omnibus (Reg. (EU) 2026/1744, en vigueur 27 juillet 2026) a fait reporter
  une grosse partie du haut risque, et tout le monde a retenu « l'AI Act est repoussé ». Faux.
  Ce qui mord dans 6 semaines : vague d'enforcement sur les **pratiques interdites (art. 5)**,
  **art. 73 (signalement d'incidents graves)**, **art. 50(2) marquage** avec sa transition
  art. 111(4) pour les systèmes génératifs déjà sur le marché (jusqu'au 2 déc. 2026),
  et le RGPD art. 5.2 (accountability) qui n'a jamais bougé.
- **Pourquoi maintenant** : la date est dans 6 semaines. Aucun blog ne la traite précisément.
- **Sources** : EUR-Lex 02024R1689-20260727 (art. 111(4), recital 38), Reg. 2026/1744.
- **Verrou produit** : la table de conformité date-par-date = `docs/COMPLIANCE-EU.md` du repo.

### 2. "Six months of logs: the obligation nobody is engineering for"
- **Angle** : art. 12(2)+(6), journalisation automatique de la durée de vie, rétention ≥ 6 mois.
  Le report au 2 décembre 2027 (annexe III) n'est pas une permission d'attendre : « automatique »
  a un sens technique (pas d'export manuel), et un journal éditable n'est pas un journal.
  Ce que demandera un auditeur : vocabulaire d'événements, horodatage, intégrité, preuve de rétention.
- **Sources** : art. 12 consolidé, art. 19 (conservation), CNIL + données de logs.
- **Verrou produit** : le journal scellé EST la réponse ; démo normexe RIA-012.

### 3. "Your chatbot must say it's a chatbot, art. 50 in production"
- **Angle** : interaction (50(1)), contenu synthétique lisible par machine (50(2)), deepfakes (50(4)).
  Comment on TESTE que c'est vrai en prod (marquage qui survit aux transformations), et ce que
  change la transition 111(4) pour les systèmes déjà en ligne.
- **Verrou produit** : marking/0.1 (v0.24.0) + le pont C2PA (ADR 011/024).

### 4. "GPAI: the Code of Practice deadlines that came and went"
- **Angle** : le Code GPAI n'est pas la loi, mais la Commission regarde. Dates du Code :
  robots.txt pour les crawlers (M1.3), délais de signalement d'incidents 2/5/10/15 j (M9.3),
  Model Report à jour tous les 6 mois (M7.6), information aval 14 j (M1.2). Ce qu'un
  provider moyen ne fait pas aujourd'hui.
- **Sources** : GPAI Code of Practice (ingéré dans la KB), art. 53-55.
- **Audience** : providers, élargit le lectorat au-delà des déployeurs.

## Pilier B, gouvernance des agents : la conversation de 2026

### 5. "Enforcement vs evidence: why OWASP ACS and NIST agent identity still need a journal"
- **Angle** : tour d'horizon honnête de la couche contrôle (OWASP ACS, NIST agent identity,
  KedgeFlow, UAI-BLOCK) et de la couche preuve, l'aveu de KedgeFlow lui-même
  (« a permissive policy still authorized an undesirable effect ») est L'argument.
  Complémentaires, pas concurrents ; NoireBox = la couche que tout le monde oublie.
- **Sources** : docs/RELATED-WORK.md (déjà écrite), arXiv 2610.14810.
- **Ton** : peer-to-peer, cité, zéro marketing, la version blog de la réponse à Bilent.

### 6. "Capability is not authority, and logs are not evidence"
- **Angle** : partir du papier SSRN de Dr. Bunic (les 4 tests : accountability, auditability,
  scale, durability) et de You-An Lin, puis poser la question que personne ne pose :
  qu'est-ce qui rend un enregistrement une PREUVE ? (chaîne de hash, signature, vérification
  offline, catalogue d'attaques rejoué). Auto-score honnête : scale et durability ouverts.
- **Sources** : SSRN, ADR 026/028, SCAR.

### 7. "Who did this, really? Execution-time identity for AI agents"
- **Angle** : l'identité revendiquée vs l'identité vérifiée (SO_PEERCRED, TLS), la leçon
  des brokers (UAI-BLOCK T04-v06) et des authorization receipts (ADR 031). Un journal qui
  enregistre des noms déclarés est un roman, pas une preuve.

## Pilier C, proof engineering : les coulisses prouvables

### 8. "A label can be stripped. A receipt can't."
- **Angle** : la sortie v0.24.0 racontée comme un problème de preuve : le marquage vit dans
  l'artefact et meurt avec lui ; le log est éditable par qui le détient ; le reçu scellé
  survit. Inclure le check de couverture (chaque génération doit rencontrer un `marked`/`exempt`).
- **Sources** : ADR 030, PR #125, art. 50(2).

### 9. "Proving what your agent was never told"
- **Angle** : l'admission receipt (ADR 026), « l'agent a utilisé une info qu'on ne lui
  avait jamais donnée » devient prouvable : le moment où le hors-contexte entre dans l'état
  est scellé, avec les 4 transitions invalides de Lin et les bases de lavage refusées.
- **Sources** : ADR 026/028, le post de You-An Lin sur Futurium.

### 10. "24 mutants: every compliance check must catch its own saboteur"
- **Angle** : le test de mutation comme standard d'honnêteté du compliance-as-code :
  un check qui ne détecte pas sa propre saboteuse est du théâtre. Notre score 24/24,
  la méthode, et pourquoi un score de couverture classique ne suffit pas.
- **Sources** : normexe tools/make_mutants.py + mutation_score.py.

### 11. "The auditor's question is 'did it happen?', not 'was it allowed?'"
- **Angle** : réconciliation décision→issue (matched / late / pending / unconfirmed /
  open_gap / unauthorized / unlogged_attempt), la ADR 020 : le dénominateur ne doit
  pas mentir. Raconté comme une scène d'audit.
- **Sources** : ADR 020, reconcile.py.

### 12. "Prompt injection is a supply-chain problem now"
- **Angle** : le catalogue public d'attaques rejoué en CI contre le journal, la supply
  chain du contenu entrant, SCAR, et pourquoi un garde-fou sans preuve de passage
  ne vaut rien en audit.
- **Sources** : SCAR-BENCH, ml/ (le micro-modèle FR 293 Ko, ADR 001/002).

## Pilier D, pratiques : les SEO magnets

### 13. "The 2 December 2027 logging deadline: a 90-day engineering plan"
- **Angle** : checklist ingénieur (inventaire des événements, vocabulaire, rétention,
  intégrité, export auditeur, essai à blanc), l'article pinable que les RSSI gardent.
- **Suite naturelle** de #2, orientée exécution.

### 14. "DPIA and FRIA: one meeting, two laws"
- **Angle** : RGPD art. 35 (AIPD, déclencheurs CNIL 2018-326) vs AI Act art. 27 (FRIA,
  droits fondamentaux), qui fait quoi, quand un document sert aux deux, les différences
  que les juristes oublient de mentionner.
- **Sources** : CNIL délib. 2018-326 + art. 27 consolidé (les deux dans la KB).

---

## Règles de répartition (mémoire)

- Rythme tenable : 1 / semaine. Ordre proposé : #1 (fenêtre 6 semaines) → #8 (produit frais)
  → #2 → #5 → #3 → #6 → le reste selon l'actualité.
- Chaque article : 1 source officielle minimum, vérifiée contre le corpus versionné,
  c'est LA différenciation vs les blogs qui paraphrasent les communiqués.
- Bilingue EN+FR dès la publication (les paires existent déjà comme convention).
- Ne PAS dupliquer les 12 articles dev.to existants (angles neufs uniquement) ;
  un lien croisé discret au pire.
