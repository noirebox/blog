---
titre: Votre chatbot doit dire qu'il est un chatbot : l'article 50, testé en production
resume: Les obligations de transparence pour les interactions IA, les contenus synthétiques et les deepfakes s'appliquent depuis août 2026, et la transition pour les systèmes déjà sur le marché se ferme le 2 décembre 2026. Ce que « marquage lisible par machine » veut dire quand quelqu'un fait une capture d'écran.
date: 2026-10-22
themes: ai-act, agents
source: https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689
image: https://blog.noirebox.eu/img/chatbot-art50-production.jpg
image_alt: Une conversation de chatbot affichée sur mobile avec un badge « IA » visible, à côté d'un même contenu dont le badge a disparu après recadrage.
---

L'article 50, c'est la partie de l'AI Act que vos utilisateurs voient, et elle
s'applique depuis le **2 août 2026**. Les systèmes génératifs déjà sur le marché ont eu
une transition étroite, jusqu'au **2 décembre 2026**, et elle se ferme. Voici ce que
l'article exige vraiment, découpé en quatre choses qu'on confond :

1. **On interagit avec une IA ? Le dire** (art. 50(1)). Si une personne interagit avec
   un système IA, le système doit se faire connaître, sauf si c'est évident pour une
   personne raisonnable. Votre chatbot support au prénom humain sans mention : c'est
   le cas d'école.
2. **Le contenu synthétique doit être marqué, lisiblement par machine** (art. 50(2)).
   Texte, image, audio, vidéo, le fournisseur marque les contenus générés dans un
   format détectable par les machines, et divulgue le caractère artificiel à qui le voit.
3. **Les personnes exposées à de la reconnaissance d'émotions ou de catégorisation
   biométrique doivent être informées** (art. 50(3)), les personnes exposées, pas
   seulement l'opérateur.
4. **Les deepfakes doivent être divulgués** (art. 50(4)), les images, sons et vidéos
   artificiels « générés ou manipulés par IA » portent une obligation de divulgation.

## Le test qui compte

La divulgation, c'est facile en démo et facile à perdre. Le mode de défaillance n'est
pas « on n'a jamais marqué », c'est **le marquage qui ne survit pas au contact du
vrai internet** : une capture d'écran ne retire rien, mais un recadrage, une
recompression, un copier-coller de texte, un réencodage par une plateforme, chaque
transformation est une chance que la couche lisible par machine meure pendant que le
contenu continue sa vie.

La question à l'ingénierie n'est donc pas « est-ce qu'on appelle le SDK de marquage ? »
mais : **le marquage survit-il aux transformations raisonnables, et peut-on le prouver ?**
Deux checks que nous faisons tourner :

- **Survie aux transformations**, ré-encodage de l'image, recompression, recadrage ;
  le marqueur doit rester détectable. Si votre marquage ne survit qu'au chemin heureux,
  il ne survit pas.
- **Couverture, scellée**, pour chaque génération, un reçu signé liant le digest de la
  sortie à son statut de marquage. La question d'audit devient mécanique :
  *montrez-moi une génération sans reçu correspondant.* Soit le journal a une réponse
  scellée, soit vous avez un manquement non discutable.

## L'endroit où les équipes se plantent en premier

Les équipes implémentent le 50(2), le marquage, et oublient que le 50(1) et le
50(3) sont des obligations face utilisateur sans SDK : le premier message du chatbot,
le badge dans l'UI, la mention pour les personnes dont les émotions sont catégorisées.
C'est de la configuration et de la rédaction, c'est auditable en cinq minutes, et
c'est la victoire de conformité la plus rapide de tout le règlement.

Puis le piège plus profond : l'evidence log livré avec votre SDK de marquage est votre
propre base de données. Modifiable par qui la détient. Le reçu qui survit à un audit
vit hors de l'artefact, signé, append-only, c'est la différence entre marquer et
pouvoir prouver qu'on a marqué
([post précédent](https://blog.noirebox.eu/fr/label-stripped-receipt-cant)).

Le 2 décembre, c'est dans quelques semaines. Le badge vous coûte un après-midi.
Faites celui-là aujourd'hui.
