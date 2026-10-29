---
titre: La question de l'auditeur, c'est « est-ce arrivé ? », pas « était-ce autorisé ? »
resume: La réconciliation décision→issue est la mécanique ennuyeuse qui trouve ce que les dashboards cachent : des décisions sans issue, des issues que personne n'a autorisées, des issues qui ont dépassé leur deadline, et un dénominateur qui a menti.
date: 2026-10-22
themes: preuve, conformité
source: https://github.com/noirebox/noirebox/blob/main/docs/ADRs.md
image: https://blog.noirebox.eu/img/did-it-happen-reconciliation.jpg
image_alt: Deux colonnes de registre comparées à la loupe sur un bureau d'auditeur, une ligne encerclée en rouge.
---

Chaque programme de conformité a deux dashboards : celui sur la *permission* (la
politique est-elle bonne, le gate est-il bien configuré ?) et celui sur le *fait*
(pour chaque décision, la chose promise est-elle réellement arrivée, à temps ?). Le
second, c'est là où les audits se perdent, et presque personne ne le construit.

La mécanique n'est pas glamour, la **réconciliation**. Pour chaque décision scellée
(un agent autorisé à agir, un paiement approuvé, une génération promise avec
marquage), on attend la deadline déclarée, puis on cherche l'issue correspondante
scellée. Ce qu'on trouve se range dans des états nommés, et les noms font tout
l'intérêt, parce qu'un manquement sans nom se fait argumenter :

- **matched**, décision et issue, toutes deux scellées. Ça va.
- **late**, les deux scellées, mais l'issue est arrivée après la deadline. Le
  process existe, la discipline non.
- **pending**, décision scellée, fenêtre pas encore passée. Rien à voir pour l'instant.
- **unconfirmed**, décision scellée, deadline dépassée, **aucune issue**. La promesse
  s'est évaporée. C'est l'état que les auditeurs cherchent en premier.
- **open_gap**, une décision **sans deadline du tout**. Quelqu'un a autorisé une
  action et personne n'a défini quand elle devait se compléter. Ça n'est pas un
  process ; c'est un espoir.

Et deux manquements qui demandent de regarder le registre entier, pas les lignes
une à une :

- **unauthorized**, une issue explicitement marquée `unauthorized: true`. « Jamais
  autorisée », les auditeurs cherchent le flag ; l'intérêt de le sceller, c'est
  qu'on ne peut pas le nettoyer discrètement ensuite.
- **unlogged_attempt**, une issue sans décision scellée avant elle. Là, c'est le
  dénominateur qui ment : plus d'issues que de tentatives, ça veut dire que des
  tentatives sont passées sans enregistrement. Le compte lui-même est l'alarme.

## Pourquoi « est-ce arrivé » bat « était-ce autorisé »

La conformité par permission se vérifie dans un deck de slides : voici la politique,
la config, le certificat de formation. La conformité par les faits ne se fake pas
avec des documents, parce que c'est une jointure entre deux enregistrements scellés
indépendamment, décision et issue, et la jointure produit des chiffres. Le nombre
d'unconfirmed. Le nombre d'open gaps. Le nombre de mensonges dans le dénominateur.

Ces chiffres sont aussi la différence entre le théâtre de gouvernance et la
gouvernance : n'importe quelle organisation peut énoncer une politique ; seule celle
qui fait de la réconciliation peut énoncer son **taux d'unconfirmed**. Et une fois
énoncé, il ne peut plus que descendre, en public.

La réconciliation n'est pas une invention NoireBox, c'est comme ça que les banques
closent leurs livres, et comme la comptabilité en partie double fonctionne depuis
cinq siècles. L'innovation, si innovation il y a, c'est de refuser que les décisions
des agents soient le seul coin de l'entreprise qui tourne sur de la narration
invérifiable.
