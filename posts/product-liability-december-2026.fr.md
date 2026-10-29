---
titre: Dans six semaines, votre IA devient un produit à responsabilité stricte — et le tribunal pourra ordonner la divulgation de vos logs
resume: Pendant que tout le monde regarde les dates de décembre de l'AI Act, la nouvelle directive responsabilité produit (UE) 2024/2853 s'applique silencieusement le 9 décembre 2026 : logiciel et systèmes IA sont désormais des « produits », la responsabilité est stricte sur toute la chaîne — et les tribunaux peuvent ordonner la divulgation de vos preuves.
date: 2026-10-29
themes: ai-act, preuve
source: https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng
image: https://blog.noirebox.eu/img/product-liability-december-2026.jpg
image_alt: Un marteau de juge posé sur un clavier, à côté d'un journal scellé remis dans une pochette de procédure estampillée « disclosure ».
---

Deux dates de décembre accaparent tous les calendriers conformité IA : les transitions
Omnibus et la vague d'enforcement du **2 décembre 2026**. La date qui devrait inquiéter
davantage les équipes produit arrive **une semaine plus tard, dans un silence quasi total**.

À partir du **9 décembre 2026**, la nouvelle directive sur la responsabilité du produit
défectueux — **[directive (UE) 2024/2853](https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng)** —
s'applique aux produits mis sur le marché ou mis en service à partir de cette date. Elle
remplace un texte de 1985 écrit pour les biens physiques. La version 2026 a lu la
dernière décennie :

- **Le logiciel et les systèmes IA sont explicitement des « produits ».** Pas une
  extension par analogie — la directive les nomme. Une mise à jour de modèle défectueuse,
  un agent hallucinatoire, un outil de tri biaisé : territoire de la responsabilité stricte.
- **Toute la chaîne est sur le crochet.** Fabricant, fabricant de composants,
  importateur, prestataire de fulfillment — le plaignant choisit qui attaquer. Dans une
  stack d'agents multi-fournisseurs, la conversation responsabilité atteint tous ceux
  qui ont touché le pipeline.
- **Les dommages indemnisables incluent la perte et la corruption de données** — en plus
  du préjudice corporel et du préjudice psychologique reconnu. Oui : l'intégrité de vos
  enregistrements est elle-même un intérêt indemnisable.

## Le passage que personne ne lit à voix haute

Le défaut, c'est une chose ; le prouver, c'en est une autre — et ici la directive fait
quelque chose d'inhabituel pour des plaignants confrontés à des systèmes opaques :
**les tribunaux peuvent ordonner à la partie détentrice des preuves de les divulguer**,
et quand la divulgation est refusée ou incomplète, la charge de la preuve bascule par
présomption vers le défendeur.

Relisez deux fois, parce que ça réécrit ce que vos logs *sont*.

Jusqu'ici, « on garde des logs internes » était une ligne de coûts. À partir du
9 décembre, dans un litige de responsabilité produit sur un système IA, le log est
**le corpus de discovery**. Le tribunal ne demande pas si vous teniez des
enregistrements ; il peut vous obliger à produire ce que vous avez — et si ce que vous
avez est éditable, rétrospectif ou commodément incomplet, *l'absence d'intégrité devient
l'argument d'en face*. L'allègement de la charge du preuve vise précisément les systèmes
dont le fonctionnement interne est difficile à sonder : votre opacité, c'est leur
présomption.

## Là où ça rejoint le journal

C'est la boucle qui se referme sur tout ce que ce blog défend. Une ordonnance de
divulgation fait de l'intégrité de vos enregistrements une **propriété contentieuse** :

- Un journal chaîné par hash, append-only et signé se remet **avec la preuve de sa
  propre intégrité** — le destinataire vérifie la chaîne au lieu de faire confiance à
  votre parole.
- Un log éditable remis de la même façon est un multiplicateur de responsabilité :
  quoi qu'il dise, l'expert d'en face établira qu'il aurait pu dire n'importe quoi.
- Et la couche de réconciliation — décisions jointes aux issues, avec états nommés —
  transforme « que s'est-il passé réellement » d'une narration en une requête. Dans un
  régime de responsabilité stricte, la partie qui a la narration cohérente gagne la salle.

La directive de 1985 demandait aux fabricants de tenir des registres ; personne ne se
souciait beaucoup de leur forme. Celle de 2026 fait de *la qualité de vos preuves* une
partie de votre position juridique.

## Quoi faire dans les six semaines

1. **Inventoriez ce que vos systèmes IA décident et font** — cet inventaire est votre
   futur corpus de disclosure. Si une classe de décision n'est pas enregistrée, vous
   divulguerez son absence.
2. **Commencez à sceller décisions et issues maintenant**, avec les horodatages qui
   comptent (la fenêtre de claims de la directive court une décennie après la mise sur
   le marché — vos logs doivent survivre à votre souvenir du produit).
3. **Traitez l'intégrité du log comme une exigence légale, pas un confort d'ops** :
   append-only, chaîné, signé, vérifiable par un tiers qui n'était pas dans la pièce.

L'AI Act vous dit quoi journaliser. La directive responsabilité produit décide ce que
vos logs valent au tribunal. L'une régule la machine ; l'autre chiffre ses défaillances.
Construisez pour les deux, et décembre cesse d'être effrayant.
