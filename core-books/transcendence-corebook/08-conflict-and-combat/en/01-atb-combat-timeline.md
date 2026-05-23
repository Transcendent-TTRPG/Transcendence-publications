---
title: "ATB: The Combat Flow"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [atb, combat, timeline, rhythm, initiative, opening]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-atb-flujo-temporal.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-actions.md
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

# ATB: The Combat Flow

Combat is not divided into fixed rounds. Each creature acts according to its position in the combat flow, its Preparation, and the rhythm cost of its actions.

The **ATB** — the Combat Flow — represents when a creature is ready to act and how long it takes to become ready again.

The ATB answers two questions:

> Who acts now?  
> How long until they act again?

---

## The Temporal Flow

The ATB is represented as a **circular track**.

Each participant occupies a position on that track. At the center of the track is a **flow marker** that indicates the current moment in combat. The marker closest to the flow marker is the next to act.

When a creature acts, its marker advances around the track according to the rhythm cost of the chosen action. The flow marker shifts to the next active marker. The flow continues without resetting.

The circular track solves the practical problem of an infinite line: markers are never repositioned. They simply advance around the track, and the flow marker follows the closest one.

The track shows:

- who acts first
- who acts again sooner
- who overcommits
- who gains tempo through lighter actions

The combat order is not fixed at the beginning. It changes with every activation.

---

## Combat Opening

When a hostile scene begins, each participant receives an initial position on the ATB.

To do this, each participant calculates their **Opening Value**.

```text
Opening Value = Preparation + situational modifiers
```

The highest Opening Value among all participants establishes the encounter's **Reference Point**.

```text
Reference Point = highest Opening Value in the encounter
```

Each participant's initial position is calculated with this formula:

```text
Initial position = Reference Point − participant's Opening Value
```

The participant with the highest Opening Value starts at position `0`, the point closest to the flow marker. That participant acts first.

All other participants start farther from the marker, at a distance equal to the difference between the Reference Point and their own Opening Value.

The combat opening is not a separate system from the ATB. It only defines the track's starting state. From the first activation onward, rhythm costs apply normally.

---

## Situational Modifiers

Situational modifiers represent advantages or disadvantages at the start of combat.

They may include:

- being alert
- ambushing
- being surprised
- having a weapon ready
- being distracted
- being wounded
- being poorly positioned
- reorganizing
- starting from an advantageous position

The Narrator assigns these modifiers according to the fiction of the scene.

---

## Opening Example

Three creatures begin an encounter.

| Participant | Preparation | Modifier | Opening Value |
| --- | ---: | ---: | ---: |
| Explorer | 4 | +1 | 5 |
| Beast | 3 | 0 | 3 |
| Custodian | 2 | -1 | 1 |

The highest Opening Value is `5`, so the Reference Point is `5`.

| Participant | Calculation | Initial position |
| --- | --- | ---: |
| Explorer | 5 − 5 | 0 |
| Beast | 5 − 3 | 2 |
| Custodian | 5 − 1 | 4 |

The Explorer acts first because their marker is closest to the flow marker. The Beast starts at distance `2`. The Custodian starts at distance `4`.

---

## Activation

A creature activates when its marker is closest to the flow marker.

During its activation, it can take an available action according to the rules for Actions, Techniques, active conditions, and the current state of the scene.

After the action is resolved, its marker advances around the track.

```text
New position = current position + rhythm cost of the action
```

A quick action moves the marker a short distance. A heavy action moves it farther.

---

## Flow Resolution

The ATB flow follows this procedure in a loop:

1. The flow marker points to the closest marker.
2. That creature acts.
3. It resolves its action.
4. Its marker advances by the rhythm cost of the chosen action.
5. The flow marker shifts to the next closest marker.

Combat repeats this procedure until the scene ends.

---

## Tiebreaking

If two or more markers are at the same distance from the flow marker, the participant with the higher Preparation acts first.

If Preparation is also tied, each tied participant makes a contested Agility Characteristic Roll.

The highest result acts first.

If the tie remains, the Narrator decides according to position, the fiction of the scene, or any clear situational advantage.

---

## Rhythm Cost

Every significant action has a **rhythm cost**.

This cost indicates how far the marker advances on the track after the action is taken.

Rhythm cost is not the same as Attrition.

| Concept | What it measures |
| --- | --- |
| Rhythm | How long the creature takes to act again |
| Attrition | How much accumulated pressure the action leaves on body, mind, or composure |

An action can be quick but exhausting. It can also be slow without generating much Attrition.

Rhythm organizes time. Attrition records the internal cost of sustaining action.

---

## Action Bands

Every action has a rhythm cost. That number indicates how many positions the marker advances after the action is resolved.

| Band | Rhythm cost |
| --- | ---: |
| Free action | 0 |
| Quick action | 3 |
| Standard action | 5 |
| Heavy action | 7 |
| Extreme action | 9 |
| Variable | Defined by the rule, Technique, or effect |

Extreme actions are not available as base actions. They appear through Techniques, special effects, or specific rules.

An action with cost `0` does not advance the marker. Free Actions remain subject to the limits defined in the Actions chapter.

The specific costs for each base action are in the Actions chapter.

---

## Reactions and ATB

Reactions exist within the same temporal economy as every other action.

Even though they occur outside a creature's normal activation, they may have:

- rhythm cost
- Attrition cost
- effects on the marker's future position

If a Reaction has a rhythm cost, the creature's marker advances from its current position.

```text
New position = current position + rhythm cost of the Reaction
```

The advantage of a Reaction is not that it is free. Its advantage is that it allows the creature to intervene before its next normal activation.

A creature can only use a Reaction when a rule, Technique, maneuver, trait, or specific situation allows it.

The full definition of Reactions is found in the Actions chapter.

---

## Example

Two characters begin close to the flow marker.

The first uses Movement to gain cover. That action has rhythm cost `5`, so their marker advances 5 positions around the track.

The second uses a two-handed weapon attack. That action has rhythm cost `7`, so their marker advances 7 positions.

The first character becomes available again sooner because they paid a lower rhythm cost. The second created more immediate pressure, but will take longer to act again.

The circular track records those choices directly, without converting them into fixed rounds.
