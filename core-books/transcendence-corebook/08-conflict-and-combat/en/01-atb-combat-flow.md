---
title: "ATB: The Combat Flow"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [atb, combat, flow, rhythm, initiative, opening]
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

Each participant occupies a numbered position on that track. On the track is a **flow marker** that records the current moment in combat.

When a creature activates, the flow marker is placed at the number corresponding to its marker. The creature declares its action and moves its marker by paying the rhythm cost. Once the action is resolved, the flow marker advances clockwise to the next closest marker — that creature activates and the process repeats.

The circular track solves the practical problem of an infinite line: markers are never repositioned. They simply advance around the track, and the flow marker always follows the next available marker clockwise.

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

## Flow Resolution

The ATB flow follows this procedure in a loop:

1. The flow marker is placed at the active marker's position.
2. The active creature declares its action. It can use any available action according to the rules for Actions, Techniques, active conditions, and the current state of the scene.
3. The active creature's marker advances by the rhythm cost of the declared action.
4. The action is resolved.
5. The flow marker advances clockwise to the next closest marker.
6. That creature activates and the process repeats.

```text
New position = current position + rhythm cost of the action
```

Combat repeats this procedure until the scene ends.

---

## Tiebreaking

If two or more markers are at the same distance from the flow marker, the participant with the higher Preparation acts first.

If Preparation is also equal, the outcome depends on who is tied:

- **NPC and PC tied:** the Narrator decides who acts first.
- **PCs tied with each other:** the players decide the order among themselves.

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

Reactions also have a rhythm cost. When a creature executes a Reaction, its marker advances from its current position by the rhythm cost of that Reaction.

The full definition of Reactions is found in the Actions chapter.

---

## Example

Two characters begin close to the flow marker.

The first uses Movement to gain cover. That action has rhythm cost `5`, so their marker advances 5 positions around the track.

The second uses a two-handed weapon attack. That action has rhythm cost `7`, so their marker advances 7 positions.

The first character becomes available again sooner because they paid a lower rhythm cost. The second created more immediate pressure, but will take longer to act again.

The circular track records those choices directly, without converting them into fixed rounds.
