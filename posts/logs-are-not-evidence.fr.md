---
titre: La capacité n'est pas l'autorité — et les logs ne sont pas des preuves
resume: Deux bons papiers ont rendu « capability ≠ authority » célèbre. Presque personne ne pose la question suivante : qu'est-ce qui fait d'un enregistrement une preuve ? Un working paper, quatre tests — accountability, auditability, scale, durability — et un scorecard honnête.
date: 2026-10-22
themes: agents, preuve
source: https://futurium.ec.europa.eu/en/apply-ai-alliance/community-content/declared-governance-demonstrable-governance-why-current-ai-governance-fails-four-tests-ssrn-working
image: https://blog.noirebox.eu/img/logs-are-not-evidence.jpg
image_alt: Un carnet de bord manuscrit raturé face à une chaîne de blocs métallique scellée, sur une table d'expertise.
---

Deux idées sont devenues virales dans le coin gouvernance-IA de 2026. *Capability Is
Not Authority* de You-An Lin : un agent qui *peut* envoyer le mail n'a pas gagné
l'autorité de l'envoyer — les outils, les documents et les succès passés ne confèrent
pas de warrant. Et un working paper qui circule sur la plateforme Futurium de l'UE,
*From Declared Governance to Demonstrable Governance*, juge les prétentions de
gouvernance sur quatre tests : **accountability, auditability, scale, durability**.

Les deux ont raison, et les deux s'arrêtent une marche avant la question
d'ingénierie :

**qu'est-ce qui transforme un enregistrement en preuve ?**

## Les logs ne sont pas des preuves

Chaque framework d'agents livre des logs. Voici la différence entre un log et une
preuve, énoncée en tests :

- **Falsifiabilité détectable** — le détenteur du log (c'est vous, l'opérateur)
  peut-il modifier discrètement l'entrée d'hier ? Si oui, c'est un journal intime,
  pas un enregistrement. Le chaînage de hash plus les signatures rendent l'édition
  *détectable*, ce qui change l'économie du mensonge.
- **Attribution** — l'enregistrement identifie-t-il qui a agi par une identité
  *vérifiée*, ou par un nom que le logiciel s'est donné ?
- **Vérification indépendante** — un tiers peut-il contrôler l'intégrité de
  l'enregistrement **hors ligne**, sans faire confiance à votre infrastructure, à
  votre uptime, à votre parole ?
- **Test adversarial** — le mécanisme a-t-il été attaqué volontairement ? Une serrure
  qui n'a jamais rencontré de crocheteur est une hypothèse.

Posez ces quatre questions sur n'importe quelle « audit trail » de votre stack — y
compris celle de la plateforme de conformité que vous avez achetée. La plupart sont
des journaux intimes.

## Les quatre tests de gouvernance, auto-scorés

Le papier de Dr. Bunic énonce sa propre barre, alors nous nous y sommes mesurés,
publiquement :

| Test | Où nous en sommes |
|---|---|
| Accountability | Decision receipts et admission receipts scellent qui a décidé, sur quelle base — attribution par signature, pas par nom déclaré |
| Auditability | Journal chaîné par hash, événements signés Ed25519, `verify` hors ligne, catalogue public d'attaques rejoué en CI |
| Scale | **Trou ouvert.** Le débit du journal à l'échelle production n'est pas banché. Le dire coûte moins cher que se faire prendre |
| Durability | **Trou ouvert.** SQLite append-only + attestations signées, mais pas d'ancrage out-of-band (TSA / pin public) encore — un hôte compromis pourrait tronquer la queue |

Deux verts, deux oranges — publiés. C'est tout l'intérêt d'une barre : on mesure, on
publie le chiffre, on ferme le trou. Une « gouvernance démontrable » qui ne montre
que ses lignes vertes, c'est de la gouvernance déclarée qui a mis une blouse de labo.
