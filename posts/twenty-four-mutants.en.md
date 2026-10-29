---
titre: 24 mutants: every compliance check must catch its own saboteur
resume: Test coverage tells you your checks run. It doesn't tell you they detect anything. Mutation testing, 24 sabotages, each of which exactly one check must catch, is the honesty standard compliance-as-code deserves.
date: 2026-10-22
themes: preuve, conformité
source: https://github.com/noirebox/noirebox
image: https://blog.noirebox.eu/img/twenty-four-mutants.jpg
image_alt: Vingt-quatre petits personnages de saboteurs en ombre chinoise face à une rangée de serrures, chacune munie d'une alarme qui s'allume.
---

Compliance-as-code has a dirty secret: most "automated compliance checks" have never been proven to detect anything. They run. They pass. They produce green. Whether they would *fail when they should* is a question nobody asks, because the check passing is the product.

There's an old answer from genetics and compiler testing: **mutation testing**. Sabotage the thing under test, on purpose, and require the safety net to catch each specific sabotage. We run 24 of them on our compliance engine. Each mutant makes exactly one change, flips one operator, deletes one retention rule, points one config read at the wrong file, and the requirement is brutal: **exactly the check targeting that obligation must fail.** Not "something fails". Not "the suite goes red". The *right* check, for the *right* reason.

## Three things the mutants caught that coverage never would

**The wrong-file read.** One mutant pointed a C2PA marking routine at a governance config in a sibling directory, a path that *looked* right. Twenty-three checks noticed nothing; the one that mattered slept through it. Coverage: 100%. Detection: zero. Real bug, fixed.

**The operator flip.** Change `>=` to `>` in a six-month retention rule and no line-coverage metric even trembles, the branch is still exercised, just wrongly. A 180-day retention that admits 179 days is precisely the difference between compliance and a finding, and only its saboteur can prove the check sees it.

**The deleted control.** Remove a logging requirement entirely and watch which check notices. If none does, you haven't written a check, you've written a greeting.

## Why this matters more in compliance than anywhere else

In product testing, a blind check wastes someone's time. In compliance, a blind check manufactures false assurance, the most dangerous product there is, because it's consumed by exactly the people who will be blamed. Regulators don't ask "do you have automated checks?"; they ask "show us a failure your checks caught." Mutation testing is the rehearsal of that question, on demand, in CI.

The score becomes a public number the same way test counts are: ours is 24/24, and it's in the repo for anyone to re-run. The discipline generalizes: **every control you sell or certify should come with its saboteur.** If a vendor can't show you the mutation that their check catches, the honest summary of their product is: *it has never been seen to work.*

Green dashboards are cheap. Sabotage-proof ones are the product.
