---
titre: AIPD et FRIA : une réunion, deux lois
resume: Si vous déployez un système IA haut risque dans l'UE, vous devez à la fois une analyse d'impact RGPD et une évaluation d'impact droits fondamentaux AI Act. Elles se recouvrent à ~70 %, et les équipes qui les mènent séparément font le travail deux fois.
date: 2026-10-22
themes: ai-act, conformité
source: https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/dpia-fria-one-meeting.jpg
image_alt: Deux grilles d'analyse superposées en transparence sur une table de réunion, les cases communes surlignées dans la même couleur.
---

Si votre organisation déploie des systèmes IA haut risque, tri de CV, scoring
crédit, tout ce qui est en annexe III, vous êtes à cheval sur deux régimes
d'analyse : l'**analyse d'impact relative à la protection des données** du RGPD
(article 35, AIPD) et l'**évaluation d'impact sur les droits fondamentaux** de
l'AI Act (article 27, FRIA). Noms différents, bases légales différentes, et environ
70 % de contenu commun. La plupart des équipes le découvrent après avoir rédigé les
deux from scratch.

## Qui doit quoi

- **AIPD (RGPD art. 35)**, le *responsable de traitement*, avant un traitement
  susceptible d'engendrer un risque élevé. Ce n'est pas neuf : la délibération
  CNIL 2018-326 a publié les listes de déclencheurs il y a des années, et la prise
  de décision automatisée à effets légaux est un déclencheur classique depuis 2018.
  Le traitement haut risque au sens AI Act est, en pratique, toujours du territoire AIPD.
- **FRIA (AI Act art. 27)**, le *déployeur* d'un système haut risque qui est un
  organisme public ou un fournisseur de services publics, ou soumis à certaines
  règles bancaires/assurance, avant la première utilisation. Nouveau avec les dates
  d'application de l'AI Act ; ça interroge le côté *droits fondamentaux*, quels
  droits sont touchés, pour quelles catégories de personnes, quelles mesures de
  surveillance humaine, quels recours.

Notez que les sujets diffèrent : la DPO / le responsable de traitement porte l'AIPD ;
l'organisation déployante porte la FRIA. Même bâtiment, signatures différentes.

## Ce qui se recouvre (à ne faire qu'une fois)

Description du process, finalité du système, catégories de personnes affectées,
identification et gravité des risques, mesures d'atténuation, dispositifs de
surveillance humaine, validation du risque résiduel. Si votre template d'AIPD vaut
quelque chose, la FRIA peut être *assemblée* depuis lui plus une annexe spécifique
à l'article 27, pas rédigée from zero.

## Ce qui ne se recouvre PAS (les pièges)

- **Le catalogue de droits de la FRIA est plus large que la protection des
  données**, non-discrimination, accès à la justice, liberté d'expression, dignité
  humaine. Une AIPD peut conclure « pas de données perso, pas de problème » ; une
  FRIA ne le peut pas.
- **Les engagements de cadence** : nous tenons les deux à *au moins une
  réévaluation annuelle*, AIPD réexaminée quand le risque change, FRIA réévaluée
  chaque année et avant tout changement matériel. Les analyses sont des process,
  pas des PDF.
- **La preuve** : les deux analyses produisent des obligations avec dates (publier
  une liste de déclencheurs, documenter le process, garder les décisions
  revérifiables). Une analyse dont les conclusions ne peuvent pas être montrées
  comme ayant façonné le déploiement est un document d'étagère, et les deux lois
  demandent de plus en plus les reçus, pas l'étagère.

## La structure « une réunion »

Menez-les comme une seule enquête avec deux templates de rapport : la même session
d'inventaire alimente les deux, avec une table de correspondance au milieu (section
AIPD ↔ section FRIA) pour que rien ne soit doublement rédigé et que les
non-recouvrements soient visibles. Les organisations qui font ça livrent les deux
analyses dans le temps qu'il fallait pour planifier la deuxième réunion.

Et le corollaire 2027 : quand la journalisation de l'article 12 arrivera pour ces
systèmes, l'analyse dit ce qui *aurait dû* être journalisé ; le journal dit ce qui
*a été*. Les auditeurs lisent les deux, et la distance entre eux est votre vrai
score de conformité.
