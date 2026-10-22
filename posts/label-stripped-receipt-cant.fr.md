---
titre: Une étiquette s'arrache. Un reçu ne s'arrache pas.
resume: L'article 50(2) veut un marquage lisible par machine sur les contenus générés. Tous les SDK de marquage qui sortent cet hiver ont le même angle mort : l'étiquette vit dans l'artefact et meurt avec lui. La preuve que vous avez marqué une sortie doit vivre ailleurs.
date: 2026-10-22
themes: preuve, ai-act
source: https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/label-stripped-receipt-cant.jpg
image_alt: Une image générée par IA dont le filigrane se détache comme un autocollant, à côté d'un reçu scellé à cachet de cire rouge intact.
---

L'article 50(2) de l'AI Act impose aux fournisseurs de systèmes génératifs de marquer
les contenus synthétiques de façon **lisible par machine** — et depuis l'Omnibus, les
systèmes génératifs déjà sur le marché avant le 2 août 2026 ont jusqu'au
**2 décembre 2026** pour se mettre en conformité. Une vague de SDK de marquage sort
pour cette date. Tous partagent le même angle mort, et presque personne ne le nomme :

**l'étiquette vit dans l'artefact — et meurt avec lui.**

Retirez le filigrane, ré-encodez l'image, rognez l'en-tête, faites passer le texte
dans un paraphraseur : le marquage a disparu, et une étiquette arrachée est
indiscernable d'une étiquette qui n'a jamais existé. Pendant ce temps, « l'evidence
log » que les SDK proposent est la base de données de l'opérateur — modifiable par
qui la détient. Vous avez marqué vos sorties ; la *preuve que vous l'avez fait* est
à un `UPDATE` près.

## Le reçu, c'est ce qui survit

C'est exactement le trou que les reçus de marquage de notre v0.24.0 ferment. Le reçu
est un événement signé dans un journal append-only chaîné par hash, lié à :

- le **sha256 de la sortie telle que livrée** — le digest, jamais le contenu, donc
  aucune donnée perso ni propriétaire ne fuite dans le journal ;
- sa **modalité** (texte, image, audio, vidéo — les quatre de l'article 50(2)) ;
- les **méthodes appliquées** — ensemble fermé, et si vous avez utilisé un manifeste
  C2PA, le digest du manifeste est lié *dans les deux sens* ;
- un **statut fail-closed** : `marked | not_marked | exempt` — et une exemption doit
  nommer laquelle des carve-outs de l'article 50 elle invoque. Un « exempt » nu est
  refusé au scellement.

Et la partie qui transforme des enregistrements en audit : **la couverture**. Chaque
événement de génération portant un digest de sortie doit rencontrer un reçu
`marked` ou `exempt` pour ce digest. Un reçu `not_marked` *est* le trou, scellé —
et un marquage ultérieur ne l'efface pas. L'auditeur ne demande pas « marquez-vous
vos sorties ? » ; il demande « montrez-moi une génération sans reçu correspondant ».
Soit vous avez une réponse scellée, soit vous avez un manquement.

## Pourquoi ça compte plus que la deadline

La transition du 2 décembre 2026 concerne les systèmes déjà sur le marché. Le SDK
que vous livrerez gérera l'étiquette. Ce qu'il ne gérera pas, c'est le jour où un
client, un régulateur ou un tribunal demande : *prouvez que cette sortie précise a
été marquée, au moment de la génération, selon les règles que vous revendiquez.*

Un filigrane répond « est-ce que c'est marqué ? » — jusqu'à ce qu'on l'arrache. Un
reçu répond « l'avez-vous marqué ? » — pour toujours, vérifiable hors ligne par
quelqu'un qui ne vous fait pas confiance.

C'est la différence entre se conformer et pouvoir prouver qu'on s'est conformé. Une
seule des deux survit à un audit.

*Le reçu de marquage est réel, livré et testé : [noirebox v0.24.0](https://github.com/noirebox/noirebox) (MIT), avec le check de couverture et le pont C2PA — l'acte de se conformer n'est pas une édition média, donc nos sceaux parlent le namespace Content Credentials, pas l'inverse.*
