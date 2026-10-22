---
titre: L'échéance du 2 décembre 2027 : un plan d'ingénierie de 90 jours
resume: Les équipes annexe III ont un an pour implémenter l'article 12 — journalisation automatique, rétention de six mois, falsifiabilité détectable. Voici le plan qui tient en un trimestre, pour que l'échéance devienne une formalité au lieu d'un exercice d'urgence.
date: 2026-10-22
themes: ai-act, conformité
source: https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/logging-90-day-plan.jpg
image_alt: Un planning de 90 jours épinglé au mur d'une salle d'ingénierie, trois colonnes de post-its verticales, une échéance surlignée au stabilo jaune.
---

L'article 12 — journalisation automatique des événements sur toute la durée de vie,
avec six mois de rétention pour les déployeurs — mord désormais au **2 décembre 2027**
pour les systèmes haut risque de l'annexe III. Un an, ça semble beaucoup. Ça ne l'est
pas, pour une raison : la journalisation n'est pas une fonctionnalité. C'est un
contrat entre votre système et chaque audit futur, et les contrats ont besoin de
temps de conception.

La bonne nouvelle : l'ingénierie tient dans **90 jours**. Voici le trimestre, en
trois mouvements.

## Jours 1–30 : définir le contrat d'événements

L'obligation dit « enregistrement automatique des événements » — le règlement ne
définit délibérément pas votre vocabulaire ; c'est votre travail, et c'est là que se
cache l'essentiel de la valeur.

- **Inventoriez les événements qui comptent** : entrées, sorties, références aux
  données sources (pour l'objectif de traçabilité de l'article 12(1)), interventions
  humaines, overrides, erreurs — et, si vous prenez l'article 26 au sérieux, les
  moments où la surveillance humaine a réellement eu lieu.
- **Figez le schéma** : un type d'événement = des champs fixes. Les chaînes libres,
  ça n'audite pas ; les champs typés, si.
- **Horodatage** : UTC uniquement, précision fixe, généré à la source. Un log d'audit
  qui mélange heures locales et changement d'heure est inutilisable, et les auditeurs
  vérifient.
- **Décidez ce que le log ne contiendra PAS** : les logs de l'article 12 sont des
  données personnelles au sens du RGPD. Digests et références plutôt que contenu brut :
  c'est le pattern qui garde les deux lois contentes.

## Jours 31–60 : rendez-le automatique et infalsifiable

C'est là que « automatique » (le mot réel de l'article 12(2)) devient de
l'architecture :

- **Émettez à la source** — la journalisation dans le chemin de la requête, pas un
  export nocturne. Si un humain doit s'en souvenir, ce n'est pas du grade article 12.
- **Stockage append-only** — le log ne doit pas être inscriptible par l'application
  qui le produit. SQLite en append-only, un store WORM, ou un journal chaîné par
  hash : l'exigence, c'est que suppression et édition soient *détectables*, pas
  seulement interdites par la politique.
- **Chaînez et signez** — chaque entrée porte le hash de la précédente ; les lots sont
  signés. L'enregistrement d'hier ne peut plus être discrètement amélioré.
- **Mécanique de rétention** — six mois, ça veut dire une politique de rétention *et*
  une preuve de rétention : le test, c'est « montrez-moi les événements de mars »,
  pas « on garde tout ».

## Jours 61–90 : répétez l'audit

- **Faites tourner la requête que l'auditeur fera** : « toutes les actions sur cette
  décision, tous les overrides du trimestre, preuve de rétention six mois pour cette
  fenêtre. » Si y répondre demande une semaine d'ingénierie, vous n'avez pas un log —
  vous avez de l'archéologie.
- **Attaquez votre propre log** — tentez d'éditer une entrée sans détection. Si vous
  y arrivez, la falsifiabilité est décorative.
- **Écrivez la one-pager** : où vivent les logs, combien de temps, qui y accède, comment
  l'intégrité se vérifie. Le document que les auditeurs lisent en premier.

## Le piège

Chaque jour de ce plan reporté à 2027 coûte plus cher qu'aujourd'hui : requalifier la
journalisation dans un système haut risque en production, pendant qu'il affronte son
premier cycle d'enforcement, c'est l'ingénierie la plus chère qui soit. Quatre-vingt-dix
jours maintenant vous achètent la seule position qui compte à une échéance : **l'ennui**.
