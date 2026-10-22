---
titre: Six mois de logs : l'obligation que personne n'ingénierie
resume: L'article 12 impose une journalisation automatique avec rétention de six mois sur les systèmes haut risque. Le report à décembre 2027 se lit comme une permission d'attendre. Il ne l'est pas — « automatique » a un sens technique, et un journal éditable n'est pas un journal.
date: 2026-10-22
themes: ai-act, conformité
source: https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/six-months-of-logs.jpg
image_alt: Un journal de bord scellé posé sur un clavier, face à un terminal affichant un log effaçable, éclairage de salle serveur.
---

L'article 12 de l'AI Act est l'obligation la plus « ingénierie » de tout le règlement,
et elle vient d'être reportée au **2 décembre 2027** pour les systèmes de l'annexe III.
Vu de la couverture presse, ça se lit comme une remise de peine. Ça se lit plutôt
comme un compte à rebours.

## Ce que le texte exige vraiment

Deux alinéas, deux obligations :

- **Article 12(2)** — les systèmes haut risque doivent permettre techniquement
  l'enregistrement **automatique** des événements (journaux) sur l'ensemble de la durée
  de vie du système. Pas « de la journalisation qu'on peut désactiver ». Pas « des logs
  qu'on exporte manuellement au moment de l'audit ». *Enregistrement automatique*, intégré.
- **Article 12(6)** — les déployeurs conservent les journaux **au moins six mois** par
  défaut, sauf droit contraire.

Maintenant, le mot que tout le monde survole : *automatique*. Il a un sens technique,
et il est adversarial. Si produire le journal demande qu'un humain s'en souvienne, un
cron dont quelqu'un est propriétaire, ou un export que quelqu'un lance avant l'audit —
une défaillance à n'importe laquelle de ces étapes produit du silence, et le silence
est indiscernable de la conformité. L'obligation est écrite pour que **l'absence de log
soit elle-même la preuve d'une défaillance**. C'est le design.

## Les trois questions que l'auditeur pose vraiment

Pas « avez-vous des logs ? » — tout le monde dit oui. Les questions qui finissent des carrières :

1. **Que contient un événement ?** Si vous ne pouvez pas produire un vocabulaire
   d'événements figé (quoi, sur quoi, quand, avec quelle référence), votre log est un tas
   de chaînes de caractères. Les chaînes de caractères, ça n'audite pas.
2. **Peut-il être édité ?** Un log stocké là où l'application écrit librement, c'est
   l'histoire de l'opérateur. La question technique est : qu'est-ce qui rend la
   falsification *détectable* — chaînage de hash, signatures, stockage append-only ?
3. **Prouvez six mois.** La rétention, ce n'est ni « on garde tout » (bonjour le RGPD)
   ni « on tourne à 30 jours » (bonjour le trou). Six mois, par événement, prouvable.

Et le RGPD ne se met pas en pause pendant que vous réfléchissez : ces logs sont des
données personnelles. Rétention et contrôle d'accès s'appliquent **au log lui-même**.

## À quoi sert le report

Le 2 décembre 2027, ce n'est pas « commencez ce jour-là ». C'est « soyez capables de le
prouver ce jour-là ». Un an, c'est exactement ce qu'il faut pour faire ça bien : définir
le vocabulaire d'événements, brancher l'enregistrement automatique dans les opérations
réelles du système, poser le log sur du stockage à falsification détectable, et jouer
un cycle d'audit complet en répétition.

Les équipes qui démarrent en septembre 2027 sortiront un log. Celles qui démarrent
maintenant sortiront une **preuve** — et la différence, c'est celle qui sépare une
boîte noire d'avion du journal de bord du pilote.

On construit exactement ça (append-only, chaîné par hash, signé, vérifiable hors
ligne — [noirebox](https://github.com/noirebox/noirebox), MIT), et la table des
obligations date par date est ouverte dans
[docs/COMPLIANCE-EU.md](https://github.com/noirebox/noirebox/blob/main/docs/COMPLIANCE-EU.md).
Six mois de logs, ce n'est pas un problème de stockage. C'est une architecture de l'honnêteté.
