---
titre: Qui a fait ça, vraiment ? L'identité à l'exécution pour les agents IA
resume: Votre journal dit « agent-7 l'a fait ». Agent-7, c'est quoi — une credential OS vérifiée, ou un nom que le logiciel a inventé ? La différence décide si votre audit trail prouve quoi que ce soit, et les expériences brokers de 2026 montrent enfin comment fermer l'écart.
date: 2026-10-22
themes: agents, preuve
source: https://futurium.ec.europa.eu/en/apply-ai-alliance/community-content/uai-block-ai-governance-principles-tested-access-controls-technical-progress-and-international
image: https://blog.noirebox.eu/img/execution-time-identity.jpg
image_alt: Un badge d'accès plastifié « agent-7 » posé à côté d'une empreinte digitale scannée sur un lecteur, lumière froide de datacenter.
---

Demandez à un responsable conformité qui a effectué une action dans ses systèmes, il
vous donnera un nom. Demandez au système, vous obtiendrez généralement une chaîne de
caractères : `agent-7`, `assistant`, `user`. L'écart entre ces deux réponses est
l'endroit où la plus grande partie de l'« accountability » des agents se dissout
discrètement — parce qu'**un nom que le logiciel se donne n'est pas une identité.**

## La leçon 2026 : les brokers vérifient, les agents déclarent

Les expériences les plus instructives de l'année viennent d'un endroit inattendu :
les prototypes de broker d'un chercheur indépendant. Le test T04-v06 d'UAI-BLOCK a
fait une petite chose proprement — il a donné à l'agent simulé et au broker **des
identités Linux distinctes**, puis laissé l'agent atteindre un fichier protégé
*uniquement* via un socket de domaine Unix où le broker pouvait vérifier la credential
du pair (`SO_PEERCRED`). L'agent pouvait obtenir la ressource approuvée à travers le
gate ; il ne pouvait pas lire le fichier directement. Le concept paper NIST sur
l'identité des agents logiciels et IA pointe la même direction au niveau des
standards : l'identité et l'autorisation appartiennent à l'infrastructure, pas à
l'auto-description de l'agent.

Le pattern généralise au-delà des OS. L'identité vérifiée à l'exécution peut être un
uid OS, un certificat client TLS, une credential de workload — ce qui compte, c'est
que le *gate* vérifie quelque chose que l'agent ne peut pas forger, et que le résultat
de la vérification voyage avec la décision.

## Sceller le check, pas la déclaration

Voici où ça rejoint le journal. Un reçu d'autorisation — ce que nous avons ajouté à
NoireBox ce mois-ci — enregistre une décision de gate, et son premier champ est
délibérément nommé pour forcer la distinction :

- `agent` : l'identité du demandeur **telle que vérifiée à l'exécution** —
  `os:uid=942 via SO_PEERCRED`, pas « agent-7 » ;
- `action` et `resource` : ce qui a été demandé, sur quoi ;
- `decision`, fail-closed : `allowed | denied | gate_error` — un gate en échec est
  *nommé*, jamais discrètement retenté en allow ;
- et pour chaque allow, un **warrant** : l'autorité indépendante sur laquelle il
  s'appuie (une instruction utilisateur, un reçu antérieur, un octroi explicite).

Les refus au scellement sont là où vit l'honnêteté : un allow sans warrant est
rejeté. Un warrant qui dit que la ressource était « pertinente » ou « plausible » —
la propre force d'attraction de la ressource, le vocabulaire de lavage — est rejeté
en le nommant. Vous vouliez l'autoriser parce qu'elle était *là* ? Le journal refuse
d'écrire ça comme de l'autorité.

Puis la passe d'audit (`replay`) attrape ce qui a été scellé en contournant les
refus : des allows sans warrant, des warrants lavés, et des **gate flips** — un triple
nié tôt dans la séquence et allowé plus tard. Soit le warrant a légitimement changé
(scellez le nouveau), soit votre gate est incohérent. Les deux manquements se
découvrent mieux par un replay que par un journaliste.

## Le test inconfortable pour votre propre stack

Trouvez le dernier rapport d'incident que votre plateforme d'agents a produit. Le
champ « qui » contient-il une credential qu'un composant d'infra a vérifiée — ou une
chaîne fournie par l'agent ? Si c'est la seconde, vous n'avez pas d'accountability ;
vous avez de l'autobiographie.

Le correctif n'est pas exotique. Des identités séparées. Une vérification au gate.
Le decision scellé avec la vérification attachée, pour que l'enregistrement porte sa
propre preuve. Tout le reste, ce sont des conventions de nommage.
