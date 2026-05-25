---
title: "Cover, Visibility, and Concealment"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [cover, visibility, concealment, perception, stealth, combat, environment]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/07-cobertura-visibilidad-y-ocultacion.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-actions.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/06-critical-impact-and-breaking-parts.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-attrition-endurance-fatigue.md
  - core-books/transcendence-corebook/13-gm-toolkit/en/01-environmental-conditions.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/01-specializations.md
authority_refs:
  - Transcendence-design/docs/system/cover-visibility-concealment.md
  - Transcendence-design/data/system/cover-visibility-concealment.yaml
  - Transcendence-design/docs/system/environmental-conditions.md
  - Transcendence-design/docs/system/roll-types.md
section_modes:
  - heading: "Example"
    writing_mode: example
---

# Cover, Visibility, and Concealment

Cover, Visibility, and Concealment resolve three separate layers of a scene.

| Layer | What it resolves |
| --- | --- |
| **Cover** | Whether something physical blocks, deflects, or absorbs an attack line |
| **Visibility** | How far and how clearly details can be distinguished |
| **Concealment** | Whether a creature is precisely located by an enemy |

These layers are resolved separately.

A creature can have Cover without being concealed. It can stand in dense fog without anything stopping a hit. It can be concealed behind a barrier even when the area is well lit.

---

## Cover

**Cover** is physical or structural protection that interferes with an attack line.

Fog, smoke, darkness, dust, or rain are not Cover by themselves. They reduce Visibility and can help a creature hide, but they do not stop a hit.

| Cover | Criterion | Effect |
| --- | --- | --- |
| Light Cover | Protects a smaller part of the body or partially interferes with the attack line | `-1` to the attacker’s Attack Roll |
| Medium Cover | Protects a significant part of the body, but leaves clear openings | `-3` to the attacker’s Attack Roll |
| Total Cover | No direct attack line to the target | The target cannot be chosen by direct attacks |

---

### Light Cover

The target is not fully exposed, but can still be attacked through a reasonable line.

Examples:

- low furniture
- railing
- small rock
- thin tree
- door edge
- cover protecting about a quarter of the body

---

### Medium Cover

The target is protected by a significant obstacle, but still has some exposure.

Examples:

- thick tree
- large rock
- barricade
- window
- opening
- wall corner
- cover protecting half the body or more without covering it completely

---

### Total Cover

The obstacle completely blocks the direct line to the target.

Examples:

- solid wall
- closed door
- trench with no exposure
- closed structure
- mass that fully covers the target

A target with Total Cover cannot be chosen by direct attacks.

Even so, it may still be affected by:

- area attacks
- Techniques that alter the attack route
- destruction of the obstacle
- flanking
- elevation
- ricochet
- explosion
- any fiction that bypasses the direct line

---

## Destroying Cover

Physical Cover can be destroyed if the object producing it has material, Potency, and Durability.

To break Cover, use the normal breaking rule.

```text
Critical Potency >= Object Durability
```

| Result | Effect |
| --- | --- |
| Critical Potency >= Durability | The Cover breaks, opens, or stops protecting according to its nature |
| Critical Potency < Durability | The Cover does not break and loses `1` Durability |

Durability loss only occurs during a valid break attempt.

A valid attempt can come from:

- Critical Impact
- a Technique that permits breaking
- a specific weapon, object, or scene rule

Normal attacks do not reduce Durability by default.

---

## Cover and Attack Types

Cover applies against melee attacks, ranged attacks, and projectiles whenever the object materially interrupts the attack line.

If the attacker moves to an angle where the Cover no longer blocks the line, the Cover stops applying.

Cover is geometric and material. It is not a fixed state attached to the character.

---

## Shields as Cover

Shields are the main source of portable Cover.

A shield primarily grants Cover to its carrier’s space.

Covering another creature normally requires:

- a Technique
- a shield Reaction
- a rule that allows that Cover to extend outside the user’s own space

Cover granted by a shield depends on:

- shield size
- carrier size
- covered creature size
- attack angle
- the carrier’s ability to carry and control the shield

---

## Cover and Areas

Against area attacks, Cover only helps if the object can stand between the creature and the effect’s origin, direction, or expansion.

| Situation | Effect |
| --- | --- |
| Cover clearly blocks the area | Apply normal Cover |
| Cover partially protects against the area | Apply half the Cover penalty, rounded down |
| The area surrounds, fills, or ignores the Cover | Cover does not apply |

A barricade can help against a frontal explosion.

It does not help against gas filling the entire zone or fire falling from above.

---

## Visibility

**Visibility** defines how far and how clearly a creature can distinguish visual details.

For grid measurement:

```text
1 meter = 1 square
```

The game can use a grid or flexible measurement. A grid is recommended when combat, areas, Cover, approximate position, or tactical movement matter.

---

## Standard Visual Range

In clear conditions, a creature can recognize relevant details up to `60 meters`.

Beyond that range, an action depending on visual detail requires a Perception Specialization Roll.

The Narrator increases difficulty according to:

- distance
- size
- movement
- contrast
- environmental conditions

Simple rule:

```text
+1 Reference Level per 10 meters beyond effective visual range
```

Do not use 2-meter increments. They create too much counting at the table and do not add useful decisions.

---

## Reduced Visibility Ranges

| Condition | Intensity | Effective visual range |
| --- | --- | ---: |
| Rain | Light | 24 m |
| Rain | Intense | 15 m |
| Rain | Storm | 8 m |
| Snow | Light | 24 m |
| Snow | Intense | 15 m |
| Snow | Snowstorm | 8 m |
| Fog | Light | 20 m |
| Fog | Dense | 10 m |
| Fog | Thick | 5 m |
| Smoke | Light | 20 m |
| Smoke | Dense | 5 m |
| Smoke | Choking | 2 m |
| Dust or sand | Light | 25 m |
| Dust or sand | Moderate | 12 m |
| Dust or sand | Storm | 5 m |
| Absolute darkness | No light source | 0 m |
| Extranatural darkness | Active | 0 m, unless a valid countermeasure applies |

These values are reference guides.

If the condition is already represented as a Moderate, Severe, Disastrous, or Extreme environment, use environmental severity as the primary authority.

---

## Light Sources

Light sources establish an effective visual range when the environment lacks sufficient illumination.

| Source | Clear range | In dense visual condition |
| --- | ---: | ---: |
| Candle | 2 m | 1 m |
| Torch | 4 m | 2 m |
| Oil lamp | 6 m | 3 m |

A light source does not remove smoke, fog, dust, or extranatural darkness by itself.

It only allows vision within the range it can still pierce.

---

## Absolute Darkness and Extranatural Darkness

**Absolute darkness** occurs when there is not enough natural, artificial, or reflected light to see. In these conditions, visual range is `0 m`.

**Extranatural darkness** also reduces visual range to `0 m`, but it is not solved by an ordinary light source.

Extranatural darkness tied to the Darkness element blocks natural light and common illumination.

Countering it requires a compatible source:

- extranatural light tied to the Light element
- artifact
- Technique
- opposing environmental condition
- specific rule

---

## Perception and Senses

Perception does not mean sight alone.

It represents the ability to locate, distinguish, or interpret sensory signals.

A character can use Perception to:

- see
- hear
- smell
- feel vibration
- recognize contact
- read chemical signals
- use echolocation
- interpret another special sense they possess

Special senses use the same Perception structure unless a rule says otherwise.

A creature with a special sense may have additional bonuses and is not blocked by effects that do not interfere with that sense.

Example: a creature tracking by smell can ignore visual Darkness to locate a target, but may suffer penalties from wind, water, chemical smoke, or a Technique that alters scent.

---

## Combat Without Vision

A creature that cannot see its target does not automatically lose all competencies.

Instead:

- it cannot precisely choose targets it has not located
- it cannot use Techniques requiring clear visual reading
- it can attack an approximate position with a penalty or increased difficulty
- it may defend worse against threats it cannot read
- it can use other senses if they are relevant

| Situation | Effect |
| --- | --- |
| Target located by any relevant sense | Can be targeted; apply penalty or Reference Level increase only if the signal is weak, indirect, or hard to interpret |
| Target not located | Cannot be targeted by a direct attack |

The Impact Roll does not lose all bonuses from lack of sight.

If the attack connects, Impact resolves normally unless a specific rule says otherwise.

---

## Concealment

**Concealment** is the system layer that governs the tactical state `Hidden`, detection, approximate position, and the loss or maintenance of that advantage.

A creature that is `Hidden` is not precisely located by one or more enemies.

It is not invisibility. It is not immunity. It does not erase physical evidence.

It means the enemy does not know exactly where the creature is or cannot fix it as a direct target.

### `Hidden` State

`Hidden` is tracked by enemy or enemy group.

A creature can be `Hidden` from one guard, but not from another who saw them enter.

The base **Hide** action grants `Hidden` when its requirements are met and the roll succeeds. Traits, artifacts, preparations, or Techniques can also grant `Hidden` through more efficient or more specific routes, but the granted state remains the same.

When `Hidden` is created by a roll, that initial roll is preserved as the active value of the state until another roll, Technique, detection result, or fictional change replaces it.

While a creature is `Hidden` from an enemy:

- that enemy cannot choose it as the target of direct “one creature” attacks
- it can attack an area or suspected position if it has a reason to do so
- it can actively search for the hidden creature
- it can react to obvious signals, noise, contact, or environmental changes

`Hidden` does not protect against area effects that cover the real position.

---

## Hide

Hide is a base action when performed under pressure.

| Action | Rhythm | Attrition | Roll |
| --- | ---: | ---: | --- |
| Hide | 6 | 1 | Appropriate Specialization Roll against environmental difficulty or enemy Perception |

Outside a hostile scene, Hide has no rhythm cost.

The Narrator only calls for the roll when risk, opposition, or consequence exists.

A creature can attempt to hide if at least one of these conditions is true:

- it has Medium Cover or Total Cover
- it is outside the effective visual range of relevant enemies
- it is inside a reduced-Visibility condition that can hide its position
- it has a Technique, trait, artifact, or preparation that can grant `Hidden`

In addition, no relevant enemy must have it clearly located by an applicable sense.

Wanting to vanish is not enough while someone clearly sees, hears, smells, or perceives it.

If an enemy has it located without obstruction, the creature must first create a real opportunity.

It can do this by:

- breaking line of sight
- entering Cover
- entering smoke, fog, Darkness, vegetation, a crowd, or sufficient noise
- using a distraction
- moving outside the effective range of the sense locating it
- using a Technique, trait, artifact, or preparation that permits hiding while observed

---

## Concealment Roll

The creature makes an appropriate Specialization Roll against environmental difficulty or enemy Perception, depending on the scene.

Typical specializations:

- **Stealth**, to hide through silence, body control, and position
- **Survival**, to hide in natural terrain, vegetation, weather, or tracks
- another specialization, if a trait, Technique, or artifact justifies it

Ties favor the concealed creature.

---

## Attacking While `Hidden`

Attacking while `Hidden` can grant an opening advantage if the target does not react in time.

Before resolving the attack, relevant creatures within `10 meters` can attempt to detect the action if they have an applicable sense.

Use a Perception Specialization Roll against the active `Hidden` state or environmental difficulty.

A creature beyond `10 meters` can attempt this detection only if it has a special sense, Technique, preparation, or position that justifies reacting to that signal.

| Perception result | Effect |
| --- | --- |
| Failure | The attack keeps opening advantage |
| Success | Detects the action in time; the attacker gains no opening advantage against that creature |

If the attack keeps opening advantage, it gains `+3` to the Attack Roll against targets that did not detect the action in time.

Attacking while `Hidden` always compromises `Hidden`, even if the attack misses.

After the attack, resolve approximate position or detection according to the scene.

---

## Maintaining and Losing `Hidden`

`Hidden` holds while the creature does not give a sufficient signal to locate it.

Actions that compromise `Hidden`:

- making a melee attack
- making a ranged attack
- moving between cover
- running
- speaking loudly
- manipulating a visible or noisy object
- interacting with a light source
- changing position in a silent environment

Compromising `Hidden` does not automatically reveal exact position.

It means there is enough signal for nearby enemies to attempt location.

When a creature compromises `Hidden`, relevant creatures within `10 meters` can attempt a Perception Specialization Roll if they have an applicable sense.

Creatures beyond `10 meters` need a special sense, Technique, preparation, or circumstance that justifies detection.

Saying “I think it is there” or pointing to a suspected position does not reveal a concealed creature by itself.

Communicating suspicion enables area attacks or directed searching, but does not remove penalties or make the position exact.

---

## Uncertain Approximate Position

An action can reveal approximate position without revealing exact position.

Examples:

- an arrow leaves a patch of shrubs
- a stone falls from a ledge
- a voice comes from the west
- a shadow crosses behind smoke

Uncertain approximate position exists so the detector receives a playable clue without knowing whether they were right.

The player should know what their character perceived, but not whether that perception was correct.

---

## Player Hidden, Creature Detects

If the player is the one concealed:

1. The player keeps the roll or value that last established `Hidden`.
2. The Narrator rolls Perception for the creature trying to detect them.
3. If Perception beats the `Hidden` state, the creature locates the character’s real position.
4. If Perception does not beat the `Hidden` state, the Narrator rolls `1d8` and the creature acts toward the false position indicated by that direction, if its behavior justifies it.

The Narrator does not have to reveal whether the creature was right.

Only describe what the creature does.

---

## Creature Hidden, Player Detects

If a creature is the one concealed:

1. The player rolls Perception.
2. The Narrator secretly rolls the creature’s `Hidden` state.
3. The Narrator also secretly rolls `1d8` at the same time, declaring only that `Hidden` is being resolved.
4. If the player’s Perception beats the `Hidden` state, the Narrator points to the real position.
5. If the player’s Perception does not beat the `Hidden` state, the Narrator points to the false position indicated by the `1d8`.

The Narrator does not declare whether the player’s roll succeeded or failed.

The point shown is what the character believes they perceived.

Ties favor the concealed creature.

---

## False Direction

| 1d8 | Direction |
| --- | --- |
| 1 | Northwest |
| 2 | North |
| 3 | Northeast |
| 4 | West |
| 5 | East |
| 6 | Southwest |
| 7 | South |
| 8 | Southeast |

On a grid, the `1d8` result points by default to the square adjacent to the concealed creature’s real position in that direction.

If the creature occupies more than one square, use the adjacent square from the edge of its space in that direction.

If that square is invalid, blocked, or implausible, use the nearest plausible Cover, cell, or area in the same direction.

Without a grid, use a credible nearby zone in that direction.

---

## Detecting Concealed Creatures

There is no universal separate action called Search.

Searching resolves as a Perception Specialization Roll, a Technique, or a scene-specific action if the Narrator requires one due to time, position, or pressure.

On success, the creature detects the position for itself.

It may communicate a suspicion or direction if the scene allows speech, pointing, or coordination, but that communication does not automatically reveal the creature to everyone.

---

## Provoked Detection

Provoked detection occurs when a concealed creature produces a signal sufficient for others to have a chance to notice it.

The Narrator may:

- call for Perception
- use a fixed threshold
- reveal partial information if the signal is obvious

Provoked detection does not replace deliberate use of Perception or Techniques.

It resolves signals created by the concealed creature, not free scanning of the entire environment.

---

## Balance Limits

Concealment needs limits because it can become too strong if it prevents too many responses.

Safety rules:

- hiding requires a physical, environmental, or technical basis
- `Hidden` is tracked per enemy or enemy group, not as a universal state
- being hidden does not mean being untouchable
- area effects still work if they cover the real position
- attacking usually reveals or risks Concealment
- specialized Perception can accelerate detection, but should not erase the whole signal game
- creatures with non-visual senses can ignore or reduce visual Concealment
- abilities, Techniques, or creatures can declare that they ignore Concealment under specific conditions

---

## Quick Summary

| Element | Rule |
| --- | --- |
| Cover | Physical protection that interferes with an attack line |
| Visibility | Clarity and distance at which details can be distinguished |
| Concealment | Lack of precise location by one or more enemies |
| Light Cover | `-1` to the Attack Roll |
| Medium Cover | `-3` to the Attack Roll |
| Total Cover | Does not allow direct attacks |
| Clear visual range | `60 m` |
| Hide in combat | Rhythm `6`, Attrition `1` |
| Attacking while `Hidden` | Can grant `+3` to the Attack Roll |
| Attacking while `Hidden` | Always compromises `Hidden` |
| Ties | Favor the concealed creature |
| Approximate position | Can be real or false depending on Perception and `Hidden` |
