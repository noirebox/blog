---
titre: Prouver ce que votre agent n'avait jamais été censé savoir
resume: « L'agent a utilisé une information qu'on ne lui avait jamais donnée », jusqu'ici, cette accusation était inprouvable dans les deux sens. Les reçus d'admission scellent le moment où le hors-contexte entre dans l'état d'un agent, avec les quatre promotions invalides et le vocabulaire de lavage refusé au scellement.
date: 2026-10-22
themes: agents, preuve
source: https://github.com/noirebox/noirebox/blob/main/docs/ADRs.md
image: https://blog.noirebox.eu/img/proving-what-agent-was-never-told.jpg
image_alt: Une enveloppe scellée glissée par une fente dans une chambre forte, alors qu'un flux de documents passe à côté sans y entrer.
---

Le litige le plus dur de l'audit des agents a deux versions. Celle de l'accusateur :
*« l'agent a recommandé les chiffres confidentiels de notre client, il a forcément lu
la data room privée. »* Celle de l'opérateur : *« il n'a jamais vu ces données ; il a
inféré depuis les dépôts publics. »* Jusqu'à récemment, les deux étaient des positions
de foi. Personne ne pouvait prouver ce qu'un agent avait ou n'avait pas pris dans son
état.

C'est le problème qu'attaquent les reçus d'admission, pas ce que l'agent a *fait*,
mais l'événement antérieur et silencieux : **le moment où quelque chose d'extérieur à
son contexte y a été admis.**

## Le reçu porte sur la promotion, pas sur l'acte

Le cadre de You-An Lin fournit le vocabulaire : la capacité n'est pas l'autorité, et
le mouvement dangereux est la *promotion*, quand la simple présence, pertinence ou
plausibilité d'une information est promue silencieusement en « l'agent peut l'utiliser ».
Un reçu d'admission scelle cette promotion comme événement signé à part entière :

- **qui** l'a admise, **de où**, et sur **quelle surface** elle est arrivée ;
- **quelle transition**, une des quatre promotions invalides, nommée :
  *visibility→admission, capability→move, relevance→payload, style→stance* ;
- la **base** : le warrant indépendant, une instruction utilisateur, un reçu
  antérieur, un octroi de périmètre explicite ;
- la **décision**, fail-closed : `admitted | denied | admission_undecidable |
  admission_check_not_run`. L'indécidable n'est jamais propre, et un check qui n'a
  pas tourné est enregistré comme sauté, jamais passé en silence.

Puis le refus qui donne ses dents au reçu : quatre choses ne sont **jamais une base**
la *présence*, la *pertinence*, la *plausibilité*, l'*utilité* du matériau. « C'était
dans le thread », « ça semblait pertinent », « ça paraissait plausible », « ça allait
aider l'utilisateur », c'est le vocabulaire de lavage, et le sceau le rejette en le
nommant. Le champ qui existe pour porter un warrant indépendant refuse de porter la
chose pour refuser laquelle il existe.

## Pourquoi les accusateurs y gagnent aussi

Ce n'est pas un bouclier d'opérateur ; ça coupe dans les deux sens. Quand les
admissions sont scellées, l'accusation « il a lu la data room » devient vérifiable :
rejouez la séquence scellée. Soit il y a un reçu d'admission avec une base légitime,
l'opérateur le montre, soit il n'y en a pas, la théorie de l'accusateur perd son
mécanisme. **Accusations fausses et accusations vraies deviennent décidables.** C'est
ce que « falsifiable détectable » achète : pas une protection contre l'audit, mais la
fin des audits infalsifiables.

Associé aux decision receipts, qui scellent la distribution de probabilités complète
produite par le moteur du modèle sur ses réponses permises, plus le doute exprimé par
le moteur lui-même, liés à une spécification de questionnaire scellée, vous pouvez
réconcilier après coup si la décision pouvait être prise sans le matériau admis. La
réconciliation a des manquements nommés, et un d'entre eux a exactement cette forme.

« Prouvable, pas supposé », c'est la thèse produit entière en quatre mots. Le reçu
d'admission, c'est là où ça compte le plus, parce que l'admission, c'est le moment où
un agent cesse d'être un outil et commence à être un témoin.
