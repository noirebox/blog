---
titre: 24 mutants : chaque check de conformité doit attraper son propre saboteur
resume: La couverture de tests vous dit que vos checks tournent. Elle ne vous dit pas qu'ils détectent quoi que ce soit. Le test de mutation, 24 sabotages, dont chacun doit être attrapé par exactement un check, est le standard d'honnêteté que mérite le compliance-as-code.
date: 2026-10-22
themes: preuve, conformité
source: https://github.com/noirebox/noirebox
image: https://blog.noirebox.eu/img/twenty-four-mutants.jpg
image_alt: Vingt-quatre petits personnages de saboteurs en ombre chinoise face à une rangée de serrures, chacune munie d'une alarme qui s'allume.
---

Le compliance-as-code a un sale secret : la plupart des « checks de conformité
automatisés » n'ont jamais été prouvés détecter quoi que ce soit. Ils tournent. Ils
passent. Ils produisent du vert. S'ils *échoueraient quand il le faudrait*, c'est une
question que personne ne pose, parce que le check qui passe, c'est le produit.

Il y a une vieille réponse, venue de la génétique et des tests de compilateurs : le
**test de mutation**. Sabotez la chose testée, volontairement, et exigez du filet que
chaque sabotage précis soit attrapé. Nous en faisons tourner 24 sur notre moteur de
conformité. Chaque mutant change exactement une chose, retourne un opérateur,
supprime une règle de rétention, pointe une lecture de config vers le mauvais fichier,
et l'exigence est brutale : **c'est exactement le check qui cible cette obligation qui
doit échouer.** Pas « quelque chose échoue ». Pas « la suite passe en rouge ». Le
*bon* check, pour la *bonne* raison.

## Trois choses que les mutants ont attrapées et que la couverture ne verra jamais

**La lecture du mauvais fichier.** Un mutant pointait une routine de marquage C2PA
vers une config de gouvernance dans un dossier voisin, un chemin qui *semblait*
bon. Vingt-trois checks n'ont rien vu ; celui qui comptait a dormi. Couverture :
100 %. Détection : zéro. Vrai bug, corrigé.

**Le retournement d'opérateur.** Changez `>=` en `>` dans une règle de rétention de
six mois, et aucune métrique de couverture de lignes ne frémit, la branche est
toujours exercée, juste mal. Une rétention de 180 jours qui admet 179 jours, c'est
précisément la différence entre la conformité et un manquement, et seul son saboteur
peut prouver que le check le voit.

**Le contrôle supprimé.** Retirez entièrement une obligation de journalisation et
regardez quel check s'en aperçoit. Si aucun ne bronche, vous n'avez pas écrit un
check, vous avez écrit une formule de politesse.

## Pourquoi ça compte plus en conformité qu'ailleurs

Dans le test produit, un check aveugle fait perdre du temps à quelqu'un. En
conformité, un check aveugle fabrique de la fausse assurance, le produit le plus
dangereux qui soit, parce qu'il est consommé par exactement les gens qui seront
blâmés. Les régulateurs ne demandent pas « avez-vous des checks automatisés ? » ; ils
demandent « montrez-nous une défaillance que vos checks ont attrapée ». Le test de
mutation est la répétition de cette question, à la demande, en CI.

Le score devient un chiffre public comme les comptages de tests : le nôtre est 24/24,
et il est dans le repo, rejouable par n'importe qui. La discipline se généralise :
**chaque contrôle que vous vendez ou certifiez devrait venir avec son saboteur.** Si
un fournisseur ne peut pas vous montrer la mutation que son check attrape, le résumé
honnête de son produit est : *il n'a jamais été vu en train de fonctionner.*

Les dashboards verts, c'est pas cher. Ceux qui résistent au sabotage, c'est le produit.
