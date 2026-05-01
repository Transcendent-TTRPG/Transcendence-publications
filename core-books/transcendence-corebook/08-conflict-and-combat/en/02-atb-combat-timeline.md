---
title: "ATB: The Combat Timeline"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [atb, combat, timeline, rhythm, initiative, actions, rhythm-cost, opening]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/02-atb-linea-de-tiempo.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-actions.md
  - core-books/transcendence-corebook/03-core-rules/en/02-rolling-system-and-competencies.md
authority_refs:
  - Transcendence-design/docs/system/atb-reference.md
  - Transcendence-design/docs/system/mechanics-overview.md
  - Transcendence-design/docs/adr/combat-atb-timeline.md
  - Transcendence-design/docs/adr/combat-atb-rhythm-costs.md
  - Transcendence-design/data/system/atb-combat.yaml
section_modes:
  - heading: "Example"
    writing_mode: example
---

# ATB: The Combat Timeline

Combat is not divided into fixed rounds. Each character, creature, or significant system in the encounter acts according to its own rhythm, its readiness, and the temporal cost of its decisions.

The combat timeline — also called the ATB — represents this directly. Each participant occupies a position on a track. Whoever is furthest to the left acts first.

When an entity acts, its marker moves to the right by the rhythm cost of the chosen action. Acting earlier costs more; delaying an action preserves tempo but surrenders ground.

The ATB exists to answer a simple question:

> Who is ready to act now, and how long will it take them to be ready again?

---

## What the ATB Represents

A marker's position on the track does not represent only "initiative." It represents the time it will take a creature to recover, reorganize, and generate another meaningful action within the combat.

A quick action leaves the creature ready sooner. A heavy or demanding action delays it more.

The track makes this visible in real time:

- who reacts first
- who overcommits
- who forces a very powerful action at the cost of losing tempo
- who manages to act twice before another because their decisions were lighter or more efficient

---

## Combat Opening

When a hostile scene begins, each participant is placed on the track before the first action resolves.

Each participant calculates an Opening Value:

Opening Value = Preparation + situational modifiers

The highest Opening Value among all participants establishes the Reference Point for this encounter. Each participant's initial position is the difference between that Reference Point and their own Opening Value.

The participant with the highest Opening Value starts at position 0 — the leftmost point on the track — and acts first. All others start to the right at a distance equal to the gap between the Reference Point and their own Opening Value.

Situational modifiers represent circumstances such as:

- being alert
- ambushing
- being surprised
- being poorly positioned
- having a weapon ready
- being distracted, wounded, or reorganizing

The combat opening is not a separate system from the track. It is the track's starting state. Rhythm costs stack on top of it from the first activation onward.

---

## The Timeline

Once the opening is resolved, combat enters the full ATB flow.

Three principles govern it:

- The leftmost marker acts first.
- After acting, that marker moves to the right.
- The distance it moves is the action's rhythm cost.

The order is not fixed from the start. It adjusts with every activation.

A character who uses quick, efficient actions can act again sooner. One who overextends with a very heavy maneuver will take longer to recover their next opportunity.

---

## Tiebreaking

If two or more markers occupy the same leftmost position, whoever has the higher Preparation acts first.

If Preparation is also tied, each participant makes a contested Agility Characteristic Roll. The higher result acts first.

---

## Rhythm Cost

Every significant action has a rhythm cost. That cost indicates how much it delays the next opportunity to act.

Rhythm cost is not the same as Attrition:

- Rhythm responds to how long it takes you to act again.
- Attrition responds to how much accumulated strain that action leaves on your body, mind, and composure.

A more demanding action often commits more in both dimensions — but not always in equal measure.

An action can be:

- quick but demanding
- slow but stable
- efficient for a trained character
- costly for one who has not developed that skill

---

## Action Bands

Every action has a rhythm cost — the number of positions its marker moves right after resolving.

| Band | Rhythm cost |
| --- | ---: |
| Free action | 0 |
| Quick action | 3 |
| Standard action | 5 |
| Heavy action | 7 |
| Extreme action | 9 |

Rhythm cost 0 means the marker does not move. The creature holds its position and the next activation in line proceeds. Free actions are constrained by scope: Drop and Speak qualify within limits defined in the action rules.

Extreme actions are not available at the base layer. They appear through Techniques.

### Base action families

These costs apply when no specific ability, training, or competency bonus modifies them.

| Action | Rhythm cost | Attrition |
| --- | ---: | ---: |
| Free action (drop, speak) | 0 | 0 |
| Interact | 3 | 1 * |
| Move | 5 | 1 |
| Hide | 5 | 1 |
| Specialization | 5 | 1 |
| Attack with one-handed weapon | 5 | 1 |
| Attack with two-handed weapon | 7 | 1 |
| Attack with two one-handed weapons | 7 | 1 |

\* Attrition cost applies only under real scene pressure. Trivial interactions generate 0.

Hide uses standard rhythm because it requires creating or exploiting a real opening, adjusting position, controlling signals, and resolving whether enemies lose precise localization. It cannot be declared without cover, reduced visibility, distraction, preparation, or a specific rule that allows it.

Terrain does not change rhythm cost. Terrain affects distance covered, required checks, and consequences of movement.

---

## Reactions

Reactions exist within the same timing economy as every other action. Even though they occur outside the character's planned activation, they carry a rhythm cost, an Attrition cost, and advance the marker on the track.

The advantage of a Reaction is not that it is free — it is that it allows the character to intervene now rather than waiting for the next normal activation.

The full definition of Reactions — what triggers them, when they are declared, and how they are used — is found in the Actions chapter.

---

## Movement and ATB

Movement is not a separate invisible layer. Displacement is part of the scene's rhythm and carries its own rhythm cost.

That cost is fixed: Movement always occupies the Standard band of the ATB. Moving to escape a breath attack, reach an advantageous position, or intercept a charge costs the same on the track — what varies is not the time it takes to decide to move, but what that movement can achieve.

Terrain does not modify the rhythm cost. What terrain changes is:

- the distance the character can cover
- whether the path requires a roll
- the consequences or hazards of the displacement

Position determines what is possible. That is the tactical value of Movement within the ATB.

---

## Example

Two characters begin the encounter near the same point on the timeline. One chooses a quick reposition to secure cover; the other commits to a heavier action with greater payoff. The first acts again sooner because the rhythm cost paid was lower. The second creates more immediate pressure, but returns later on the track. The timeline records those choices directly instead of converting them into abstract rounds.
