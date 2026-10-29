---
titre: Un UPDATE SQL contre l'alibi de votre agent IA, et la défense qui le prend en 458 ms
resume: Réponse produit au labo d'attaque paru sur mon journal de bord : ce que NoireBox fait exactement quand quelqu'un réécrit une décision dans le journal, chaîne SHA-256, signature Ed25519, verdict localisé en 458 ms, et vérification par un tiers qui n'a pas besoin de vous croire.
date: 2026-10-22
themes: agents, preuve
source: https://blog.slabb.dev/fr/one-sql-update-your-ai-agents-alibi-destroyed-and-caught-in-458-ms
image: https://blog.noirebox.eu/img/one-sql-update-defense.jpg
image_alt: Base de données SQLite reliée par une chaîne de hachage dorée, maillon rompu au niveau de l'événement 2 ; terminal affichant l'UPDATE SQL ; verdict « DETECTED » en 458 ms.
---

[Le labo d'attaque est paru sur mon journal de bord](https://blog.slabb.dev/fr/one-sql-update-your-ai-agents-alibi-destroyed-and-caught-in-458-ms) : on scelle le journal d'un agent avec NoireBox, on donne une console SQLite à l'attaquant, et une seule ligne réécrit l'histoire, « le client VALIDE le devis » devient « le client REFUSE, aucune action requise ». Verdict : événement 2, hash invalide, 458 ms pour le désigner parmi mille. Ce billet est la réponse côté défense : ce qui s'est passé à l'intérieur, pourquoi c'est construit comme ça, et, c'est important, où ça s'arrête.

## Pourquoi une ligne ne passe pas

Chaque événement du journal embarque le hash du précédent :

```json
{
  "seq": 2,
  "type": "llm_output",
  "payload": {"summary": "The client VALIDATES the quote, next step: signature."},
  "prev_hash": "5f164b1ab574fb89e84d2f88d93bdd5a1a80282ae4710fda89fb92282ca33c59",
  "event_hash": "37093f3e23b64c1c7f3ed621ce448c9eba178b5a732ee57f4ad1d0c47b0850e8",
  "signature": "2ecfdb1233a43d08d8bf836db494dc5cbaf2c53674eae409ed…"
}
```

`event_hash` est un SHA-256 sur tout l'événement, séquence, horodatage, type, payload **et le hash du précédent**, et la signature est une Ed25519 sous la clé d'instance. L'historique n'est pas stocké, il est *engagé*. L'attaque tient en une ligne :

```sql
UPDATE events SET payload = '{ "summary": "The client REFUSES the quote, no action required." }'
WHERE seq = 2;
```

```text
[✗] DETECTED, event 2: invalid hash (content was modified)
```

Pas « quelque chose a bougé quelque part » : **événement 2, contenu modifié**. Rapiécer sans la clé exige de refaire toute la queue du journal, rehasher la moitié de la chaîne, par tentative. Sur mille événements : 242 ms pour vérifier un journal intact, 458 ms pour pointer l'événement 500 falsifié en plein milieu.

## La fonction réelle : être cru par quelqu'un qui ne vous croit pas

Le 21 octobre 2026, OpenAI a reconnu que ses propres agents avaient affaibli le système interne chargé de les surveiller, et que l'un d'eux avait nié l'avoir fait. La leçon est la même pour tout le monde : quand l'acteur surveillé peut toucher l'instrument de surveillance, la preuve doit vivre hors de sa portée. En pratique, « hors de portée » veut dire : un export vérifiable sur la machine d'un tiers.

```bash
curl -s http://127.0.0.1:8768/api/v1/export > export.json
python3 verifier/verifier.py export.json
```

```text
[✓] INTACT, 3 events verified, attestation valid   exit 0
[✗] TAMPERING DETECTED, event 2: invalid hash      exit 1
```

Pas de dashboard, pas d'appel à la maison, pas de « croyez-moi sur les logs ». Le vérificateur recalcule la chaîne entière depuis le fichier : exit 0 ou exit 1.

## Ce que ce n'est pas

Le marketing facile s'arrêterait là. Un produit honnête énonce ses limites :

- **Tamper-evident n'est pas tamper-proof.** Le sceau tient contre quiconque ne détient pas la clé d'instance, la garde de cette clé est la vraie frontière de sécurité.
- **La version sophistiquée de l'attaque** efface tout et rejoue l'historique en re-signant. C'est ce que répond l'ancrage RFC 3161 : périodiquement, le journal scelle son hash de tête auprès d'une autorité d'horodatage externe, comme un événement du journal. Rejouer le passé, et les ancres ne collent plus.
- **Supprimer le store supprime la preuve.** Exports et ancres conservés à l'extérieur, une discipline opérationnelle, pas une ligne de code.
- **Ce n'est pas une certification.** NoireBox ne rend rien « conforme » ; il rend les affirmations *vérifiables*, ce qui précède toute conformité.

## Pour que vos agents l'aient d'office

Les quatre opérations existent aussi en serveur MCP (`noirebox-mcp`) : `noirebox_scan` (garde-fou sur les transcripts entrants), `noirebox_log_event`, `noirebox_verify`, `noirebox_attestation`. Tout agent qui parle MCP obtient une boîte noire comme il obtient un système de fichiers, une infrastructure dont il ne peut pas se défaire.

## Reproduire

```bash
pip install noirebox            # 0.24.0 · MIT
git clone https://github.com/noirebox/noirebox
cd noirebox && .venv/bin/python demo/demo_tamper.py    # la chaîne explose
python3 verifier/verifier.py export.json               # exit 0 / 1 / 2
```

Le labo d'attaque complet, avec le contexte et les chiffres : [mon journal de bord](https://blog.slabb.dev/fr/one-sql-update-your-ai-agents-alibi-destroyed-and-caught-in-458-ms). Le modèle de menace, sans filtre : [docs/THREAT-MODEL.md](https://github.com/noirebox/noirebox/blob/main/docs/THREAT-MODEL.md).

Qui garde le gardien, quand le gardien est un fichier à côté de l'agent ? La réponse n'a jamais été « un meilleur fichier ». C'est une structure dont la clé vit hors de portée de la chose surveillée.
