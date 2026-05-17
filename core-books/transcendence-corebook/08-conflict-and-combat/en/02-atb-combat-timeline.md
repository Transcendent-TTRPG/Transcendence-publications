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

Combat is not divided into fixed rounds. Each creature acts according to its position on the timeline, its Preparation, and the rhythm cost of its actions.

The combat timeline, or **ATB**, represents when a creature is ready to act and how long it takes to become ready again.

Each participant occupies a position on a track. The marker furthest to the left acts first. After acting, that marker advances to the right according to the rhythm cost of the chosen action.

The ATB answers two questions:

> Who acts now?  
> How long until they act again?

---

## What the ATB Represents

A marker’s position on the track does not represent only initiative. It represents the time a creature needs to recover, reorganize, and generate another meaningful action.

A quick action leaves the creature available sooner. A heavy action delays it more.

The track shows:

- who acts first
- who acts again sooner
- who overcommits
- who delays their next opportunity through a heavy action
- who gains tempo through lighter actions

The combat order is not fixed at the beginning. It changes with every activation.

---

## Combat Opening

When a hostile scene begins, each participant receives an initial position on the ATB.

To do this, each participant calculates their **Opening Value**.

```text
Opening Value = Preparation + situational modifiers
```

The highest Opening Value among all participants establishes the encounter’s **Reference Point**.

```text
Reference Point = highest Opening Value in the encounter
```

Each participant’s initial position is calculated with this formula:

```text
Initial position = Reference Point - participant's Opening Value
```

The participant with the highest Opening Value starts at position `0`, the leftmost point on the track. That participant acts first.

All other participants start to the right, at a distance equal to the difference between the Reference Point and their own Opening Value.

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

The combat opening is not a separate system from the ATB. It only defines the track’s starting state. From the first activation onward, rhythm costs apply normally.

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
| Explorer | 5 - 5 | 0 |
| Beast | 5 - 3 | 2 |
| Custodian | 5 - 1 | 4 |

The Explorer acts first because they are at position `0`. The Beast starts at position `2`. The Custodian starts at position `4`.

---

## ATB Flow

Once the opening is resolved, combat follows the normal ATB flow.

To resolve order:

1. The leftmost marker acts.
2. The creature resolves its action.
3. The marker advances to the right by the rhythm cost of that action.
4. Check again which marker is now furthest to the left.
5. That marker acts next.

Combat repeats this procedure until the scene ends.

---

## Activation

A creature activates when its marker is furthest to the left on the track.

During its activation, it can take an available action according to the rules for Actions, Techniques, active conditions, and the current state of the scene.

After the action is resolved, its marker advances to the right.

```text
New position = current position + rhythm cost of the action
```

A quick action moves the marker a short distance. A heavy action moves it farther.

---

## Tiebreaking

If two or more markers occupy the same leftmost position, the participant with the higher Preparation acts first.

If Preparation is also tied, each tied participant makes a contested Agility Characteristic Roll.

The highest result acts first.

If the tie remains, the Narrator decides according to position, the fiction of the scene, or any clear situational advantage.

---

## Rhythm Cost

Every significant action has a **rhythm cost**.

This cost indicates how much the action delays the creature’s next opportunity to act.

Rhythm cost is not the same as Attrition.

| Concept | What it measures |
| --- | --- |
| Rhythm | How long the creature takes to act again |
| Attrition | How much accumulated pressure the action leaves on body, mind, or composure |

An action can be quick but exhausting. It can also be slow without generating much Attrition.

Rhythm organizes time. Attrition records the internal cost of sustaining action.

---

## Action Bands

Every action has a rhythm cost. That number indicates how many positions the marker advances to the right after the action is resolved.

| Band | Rhythm cost |
| --- | ---: |
| Free action | 0 |
| Quick action | 3 |
| Standard action | 5 |
| Heavy action | 7 |
| Extreme action | 9 |
| Variable | Defined by the rule, Technique, or effect |

Extreme actions are not available as base actions. They appear through Techniques, special effects, or specific rules.

An action with cost `0` does not advance the marker. This does not mean it can be used without limit. Free Actions remain subject to the limits defined in the Actions chapter.

---

## Base Actions and Rhythm

These costs apply when no Technique, specific rule, condition, or bonus modifies them.

| Action | Rhythm cost | Base Attrition |
| --- | ---: | ---: |
| Free action: drop, speak briefly | 0 | 0 |
| Interact | 3 | 0 or 1 |
| Move | 5 | 1 |
| Hide | 6 | 1 |
| Use Specialization | 6 | 1 |
| Attack with natural weapon | 6 | 1 |
| Attack with one-handed weapon | 6 | 1 |
| Attack with two-handed weapon | 7 | 1 |
| Attack with two weapons | 8 | 1 |
| Use Technique | Variable | Variable |

Interact only generates Attrition when the interaction occurs under real scene pressure. A trivial interaction with no immediate risk generates `0` Attrition.

---

## Actions with Cost 0

An action with rhythm cost `0` does not move the marker on the ATB.

This applies to brief actions such as dropping an object or saying a short phrase, within the limits defined in the Actions chapter.

Cost `0` does not make an action unlimited. If a Free Action changes the scene in a meaningful way, replaces an Active Action, or is repeated to create advantages without cost, the Narrator may assign rhythm cost, Attrition, or both.

---

## Reactions and ATB

Reactions exist within the same temporal economy as every other action.

Even though they occur outside a creature’s normal activation, they may have:

- rhythm cost
- Attrition cost
- effects on the marker’s future position

If a Reaction has a rhythm cost, the creature’s marker advances from its current position.

```text
New position = current position + rhythm cost of the Reaction
```

The advantage of a Reaction is not that it is free. Its advantage is that it allows the creature to intervene now, before its next normal activation.

A creature can only use a Reaction when a rule, Technique, maneuver, trait, or specific situation allows it.

The full definition of Reactions is found in the Actions chapter.

---

## Movement and ATB

Movement is not a separate layer from combat. It is part of the scene’s rhythm and has its own cost.

Moving always occupies the Standard band of the ATB.

```text
Movement = rhythm cost 5
```

Moving to escape a breath attack, reach cover, close distance, or intercept a charge costs the same on the track. What changes is what that movement achieves.

Terrain does not modify rhythm cost. Terrain can modify:

- distance covered
- required rolls
- consequences of the path
- hazards crossed

Position determines what is possible. That is the tactical value of Movement within the ATB.

---

## Hide and ATB

Hide uses a value above standard rhythm because it requires a real opening and
changes tactical information state within the scene.

```text
Hide = rhythm cost 6
```

To hide, the character must create or exploit a situation that allows them to break the enemies’ precise localization.

Hide cannot be declared without cover, reduced visibility, distraction, preparation, or a specific rule that allows it.

The full rules for Concealment, approximate position, and detection are found in **Cover, Visibility, and Concealment**.

---

## Techniques and Variable Costs

Techniques can modify the normal flow of the ATB.

A Technique can:

- use a different rhythm cost
- reduce or increase Attrition
- function as a Reaction
- create an exception to the normal order
- move markers
- alter a creature’s position on the track

When a Technique contradicts a general ATB rule, the specific rule of the Technique applies.

---

## Example

Two characters begin near the same point on the timeline.

The first uses Movement to gain cover. That action has rhythm cost `5`, so their marker advances 5 positions.

The second uses a two-handed weapon attack. That action has rhythm cost `7`, so their marker advances 7 positions.

The first character becomes available again sooner because they paid a lower rhythm cost. The second created more immediate pressure, but will take longer to act again.

The timeline records those choices directly, without converting them into fixed rounds.
