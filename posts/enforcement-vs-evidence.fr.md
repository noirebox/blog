---
titre: Contrôle vs preuve : pourquoi OWASP ACS et l'identité NIST ont quand même besoin d'un journal
resume: 2026 a livré du contrôle sérieux pour les agents IA, OWASP ACS, identité NIST, control plane KedgeFlow. Leurs propres évaluations admettent ce qu'ils ne font pas : prouver ce qui a été décidé, après coup, à quelqu'un qui ne vous fait pas confiance. C'est une autre couche.
date: 2026-10-22
themes: agents, preuve
source: https://genai.owasp.org/resource/agent-control-standard-acs/
image: https://blog.noirebox.eu/img/enforcement-vs-evidence.jpg
image_alt: Un poste de garde à l'entrée d'un bâtiment (contrôle) face à une boîte noire d'avion scellée (preuve), style manuel d'ingénierie.
---

2026, c'est l'année où le contrôle des agents est devenu sérieux. Trois efforts qui
méritent d'être lus, aucun n'est de la vapeur :

- **[OWASP Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/)**
  (septembre 2026), application de politique runtime portable et visibilité across
  plateformes d'agents.
- **Le concept paper NIST sur l'identité des agents logiciels et IA** (février 2026),
  identité, autorisation, audit : le bon vocabulaire, enfin.
- **[KedgeFlow](https://arxiv.org/abs/2610.14810)** (octobre 2026), un control plane
  programmable avec des allocations signées à usage unique et un chaînage
  grant–claim–dispatch ; leur évaluation compte 6 560 tentatives de claim concurrentes
  produisant exactement un claim réussi par allocation. C'est du vrai génie
  d'infrastructure.

On aime les trois, et on n'en construit aucun, NoireBox n'impose rien au moment de
l'exécution. Mais lisez leurs propres évaluations attentivement, parce que chacune
nomme la couche manquante :

Le papier KedgeFlow, en limitations, rapporte qu'**une politique permissive a quand
même autorisé un effet indésirable**, l'autorisation d'exécution seule a des limites,
de leur propre mesure. Les contrôles OWASP ACS décident et agissent ; rien dans le
standard ne rend la séquence de décisions infalsifiable a posteriori. Et la
disclosure du 18 octobre d'UAI-BLOCK énonce son trou verbatim : *pas de journaux
d'audit à falsification résistante, pas de vérification indépendante.*

## Contrôle et preuve répondent à deux questions différentes

Le contrôle répond : **« cela peut-il arriver, maintenant ? »** Il tourne au moment
de l'action, dans votre infrastructure, sous votre politique.

La preuve répond : **« que s'est-il passé, et pouvez-vous me le prouver si je ne vous
fait pas confiance ? »** Elle tourne après coup, sur des enregistrements que l'agent,
et l'opérateur, ne peuvent pas réécrire discrètement.

Il faut les deux, et ils se composent proprement : chaque allow/deny produit par un
gate peut être scellé comme événement signé dans un journal chaîné par hash, l'identité
de l'agent *telle que vérifiée à l'exécution* (une credential OS, pas un nom déclaré),
l'action, la ressource, le warrant derrière un allow. Alors « notre gate n'a jamais
approuvé de requête non autorisée » cesse d'être une affirmation et devient un replay :
l'auditeur rejoue la séquence scellée et vérifie.

La version audit-grade du test de race de KedgeFlow, ce n'est pas « la gateway a
committé un effet », c'est « *voici l'enregistrement scellé et vérifiable qu'elle en a
committé exactement un, et vous pouvez le vérifier vous-même hors ligne* ».

## La partie honnête

Cette composition est une affirmation, et les affirmations ont besoin de preuves
elles aussi. Notre couche de preuve a ses trous ouverts, pas de bench du débit du
journal à l'échelle production, pas d'ancrage out-of-band (TSA / pin public) câblé
encore. Le score reste public dans
[docs/RELATED-WORK.md](https://github.com/noirebox/noirebox/blob/main/docs/RELATED-WORK.md),
à côté de la même carte de la couche contrôle.

Si vous construisez le gate : parfait, construisez-le bien. Ne le laissez simplement
pas être le seul témoin. Les gates se font mal configurer, contourner, hériter. Le
journal est celui qui témoigne après, et il devrait être construit par quelqu'un
dont le seul métier est d'être crédible.
