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
  - core-books/transcendence-corebook/12-gm-toolkit/en/01-environmental-conditions.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/01-specializations.md
authority_refs:
  - Transcendence-design/docs/system/cover-visibility-concealment.md
  - Transcendence-design/data/system/cover-visibility-concealment.yaml
  - Transcendence-design/docs/system/environmental-conditions.md
  - Transcendence-design/docs/system/roll-types.md
---

# Cover, Visibility, and Concealment

Cover, Visibility, and Concealment resolve three different scene problems.

Cover is physical protection. Something blocks, deflects, absorbs, or interrupts an attack line. Visibility defines how far and how clearly details can be distinguished. Concealment defines whether a creature is precisely located by an enemy.

A creature can have Cover without being hidden. It can stand in dense fog without anything stopping a hit. It can be concealed behind a barrier even when the area is well lit. The table resolves each layer separately.

---

## Cover

Cover is physical or structural protection that interferes with an attack line.

Fog, smoke, and darkness are not Cover by themselves. They reduce Visibility and can help a creature hide, but they do not stop a hit.

| Cover | Criterion | Effect |
| --- | --- | --- |
| Light Cover | Protects a smaller part of the body or partially interferes with the line. | -1 to the attacker's Attack Roll. |
| Medium Cover | Protects a significant part of the body, with clear openings. | -3 to the attacker's Attack Roll. |
| Total Cover | No direct attack line to the target. | Cannot be targeted by direct attacks. |

### Light Cover

The target is not fully exposed, but can still be attacked through a reasonable line.

Examples: low furniture, railing, small rock, thin tree, door edge, or cover protecting about a quarter of the body.

### Medium Cover

The target is protected by a significant obstacle, but still has some exposure.

Examples: thick tree, large rock, barricade, window, opening, wall corner, or cover protecting half the body or more without covering it completely.

### Total Cover

The obstacle completely blocks the direct line.

Examples: solid wall, closed door, trench with no exposure, closed structure, or mass that fully covers the target.

A target with Total Cover can still be affected by area attacks, Techniques that alter the attack route, destruction of the obstacle, flanking, elevation, ricochet, explosion, or other fiction that bypasses the direct line.

---

## Destroying Cover

Physical Cover can be destroyed if the object producing it has material, Potency, and Durability.

To break Cover, use the normal break rule.

```text
Critical Potency >= Object Durability
```

If Critical Potency is equal to or greater than Durability, the Cover breaks or stops protecting according to its nature.

If Critical Potency is lower, the Cover does not break, but loses 1 Durability. Normal attacks do not reduce Durability by default; there must be a valid Break Attempt, Critical Impact, Technique, or specific rule.

---

## Cover and Attack Types

Cover applies against melee attacks, ranged attacks, and projectiles whenever the object materially interrupts the attack line.

If the attacker stands at an angle where the Cover no longer blocks the line, it does not apply. Cover is geometric and material, not a fixed state attached to the character.

### Shields as Cover

Shields are the main source of portable Cover.

A shield primarily grants Cover to its carrier's space or cell. Covering another creature normally requires a Technique, a shield Reaction, or a rule that permits extending that Cover outside the user's own space.

Shield Cover depends on shield size, carrier size, covered creature size, attack angle, and the carrier's ability to carry and control the shield.

### Cover and areas

Against area attacks, Cover only helps if the object can stand between the creature and the effect's origin, direction, or expansion.

| Situation | Effect |
| --- | --- |
| Cover clearly blocks the area. | Apply normal Cover. |
| Cover partially protects against the area. | Apply half the Cover penalty, rounded down. |
| The area surrounds, fills, or ignores the Cover. | Cover does not apply. |

A barricade can help against a frontal explosion. It does not help against gas filling the entire zone or fire falling from above.

---

## Visibility

Visibility defines how far and how clearly a creature can distinguish visual details.

For grid measurement:

```text
1 meter = 1 square
```

The game can use a grid or flexible measurement. A grid is recommended when combat, areas, Cover, approximate position, or tactical movement matter.

### Standard visual range

In clear conditions, a creature can recognize relevant details up to 60 meters.

Beyond that range, an action depending on visual detail requires a Perception Specialization Roll. The Narrator increases difficulty based on distance, size, movement, contrast, and environmental conditions.

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
| Extranatural darkness | Active | 0 m, unless valid countermeasure |

These values are quick references. If the condition is already represented as a Moderate, Severe, Disastrous, or Extreme environment, use environmental severity as the primary authority.

---

## Light Sources

Light sources establish an effective visual range when the environment lacks sufficient illumination.

| Source | Clear range | In dense visual condition |
| --- | ---: | ---: |
| Candle | 2 m | 1 m |
| Torch | 4 m | 2 m |
| Oil lamp | 6 m | 3 m |

A light source does not remove smoke, fog, dust, or extranatural darkness by itself. It only allows vision within the range it can still pierce.

### Absolute darkness and extranatural darkness

Absolute darkness occurs when there is not enough natural, artificial, or reflected light to see. In those conditions, visual range is 0 m.

Extranatural darkness also reduces visual range to 0 m, but it is not solved by an ordinary light source. Extranatural darkness tied to the Darkness element blocks natural light and common illumination.

Countering it requires a compatible source: extranatural light tied to the Light element, an artifact, a Technique, an opposing environmental condition, or a specific rule.

---

## Perception and Senses

Perception does not mean sight alone. It represents the ability to locate, distinguish, or interpret sensory signals.

A character can use Perception to see, hear, smell, feel vibration, recognize contact, read chemical signals, use echolocation, or use another special sense they possess.

Special senses use the same Perception structure unless a rule says otherwise. A creature with a special sense can have additional bonuses and is not blocked by effects that do not interfere with that sense.

Example: a creature tracking by smell can ignore visual Darkness to locate a target, but can suffer penalties from wind, water, chemical smoke, or a Technique that alters scent.

---

## Combat Without Vision

A creature that cannot see its target does not automatically lose all competencies.

Instead:

- it cannot precisely choose targets it has not located;
- it cannot use Techniques requiring clear visual reading;
- it can attack an approximate position with a penalty or increased difficulty;
- it may defend worse against threats it cannot read;
- it can use other senses if they are relevant.

| Situation | Effect |
| --- | --- |
| Target located by any relevant sense. | Can be targeted; apply penalty or Reference Level only if the signal is weak, indirect, or hard to interpret. |
| Target not located. | Cannot be targeted by a direct attack. |

The Impact Roll does not lose all bonuses from lack of sight. If the attack connects, Impact resolves normally unless a specific rule says otherwise.

---

## Concealment

Concealment is a tactical state: a creature is not precisely located by one or more enemies.

It is not invisibility, immunity, or erasure of physical evidence. It means the enemy does not know exactly where the creature is or cannot fix it as a direct target.

### Hide

Hide is a base action when performed under pressure.

| Action | Rhythm | Attrition | Roll |
| --- | ---: | ---: | --- |
| Hide | 5 | 1 | Appropriate Specialization Roll against environment difficulty or enemy Perception |

Outside a hostile scene, Hide has no Rhythm cost. The Narrator only calls for the roll when risk, opposition, or consequence exists.

A creature can attempt to hide if at least one of these conditions is true:

- it has Medium Cover or Total Cover;
- it is outside the effective visual range of relevant enemies;
- it is inside a reduced-Visibility condition that can hide its position;
- it has a Technique, trait, artifact, or preparation that permits Concealment.

In addition, no relevant enemy must have it clearly located by an applicable sense. Wanting to vanish is not enough while someone clearly sees, hears, smells, or perceives it.

If an enemy has it located without obstruction, the creature must first create a real opportunity: break line of sight, enter Cover, enter smoke, fog, Darkness, vegetation, a crowd, or sufficient noise, create a distraction, move outside the effective range of the sense locating it, or use a Technique, trait, artifact, or preparation that permits hiding while observed.

### Concealment roll

The creature makes an appropriate Specialization Roll against environmental difficulty or enemy Perception, depending on the scene.

Typical specializations:

- Stealth to hide through silence, bodily control, and position;
- Survival to hide in natural terrain, vegetation, weather, or tracks;
- another specialization if a trait, Technique, or artifact justifies it.

Concealment is tracked by enemy or enemy group. A character can be hidden from one guard, but not from another who saw them enter.

---

## Effects of Concealment

While a creature is concealed from an enemy:

- that enemy cannot choose it as the target of direct “one creature” attacks;
- it can attack an area or suspected position if it has a reason to do so;
- it can search with Perception, a Technique, or a scene-specific action;
- it can react to obvious signals, noise, contact, or environmental changes.

Concealment does not protect against area effects that cover the real position.

### Attacking from Concealment

Attacking from Concealment can grant an opening advantage if the target does not react in time.

Before resolving the attack, relevant creatures within 10 meters can attempt to detect the action if they have an applicable sense. Use a Perception Specialization Roll against active Concealment or environmental difficulty.

A creature beyond 10 meters can attempt this detection only if it has a special sense, Technique, preparation, or position that justifies reacting to that signal.

| Perception result | Effect |
| --- | --- |
| Failure | The attack keeps opening advantage. |
| Success | Detects the action in time; the attacker gains no opening advantage against that creature. |

If the attack keeps opening advantage, it gains +3 to the Attack Roll against targets that did not detect the action in time.

Attacking from Concealment always compromises Concealment, even if the attack misses. After the attack, resolve approximate position or detection according to the scene.

---

## Maintaining and Losing Concealment

Concealment holds while the creature does not give a sufficient signal to locate it.

Actions that compromise Concealment:

- making a melee attack;
- making a ranged attack;
- moving between cover;
- running;
- speaking loudly;
- manipulating a visible or noisy object;
- interacting with a light source;
- changing position in a silent environment.

Compromising Concealment does not automatically reveal exact position. It means there is enough signal for nearby enemies to attempt location.

When a creature compromises Concealment, relevant creatures within 10 meters can attempt a Perception Specialization Roll if they have an applicable sense. Creatures beyond 10 meters need a special sense, Technique, preparation, or circumstance that justifies detection.

Saying “I think it is there” or pointing to a suspected position does not reveal a concealed creature by itself. Communicating suspicion enables area attacks or directed searching, but does not remove penalties or make the position exact.

---

## Uncertain Approximate Position

An action can reveal approximate position without revealing exact position.

Examples: an arrow leaves a patch of shrubs, a stone falls from a ledge, a voice comes from the west, or a shadow crosses behind smoke.

Uncertain approximate position exists so the detector receives a playable clue without knowing whether they were right. The player should know that their character perceived something, but not whether that perception was correct.

### Player hidden, creature detects

If the player is the one concealed:

1. The player rolls the same specialization used to hide, or the appropriate specialization if the fiction changed.
2. The Narrator rolls Perception for the creature trying to detect them.
3. If Perception beats Concealment, the creature locates the character's real position.
4. If Perception does not beat Concealment, the Narrator rolls 1d8 and the creature acts toward the false position indicated by that direction, if its behavior justifies it.

### Creature hidden, player detects

If a creature is the one concealed:

1. The player rolls Perception.
2. The Narrator secretly rolls the creature's Concealment.
3. The Narrator also secretly rolls 1d8 at the same time, declaring only that Concealment is being resolved.
4. If the player's Perception beats Concealment, the Narrator points to the real position.
5. If the player's Perception does not beat Concealment, the Narrator points to the false position indicated by the 1d8.

The Narrator does not declare whether the player's roll succeeded or failed. The point shown is what the character believes they perceived.

Ties favor the concealed creature.

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

On a grid, the 1d8 result points by default to the square adjacent to the concealed creature's real position in that direction. If the creature occupies more than one square, use the adjacent square from the edge of its space in that direction.

If that square is invalid, blocked, or implausible, use the nearest plausible Cover, cell, or area in the same direction. Without a grid, use a credible nearby zone in that direction.

---

## Detecting Concealed Creatures

There is no universal separate action called Search. Searching resolves as a Perception Specialization Roll, a Technique, or a scene-specific action if the Narrator requires one due to time, position, or pressure.

On success, the creature detects the position for itself. It may communicate a suspicion or direction if the scene allows speech, pointing, or coordination, but that communication does not automatically reveal the creature to everyone.

Provoked detection occurs when a concealed creature produces a signal sufficient for others to notice. The Narrator can call for Perception, use a fixed threshold, or reveal partial information if the signal is obvious.

Provoked detection does not replace deliberate use of Perception or Techniques. It resolves signals created by the concealed creature, not free scanning of the entire environment.

---

## Balance Limits

Concealment needs limits because it can become too strong if it prevents too many responses.

Safety rules:

- Hiding requires a physical, environmental, or technical basis;
- Concealment is measured by enemy, not as a universal state;
- hidden does not mean untouchable;
- area effects still work if they cover the real position;
- attacking usually reveals or risks Concealment;
- specialized Perception can accelerate detection, but should not erase the whole signal game;
- creatures with non-visual senses can ignore or reduce visual Concealment;
- abilities, Techniques, or creatures can declare that they ignore Concealment under specific conditions.
