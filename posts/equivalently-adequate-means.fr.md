---
titre: Vous n'avez pas signé le Code de conduite marquage ? La Commission a un seul mot pour vous : prouvez-le
resume: La Commission vient de publier ses lignes directrices sur l'article 50 et un Code de conduite sur le marquage — avec une fourchette cachée dans une phrase. Signez le Code, ou démontrez des « moyens alternatifs également adéquats ». Personne ne définit ce que ça veut dire. Voici la lecture ingénieur.
date: 2026-10-23
themes: ai-act, preuve
source: https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations
image: https://blog.noirebox.eu/img/equivalently-adequate-means.jpg
image_alt: Une fourche stylisée à deux chemins — d'un côté un cahier de charges signé par plusieurs mains, de l'autre un reçu scellé à cachet de cire avec une loupe d'auditeur — sous un panneau « Article 50 » aux étoiles européennes.
---

Deux publications discrètes viennent de redessiner le paysage du marquage pour quiconque
livre de l'IA générative dans l'UE : les **[lignes directrices de la Commission sur les
obligations de transparence de l'article 50](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)**
(façonnées par une consultation publique sur le marquage), accompagnées d'un **Code de
conduite sur la transparence des contenus générés par IA**. L'article 50 s'applique
depuis le 2 août 2026, et la transition pour les systèmes déjà sur le marché se ferme
le **2 décembre 2026** — dans quelques semaines.

Enterrée dans les lignes directrices, une phrase qui compte plus que tout le reste du
document réuni. Les fournisseurs et déployeurs d'IA générative qui ne signent pas le
Code de conduite :

> « devront démontrer la conformité avec les obligations de marquage et d'étiquetage
> des contenus générés par IA par des **moyens alternatifs également adéquats**. »

Relisez. La Commission a tracé une fourchette : **signez le Code et héritez de son
port sécuritaire, ou restez dehors et *démontrez* que ce que vous faites à la place est
équivalent.** Ce qu'elle n'a pas fait — délibérément — c'est définir ce que « démontrer »
veut dire. Aucun format épinglé, aucun chemin de certification, des standards encore en
cours. La liberté des moyens vient avec la pleine charge de la preuve.

## « Également adéquat » est une spécification d'ingénierie déguisée

Adequate par rapport à quoi ? À la barre que le Code fixe à ses propres signataires.
Le travail du non-signataire est donc de démontrer, sur son propre régime de marquage,
les quatre choses que tout auditeur va sonder :

**1. Le marquage survit aux transformations raisonnables.** Un filigrane qui meurt au
ré-encodage, au recadrage ou à la capture d'écran ne démontre rien — la barre du Code
est la détection après manipulation réelle, et « également adéquat » veut dire atteindre
cette même barre, pas la déclarer.

**2. Chaque génération est prouvée.** Pas « nous marquons nos sorties » — *cette* sortie,
liée à son digest, horodatée, scellée au moment de la génération. L'affirmation vit par
artefact, pas par page de politique.

**3. La couverture est prouvable.** La démonstration qui tue : *montrez-moi une
génération sans preuve correspondante.* Si vos preuves sont dans un log que votre propre
application peut éditer, l'auditeur est en train de lire votre journal intime. Si c'est
un enregistrement append-only chaîné par hash et signé, où une génération sans son reçu
est un manquement nommé et scellé — la question se répond toute seule.

**4. Un tiers peut vérifier hors ligne.** L'équivalence avec un Code que tout le monde
peut lire veut dire que votre preuve doit être vérifiable par quelqu'un qui ne fait pas
confiance à votre infrastructure, à votre uptime, ni à votre volonté de livrer vos logs.

Ce n'est pas une note juridique. C'est une spécification système — et c'est exactement
la forme des reçus de marquage que nous avons livrés dans
[noirebox v0.24.0](https://github.com/noirebox/noirebox) : sha256 de la sortie telle que
livrée (jamais le contenu), modalité fermée sur les quatre de l'article 50(2), méthodes
en ensemble fermé avec le digest du manifeste C2PA lié dans les deux sens, statut
fail-closed (`marked | not_marked | exempt` — une exemption doit nommer son carve-out),
et une jointure de couverture où un reçu `not_marked` *est* le trou scellé, qu'un
marquage ultérieur n'efface pas.

## L'autre chose que les lignes directrices ont réglée — et laissée ouverte

Deux détails à noter. Les lignes directrices confirment les obligations côté déployeur
qu'on oublie : divulgation des deepfakes, information des personnes exposées à la
reconnaissance d'émotions et à la catégorisation biométrique, et les textes IA sur des
sujets d'intérêt public sans contrôle éditorial humain. Et elles donnent le contour des
exemptions — « l'édition standard » est traitée comme hors champ. Mais sur le *comment*
du marquage, la Commission s'est tue à dessein : les formats et les tests de robustesse
appartiennent à la normalisation future. Ce qui veut dire que la fenêtre pour définir à
quoi ressemble une « démonstration adéquate » est **ouverte maintenant** — et les
premières organisations qui publient des régimes de preuve crédibles et vérifiables
écrivent le standard de facto pour tous ceux qui sont derrière.

## L'horloge

Six semaines avant la fermeture de la transition du 2 décembre 2026. La fourchette
coûte dans les deux cas : signer veut dire adopter les pratiques du Code ; ne pas
signer veut dire construire la démonstration. Les deux prennent plus de temps que la
deadline ne le suggère. Mais une seule vous laisse entre les mains quelque chose que
vous pouvez tendre à n'importe quel auditeur, dans n'importe quelle juridiction, pour
toujours — quel que soit ce que dira la prochaine révision du Code.

On avait écrit sur le piège de fond — [une étiquette s'arrache, un reçu ne s'arrache
pas](https://blog.noirebox.eu/fr/label-stripped-receipt-cant) — et sur [les devoirs
côté chatbot que les équipes oublient](https://blog.noirebox.eu/fr/chatbot-art50-production).
Les lignes directrices viennent de transformer ce piège en politique officielle :
pour quiconque est hors du Code, la conformité par déclaration est terminée. La preuve
est le chemin qui reste.
