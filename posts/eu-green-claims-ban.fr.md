---
titre: L'UE a bien interdit « éco-friendly » — mais pas tout à fait comme on vous le raconte
resume: Vrai : depuis le 27 septembre 2026, la directive 2024/825 interdit les allégations vertes génériques et la « neutralité carbone » achetée par compensation. Vérifié ligne par ligne sur le texte officiel EUR-Lex, avec un audit de 20 minutes pour votre landing page.
date: 2026-10-22
themes: preuve, web
source: https://eur-lex.europa.eu/eli/dir/2024/825/oj
---

Un [article dev.to](https://dev.to/shuttlewright/the-eu-banned-eco-friendly-on-27-september-check-your-landing-page-3855) très partagé en ce moment affirme que l'UE a interdit « eco-friendly » le 27 septembre, « sans période de grâce », et vous propose un balayage de 20 minutes de votre landing page. C'est exactement le genre de titre qu'on relaie avant de vérifier — l'article lui-même ne cite aucune source. Je suis allé lire [le texte officiel sur EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024L0825). Verdict : **le cœur de l'affirmation est vrai**, mais trois nuances changent ce que vous devez réellement faire.

## Ce qui est vrai, vérifié sur le texte

La directive (UE) 2024/825 du 28 février 2024 — dite « EmpCo », *Empowering Consumers for the Green Transition* — modifie la directive « pratiques commerciales déloyales » (2005/29/CE). Son article 4 imposait aux États membres de transposer avant le **27 mars 2026** et d'appliquer les mesures **à partir du 27 septembre 2026**. Ce n'est ni une rumeur ni un projet : la date est dans le texte, et elle est passée.

Concrètement, trois familles de pratiques deviennent des pratiques commerciales déloyales interdites :

**1. Les allégations environnementales génériques.** Le considérant 9 cite nommément « respectueux de l'environnement », « écologique », « ami de la nature », « respectueux du climat », « biodégradable », « biosourcé » et similaires. Interdites **sauf** si vous démontrez une « performance environnementale excellente reconnue » pertinente pour l'allégation — le considérant 10 précise : écolabel UE (règlement 66/2010), label de type I ISO 14024 reconnu par un État membre, ou classe A d'étiquetage énergétique — **ou** si la spécification est fournie « en des termes clairs et visibles dans le même support de l'allégation ». L'exemple de la directive elle-même : « emballage respectueux du climat » = générique, interdit ; « 100 % de l'énergie utilisée pour la fabrication de cet emballage provient de sources renouvelables » = spécifique, admis.

**2. La « neutralité » achetée par compensation.** Le considérant 12 : affirmer qu'un produit a un impact neutre, réduit ou positif « sur la base de la compensation des émissions de gaz à effet de serre » doit être interdit « dans toutes les circonstances ». La directive liste les formulations visées : « neutre pour le climat », « certifié neutre en CO2 », « carbone positif », « zéro net pour le climat », « compensé sur le plan climatique ». Seule exception de fond : une allégation fondée sur l'impact réel du cycle de vie du produit — pas sur des crédits carbone achetés hors de votre chaîne de valeur. Sur ce point, l'article dev.to (« banned outright, cannot be fixed by wording ») est correct.

**3. Les labels maison.** Un badge « Eco certified » dessiné en interne est une pratique déloyale, sauf s'il repose sur un système de certification répondant aux critères de transparence et de vérifiabilité de la directive, ou s'il est établi par une autorité publique (considérant 7).

Le même texte couvre trois cas qu'on oublie : une allégation qui porte sur l'ensemble du produit alors qu'elle n'en concerne qu'un aspect (« fabriqué à partir de matériaux recyclés » quand seul l'emballage l'est) est trompeuse (considérant 11) ; présenter une exigence légale comme un argument commercial distinctif l'est aussi (considérant 15) ; et une promesse de performance environnementale future exige un plan de mise en œuvre mesurable, vérifié par un tiers indépendant (article 6).

## Ce que l'article viral simplifie

**« No grace period »** — faux par omission. La directive date du 28 février 2024 : l'industrie a eu deux ans et demi pour s'y préparer, et les États membres deux ans pour transposer. Ce qui est vrai : après le 27 septembre 2026, il n'y a plus de sursis supplémentaire.

**« Les mots sont interdits »** — pas absolument. Le mot n'est pas l'infraction ; l'infraction, c'est le caractère générique et invérifiable. Deux portes de sortie existent (performance excellente reconnue, ou précision claire dans le même support). Et « durable », « responsable », « conscient » sont pires que « écologique » : le considérant 10 dit explicitement qu'on ne peut même pas les justifier par une excellente performance environnementale, car ils couvrent aussi des caractéristiques sociales.

**« La compensation est interdite »** — non : la communication sur la compensation ne l'est pas. Vous pouvez continuer à dire que vous financez des projets de compensation. Ce qui est interdit, c'est d'en déduire que votre produit est « neutre ».

Deux cadrages utiles. D'abord, c'est du droit de la consommation : cela vise les pratiques commerciales **B2C** adressées à des consommateurs de l'UE, sur n'importe quel support — site, publicité, e-mails transactionnels, factures PDF, packaging, checkout. Une landing page SaaS grand public est dans le champ ; la documentation technique d'une offre strictement B2B, non. Ensuite, ne pas confondre avec la « directive Green Claims » (vérification préalable de chaque allégation explicite) : cette proposition a été retirée par la Commission en juin 2025. La 2024/825, elle, est adoptée et applicable.

Le contrôle revient aux autorités nationales de protection des consommateurs (en France, la DGCCRF), avec le régime de sanctions du droit des pratiques déloyales — des amendes pouvant atteindre au moins 4 % du chiffre d'affaires annuel pour les infractions généralisées. Sans compter le contentieux concurrentiel : le premier signalement viendra probablement d'un concurrent ou d'une ONG, pas d'un régulateur.

## L'audit 20 minutes, version développeur

Un grep suffit pour la première passe :

```bash
grep -rniE "eco[- ]?friendly|environmentally[- ]?friendly|climate[- ]?neutral|carbon[- ]?neutral|net[- ]?zero|sustainable|green|biodegradable|biosourcé|écologique|éco[- ]?responsable|neutre en CO2|compensé" \
  src content emails public \
  --include="*.html" --include="*.md" --include="*.js" --include="*.ts" \
  --include="*.tsx" --include="*.jsx" --include="*.json" --include="*.yaml"
```

Couvrez toutes les surfaces, pas seulement le dépôt : fichiers d'i18n, métadonnées (`og:description`, JSON-LD, sitemap), templates d'e-mails, PDF générés, badges en image de fond dans le CSS — et le site déployé, qui peut servir une version antérieure en cache. Chaque occurrence trouvée suit la même règle : prouvée par un label reconnu, précisée chiffres et source à l'appui, ou supprimée.

| Interdit (générique) | Admis (spécifique et vérifiable) |
| --- | --- |
| « Green hosting » | « Hébergé en Suède, région alimentée à 97 % d'hydraulique (mix 2025, source publique) » |
| « Climate neutral » (par compensation) | « −38 % d'émissions scopes 1+2 depuis 2022, bilan vérifié » — et suppression de l'argument de neutralité |
| Badge « Eco certified » maison | Un label reconnu (écolabel UE, ISO 14024 type I)… ou rien |

Documentez le passage : commit, capture datée, page avant/après. Si un contrôle remonte à la version du 26 septembre, pouvoir montrer la correction et sa date compte.

## La vraie leçon

Ce qui change le plus n'est pas la liste de mots — c'est l'inversion de la charge. Une allégation verte est désormais, juridiquement, une affirmation qu'il faut pouvoir prouver au moment où on la publie : chiffres, périmètre, source. C'est un sujet de preuve avant d'être un sujet de marketing. Et si vous n'avez rien à montrer, il y a un mot de moins à écrire — c'est l'audit le plus rapide du monde.

Sources : directive (UE) 2024/825 — [texte français](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024L0825) et [texte anglais](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L0825) sur EUR-Lex.
