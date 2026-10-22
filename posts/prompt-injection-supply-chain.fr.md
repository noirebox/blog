---
titre: La prompt injection est devenue un problème de supply chain
resume: Vos agents consomment des pages web, des tickets et des mails écrits par des inconnus. La prompt injection est donc une vulnérabilité de dépendance — et comme tout risque supply chain, ça se gère avec des catalogues d'attaques rejoués et des preuves, pas avec de l'espoir.
date: 2026-10-22
themes: agents, sécurité
source: https://github.com/noirebox/noirebox
image: https://blog.noirebox.eu/img/prompt-injection-supply-chain.jpg
image_alt: Une chaîne d'approvisionnement stylisée dont un maillon est un e-mail hostile, tenant en otage les maillons suivants, style schéma d'audit.
---

Personne ne demande si votre framework web « résiste » aux requêtes HTTP malveillantes
par espoir ; vous faites tourner un WAF, vous patchez des CVE, vous auditez vos
dépendances. La prompt injection mérite le même traitement ennuyeux, parce que
l'exposition a la même forme : **vos agents consomment du contenu écrit par des
inconnus** — pages, tickets, mails, PDF — et n'importe lequel peut porter des
instructions destinées à l'agent plutôt qu'au lecteur.

Le prendre au sérieux, c'est emprunter le playbook supply chain :

## 1. Le catalogue d'attaques est un actif, pas une anecdote

« On a testé contre quelques injections célèbres », c'est l'équivalent sécurité de
« on met à jour nos dépendances de temps en temps ». La forme qui marche, c'est un
**catalogue versionné de fixtures d'attaque** — chacune un pattern d'injection réel
avec son résultat attendu — rejoué **en CI** à chaque changement, comme les tests de
régression CVE. Quand une nouvelle technique est publiée, elle devient une fixture ;
à partir de là, chaque build prouve qu'elle reste battue. Le catalogue croît de façon
monotone ; les défenses ne peuvent pas pourrir en silence.

## 2. Des étages, parce que le coût suit chaque requête

Scanner chaque transcript avec un gros modèle, c'est le « réécris-le en Rust » des
garde-fous : vrai et intenable. L'architecture qui marche est étagée, du moins cher
en premier : la **regex** pour l'évident (déterministe, testable, gratuit), un
**petit modèle local** (le nôtre en français fait 293 Ko — assez petit pour tourner
partout, entraîné sur un corpus français versionné) pour les paraphrases, et un
**juge LLM** uniquement pour le résidu ambigu. Le format est unifié entre étages —
positions et catégorie — donc l'étage est un détail d'implémentation, pas un changement
de schéma.

## 3. Le garde-fou a besoin de preuves, lui aussi

Voilà ce qui transforme la sécurité en conformité : un garde-fou qui a bloqué une
attaque, c'est une belle histoire ; un garde-fou dont le blocage est **un événement
scellé et signé** — pattern, positions, catégorie, horodatage — c'est un fait
d'audit. Et son complément compte tout autant : chaque transcript admis doit être
scellé aussi, pour que la question finale « le garde-fou a-t-il vu cette entrée ? »
ait une réponse de journal plutôt qu'un haussement d'épaules.

Pourquoi les deux côtés ? Parce que les incidents sont des disputes. Le client dit
que l'agent a fui ; vous dites que le garde-fou a tenu. Deux flux d'événements
scellés — blocages et admissions — transforment la dispute en requête.

## 4. Oui, on a rejeté le modèle du grand éditeur — avec des mesures

Le raccourci tentant, c'est un classifieur d'injection open-weights célèbre. On en a
évalué un, le standard de l'industrie, et on l'a rejeté sur des critères mesurés :
entraîné en anglais alors que nos transcripts sont en français ; sortie binaire là où
un audit veut des catégories et des positions ; licence gated là où un produit veut un
artefact sans friction. L'évaluation est écrite dans un ADR, et c'est ça le vrai
sujet — **les rejets avec raisons sont une mémoire institutionnelle ; les vibes, du
churn.**

La prompt injection ne sera pas « résolue ». Elle sera *gérée* — cataloguée, rejouée,
étagée et prouvée — exactement comme tous les risques supply chain avant elle. Les
équipes qui commencent à garder les preuves maintenant seront celles qui auront des
réponses quand le premier incident sérieux tombera dans une juridiction de quelqu'un.
