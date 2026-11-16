---
title: "Borrowed Force"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 9
status: draft
canonical: false
tags: [techniques, bufoni, torsion, reactive, utility, attack-redirection]
authority_refs:
  - Transcendence-design/data/system/techniques.yaml
  - Transcendence-design/docs/system/technique-la-fuerza-prestada.md
related:
  - core-books/transcendence-techniques/es/163-la-fuerza-prestada.md
  - core-books/transcendence-corebook/06-species/es/14-bufoni.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-acciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/05-heridas-y-dano.md
section_modes:
  - heading: "Example"
    writing_mode: example
---

# Borrowed Force

### Reactive - Utility

**Novice Rank**

*The blow finds other flesh.*

| Range | Area | Duration | Roll |
| --- | --- | --- | --- |
| Weapon reach | 1 Creature | Instantaneous | `A.R.` |

| Saving Roll | Impact | Rhythm | Attrition |
| --- | --- | --- | --- |
| — | — | `3` | `1` |

## Requirements

- Novice or higher competency with the weapon used.
- A weapon with the `Torsion` profile.

## Keywords

- `Torsion`

## Effect

When a physical attack against a single creature is declared, you may intervene before its defense resolves if your weapon can reach the attacking weapon or limb at the contact point you intend to alter. You may intervene even when the attack is not directed at you. This Technique cannot redirect projectiles or area attacks.

Choose another creature that the same attack can reach along a physically valid trajectory, without extending its reach or passing through obstacles. Make an `A.R.` with your Torsion weapon, opposed by the aggressor's `A.R.`.

If your `A.R.` does not exceed the aggressor's, the attack continues against its original recipient, who retains their normal defense.

If you exceed it, the attack is directed at the chosen creature. The aggressor keeps the original die result of their `A.R.` and adjusts only modifiers that depend on the new recipient. That `A.R.` is opposed by the chosen creature's `D.R.`.

If the attack connects, the aggressor resolves its impact and contact effects against the new recipient's protection. Their requirements, margins and resistance checks are evaluated against that creature. You add neither impact nor effects from your own weapon.

Each use affects a single attack, not an entire sequence or its movement or additional attacks. You may attempt this Technique once against each attack. An attack already redirected through this same Technique cannot be redirected through it again. The new recipient retains their other permitted reactions.

You pay Rhythm and Attrition even if the intervention fails.

## Example

An aggressor attacks your companion with `A.R.` 10. You can reach the attacking weapon, and another creature lies on a valid trajectory for that same blow. Your `A.R.` is 12: you redirect the attack. With no recipient-dependent modifier changes, it retains `A.R.` 10. The new creature gets `D.R.` 11 and avoids the blow, taking no impact. You have paid Rhythm 3 and Attrition 1. If your intervention had scored 10, the tie would leave the attack directed at your companion, who would retain their normal defense.
