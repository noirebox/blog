---
titre: Fournisseurs GPAI : les échéances du Code de conduite qui sont déjà passées
resume: Le Code de conduite GPAI n'est pas la loi, mais c'est la grille avec laquelle la Commission lit votre conformité aux articles 53-55. Permissions crawler, préavis aval de 14 jours, signalement d'incidents en jours, documentation du modèle tous les six mois. La plupart des fournisseurs en ratent au moins deux.
date: 2026-10-22
themes: ai-act, conformité
source: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai-ai-act
image: https://blog.noirebox.eu/img/gpai-code-deadlines.jpg
image_alt: Un cahier des dates d'échéance barrées (robots.txt, 14 jours, 6 mois, 2/5/10/15 jours) posé sur un rack serveur, tampon Commission européenne.
---

Les fournisseurs d'IA à usage général vivent sous les obligations des articles 53-55
depuis le **2 août 2025**, intouchées par le report de l'Omnibus, qui n'a déplacé que
les dates haut risque. Et la référence pratique pour « comment je montre que je suis
conforme ? », c'est le **Code de conduite GPAI**. Distinction importante, souvent
gommée : le Code n'est pas la loi. Mais c'est le cadre que la Commission reconnaît,
et s'en écarter veut dire se justifier avec des preuves équivalentes. Voici les quatre
échéances qui sont le plus souvent ratées.

## 1. Permissions crawler, l'engagement robots.txt

Le Code engage les signataires à respecter les permissions crawler de type robots.txt
pour leurs crawlers d'entraînement. C'est la seule obligation dont la conformité est
**vérifiable de l'extérieur en quelques minutes** : pointez n'importe quel auditeur de
crawler sur vos user-agents et regardez s'ils honorent les règles de disallow. Si
votre pipeline de données est plus vieux que votre équipe conformité, c'est l'endroit
où personne n'a jamais regardé.

## 2. Information aval, le préavis de 14 jours

Quand quelque chose de matériel change (documentation, capacités, mises à jour
sécurité), les fournisseurs aval qui intègrent votre modèle ont un engagement de
préavis de **14 jours**. En pratique, ça veut dire que votre process de release a
besoin d'une étape de notification *avant* que les poids ou l'API changent, pas un
changelog après. Les équipes qui livrent chaque semaine découvrent cette exigence
par la manière forte.

## 3. Signalement d'incidents, 2, 5, 10, 15 jours selon la gravité

La timeline d'incidents du Code est graduée par gravité : environ **2 jours** pour les
incidents les plus critiques, puis 5, 10 et 15 jours en descendant l'échelle.
Comparez avec ce que la plupart des fournisseurs ont, un alias mail dont personne
n'est propriétaire. L'obligation n'est pas la partie dure ; c'est d'avoir quelqu'un
qui répond de l'horloge.

## 4. Documentation du modèle, rafraîchie tous les six mois

Le Model Documentation Form n'est pas un dépôt unique. L'engagement est de le garder
**à jour sur un cycle de six mois**. Mettez la récurrence au calendrier aujourd'hui ;
les fournisseurs qui échoueront sur cette ligne sont ceux pour qui le Formulaire était
un artefact du jour de lancement qui décrit désormais un modèle qui n'existe plus.

## Le pattern derrière les quatre

Aucune de ces lignes n'est un problème de recherche. Ce sont des **obligations de
process avec des horloges**, et les horloges, c'est ce qui tue la conformité de
papier. La question d'ingénierie intéressante est celle qu'on se repose sans cesse sur
ce blog : quand vous affirmez avoir signalé en 2 jours ou notifié en 14, *qu'est-ce
qui le rend prouvable après coup ?* Un mail dans votre dossier envoyé, c'est votre
parole. Un événement horodaté et scellé dans un journal que ni vous ni nous ne
pouvons réécrire discrètement, c'est une preuve.

Le Code est volontaire. Être crédible ne l'est pas.
