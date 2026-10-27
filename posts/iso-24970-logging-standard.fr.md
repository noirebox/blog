---
titre: Le standard de logging vient de trouver sa forme : EN ISO/IEC 24970 est en projet final
resume: Le standard harmonisé pour la tenue de registres de l'article 12 — journalisation des systèmes IA, avec modèle d'information et exigences d'intégrité — est passé en projet final (FprEN) en route vers EN ISO/IEC 24970:2026. Ce que ça change pour votre échéance du 2 décembre 2027, et le trou honnête qu'on vous doit.
date: 2026-10-23
themes: ai-act, conformité
source: https://www.iso.org/standard/88723.html
image: https://blog.noirebox.eu/img/iso-24970-logging-standard.jpg
image_alt: La couverture d'un standard ISO/IEC 24970 en cours d'impression, posée sur un registre chaîné et cadenassé, avec un calendrier décembre 2027 en arrière-plan.
---

Depuis un an, chaque guide honnête sur l'article 12 de l'AI Act se terminait pareil :
*le règlement exige la journalisation automatique des événements, mais ne définit pas
votre vocabulaire d'événements — les standards harmonisés sont encore à venir.* Cette
astérisque vient de rétrécir. **EN ISO/IEC 24970 — *Artificial intelligence — AI system
logging* — a atteint son stade de projet final (FprEN/FDIS)** en route vers la
publication sous la référence EN ISO/IEC 24970:2026, et c'est le candidat **norme
harmonisée pour les obligations de tenue de registres de l'article 12** au CEN-CENELEC.

## Pourquoi « harmonisée » est le mot qui compte

N'importe qui peut écrire un standard de logging. Un standard *harmonisé*, c'est
différent : s'appuyer sur lui donne la **présomption de conformité** avec l'obligation
qu'il soutient. Ça transforme la conversation sur l'article 12, de « prouvez que votre
journalisation est adéquate » — un argument — en « nous avons implémenté EN ISO/IEC
24970 » — une référence. Pour les équipes qui affrontent le 2 décembre 2027 sur les
systèmes annexe III, c'est la différence entre défendre une conception et citer une norme.

## Ce qu'il contient (au registre public)

Le périmètre, selon la fiche ISO elle-même : **capacités communes, exigences, et un
modèle d'information pour la journalisation des événements dans les systèmes IA**,
au service de la transparence et de l'accountability, conçu pour se brancher sur votre
démarche de management du risque (ISO/IEC 42001, ISO/IEC 23894). Les analystes qui
suivent le projet relient sa couverture aux points de douleur de l'article 12 :
**quels événements journaliser, comment, la rétention, et l'intégrité/l'immutabilité
des enregistrements**. Autrement dit : la question du vocabulaire d'événements qu'on
vous disait « à vous de répondre » reçoit sa réponse — sous forme de modèle
d'information formel.

## Trois conséquences pour votre plan de logging

**1. N'inventez pas un format privé maintenant.** Si votre plan 90 jours (on en a
publié un) commence par « figez le schéma », ancrez la forme de ce schéma sur le modèle
d'information du 24970 — même depuis le draft. Un format d'événements maison antérieur
au standard harmonisé, c'est un projet de migration en 2027.

**2. L'intégrité passe de bonne pratique à exigence citable.** Les enregistrements
chaînés par hash, append-only, à falsification détectable — ce que ce blog répète
depuis des mois — c'est exactement ce que veut dire « intégrité/immutabilité » dans un
standard de logging, côté opérationnel. Le standard légitime l'architecture ; il ne la
change pas.

**3. La présomption marche vers l'avant, pas vers l'arrière.** La conformité des
systèmes annexe III mord au 2 décembre 2027 ; la publication du standard plus sa
citation sera le chemin le plus lisse *à* cette date. Les retardataires qui auront
construit leur logging en 2027 le requalifieront vers le modèle d'information sous
pression — l'archéologie la plus chère qui soit.

## La partie honnête

Nous n'avons pas audité notre propre journal contre le texte final — parce que le
texte final n'est pas public. Ce qu'on peut dire : un vocabulaire d'événements typé, du
chaînage de hash, des événements signés — c'est exactement l'espèce d'exigences que le
draft est rapporté contenir, et c'est pour ça qu'on les a construites avant qu'il y ait
un numéro à citer. **Quand EN ISO/IEC 24970:2026 publiera, on fera ça proprement : une
table de correspondance publique, ligne par ligne, entre les exigences du standard et
le comportement du journal** — y compris les lignes où l'on n'est pas encore conforme.

C'est la suite à surveiller. Le standard a trouvé sa forme ; la deadline, elle, n'a pas
bougé. Les équipes qui le lisent maintenant le citeront en 2027. Celles qui attendent
reconstruiront leurs logs pour s'y conformer.

C'est le troisième volet de notre série logging — avec [les six mois de logs que
personne n'ingénierie](https://blog.noirebox.eu/fr/six-months-of-logs) et [le plan
90 jours](https://blog.noirebox.eu/fr/logging-90-day-plan).
