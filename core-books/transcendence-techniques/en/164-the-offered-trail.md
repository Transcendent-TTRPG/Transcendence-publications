---
title: "The Offered Trail"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 9
status: draft
canonical: false
tags: [techniques, bufoni, unpredictability, reactive, utility, concealment, false-location]
authority_refs:
  - Transcendence-design/data/system/techniques.yaml
  - Transcendence-design/docs/system/technique-el-rastro-ofrecido.md
  - Transcendence-design/docs/system/cover-visibility-concealment.md
related:
  - core-books/transcendence-techniques/es/164-el-rastro-ofrecido.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/07-cover-visibility-and-concealment.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/07-cobertura-visibilidad-y-ocultacion.md
section_modes:
  - heading: "Example"
    writing_mode: example
---

# The Offered Trail

### Reactive - Utility

**Novice Rank**

*Claws find leaves.*

| Range | Area | Duration | Roll |
| --- | --- | --- | --- |
| Weapon reach | 1 Creature | Instantaneous | `A.R.` |

| Saving Roll | Impact | Rhythm | Attrition |
| --- | --- | --- | --- |
| — | — | `2` | `1` |

## Requirements

- Novice or higher competency with the weapon used.
- A weapon with the Unpredictability profile.
- Be Hidden from the detector.

## Keywords

- Unpredictability
- Hidden

## Effect

When an enemy is about to resolve an attempt to locate you, you may declare this Technique before learning the result of their Perception roll.

Choose a false position different from the one you occupy, where your weapon can produce a physically plausible signal for the sense the detector is using. Your weapon's reach limits the signal's point of origin, not the distance to the detector; the detector must be able to perceive it under the normal detection rules.

Make an `A.R.` with your Unpredictability weapon, opposed by the detector's Perception `S.R.`. Use that same Perception result to resolve their normal attempt to locate you against the active value of your Hidden state. You neither reroll nor replace that value, and the detector does not make a second Perception roll for this Technique.

If their Perception exceeds your Hidden value, they locate your real position, even if your `A.R.` is higher.

If their Perception does not exceed your Hidden value and your `A.R.` exceeds their Perception, they receive the false position you chose as a clue, instead of the one determined by 1d8. If your `A.R.` does not exceed their Perception, determine the false position through the normal Concealment procedure.

The creature decides what to do with the clue. This Technique does not force them to move or attack, does not modify your Hidden value, and does not prevent future searches. It does not erase information obtained through other senses or negate automatic detection.

Each use affects one localization attempt by one detector. You may attempt this Technique only once against that attempt. Other observers resolve detection normally; the signal may compromise your concealment from them under the usual rules.

This Technique deals no impact and applies no effects from your weapon, grants no Opening Advantage, and does not protect you from areas that cover your real position.

You pay Rhythm and Attrition even if you fail to direct the clue.

## Example

Your active Hidden value is 12. You declare a valid signal point before detection resolves. You get `A.R.` 14 and the enemy gets Perception 10: they receive your chosen point as a clue. If their Perception were 13, they would locate your real position even with your `A.R.` still at 14. If you got `A.R.` 10 against Perception 10, you would not direct the clue: the false position would follow the normal procedure. In every case, you pay Rhythm 2 and Attrition 1.
