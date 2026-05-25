---
title: "Attrition, Endurance, and Fatigue"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [attrition, endurance, fatigue, combat, strain, fatigue-thresholds]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-desgaste-aguante-fatiga.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/04-rest.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-actions.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/05-wounds-and-damage.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/01-specializations.md
authority_refs:
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/docs/system/mechanics-overview.md
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/data/system/attrition-fatigue.yaml
  - Transcendence-design/data/system/specializations.yaml
section_modes:
  - heading: "Example"
    writing_mode: example
  - heading: "Example of Thresholds"
    writing_mode: example
---

# Attrition, Endurance, and Fatigue

Combat and high-pressure scenes do not only threaten a character’s life. They also wear down the body, mind, and composure.

This system uses three values:

| Value | What it represents |
| --- | --- |
| **Attrition** | The accumulated burden of acting under pressure |
| **Endurance** | How much Attrition the character can sustain before deteriorating |
| **Fatigue** | The deterioration that appears when Attrition exceeds Endurance |

Attrition does not replace damage. It also does not replace activation order. It tracks how much effort a character can continue to sustain before their performance begins to break.

---

## Attrition

**Attrition** is the accumulated burden a character bears when performing meaningful actions in a hostile or high-pressure scene.

It does not represent direct physical damage. It also includes physical effort, concentration, tactical reading, emotional control, and immediate response to danger.

A character can accumulate Attrition from:

- attacking, defending, or moving in combat
- reacting to sudden threats
- sustaining a demanding maneuver
- analyzing a creature under pressure
- applying mental or social pressure in a conflictive scene
- acting while suffering adverse conditions or environmental pressure

Not every action generates Attrition. Only actions that demand real effort and carry weight within the scene do.

---

## Attrition Costs

Actions use a simple cost scale.

| Cost | Action type |
| ---: | --- |
| 0 | Action with no real demand |
| 1 | Standard meaningful action |
| 2 | High-demand action |
| 3 | Extreme or overextension action |

---

### 0 Attrition

Trivial or purely narrative actions that impose no real effort within the scene.

Examples:

- an obvious observation
- a brief remark with no tactical weight
- a minor action with no immediate threat

---

### 1 Attrition

Standard meaningful actions.

Examples:

- a standard attack
- a simple defense
- significant movement under pressure
- active observation of an enemy
- a basic reading of a creature’s behavior

---

### 2 Attrition

High-demand actions.

Examples:

- intercepting a charge
- protecting another character by absorbing pressure
- deeply analyzing an enemy during combat
- executing a maneuver that changes the rhythm of the scene
- using a mental or social action that removes an important advantage

---

### 3 Attrition

Extreme or overextension actions.

Examples:

- a limit effort while the character is already under heavy pressure
- a heroic intervention beyond the character’s safe margin
- an especially demanding maneuver that forces the character beyond their normal rhythm

---

## Physical, Mental, and Social Actions

Attrition does not depend on the type of characteristic used. It depends on the real demand of the action.

A mental or social action can generate Attrition if it:

- requires real focus under threat
- changes the tactical situation
- competes with other important combat actions
- forces the character to sustain reading, control, or pressure in the middle of chaos

Not every mental or social action generates Attrition. Only those that provide a real advantage or impose a meaningful burden under pressure do.

Reading a creature, breaking its pattern, forcing a reaction, or destabilizing its behavior can cost as much as attacking or defending, if the situation warrants it.

---

## Reactions and Attrition

Reactions are not costly because they are Reactions. They are costly because of the demand they imply.

Responding outside a character’s natural rhythm usually requires precision, tension, and speed. For that reason, a Reaction may cost more or less Attrition depending on how difficult it is to execute.

| Reaction type | Suggested Attrition |
| --- | ---: |
| Simple Reaction | 1 |
| Demanding Reaction | 2 |
| Limit Reaction | 3 |

What matters is not the action category, but its intensity within the scene.

---

## Endurance

**Endurance** represents how much accumulated burden a character can sustain before beginning to suffer Fatigue.

Every character has a minimum reserve of function. This reserve covers three planes of conflict:

- the **body**, which sustains effort, impact, and movement
- the **mind**, which sustains attention, reading, and interpretation
- **composure**, which sustains control, intent, and clarity under pressure

Every character has a base Endurance reserve of `3`. To that base, add the character’s final bodily resistance, expressed through Tenacity.

```text
Endurance = 3 + (Tenacity × 2)
```

The Tenacity used in this formula is the character’s final Tenacity, after applying species and Synapsis.

Every character begins with one starting Tenacity specialization at level 1, Novice rank: **March**, **Acclimation**, or **Tolerance**. That specialization is already included indirectly in Endurance because it increases Tenacity through Synapsis during character creation.

---

## Example

A character finishes creation with Tenacity `2`.

```text
Endurance = 3 + (2 × 2)
Endurance = 7
```

That character has Endurance `7`.

---

## Fatigue

**Fatigue** is the progressive deterioration that appears when a character accumulates more Attrition than they can sustain.

It does not come from a single isolated action. It comes from accumulation.

As Attrition increases, it becomes harder for the character to maintain precision, keep pace, preserve clarity, or respond with firmness.

Fatigue can reflect:

- bodily saturation
- cognitive overload
- loss of composure
- difficulty sustaining the same performance
- general deterioration after a demanding scene

---

## Projected Fatigue and Settled Fatigue

Fatigue is handled in two moments: while the scene is still active, and when the scene ends.

---

### Projected Fatigue

During a hostile scene, the character tracks accumulated Attrition and calculates what Fatigue level they would suffer if the scene ended at that moment.

That Fatigue is still **projected**.

This means the character is pushing their margin, but the full penalty does not settle while adrenaline, urgency, or immediate danger continue to support performance.

During combat, Fatigue is projected.

---

### Settled Fatigue

When the hostile scene ends or clearly drops in intensity, Projected Fatigue becomes real Fatigue.

At that moment:

1. Check accumulated Attrition.
2. Determine the Fatigue level reached.
3. Apply that level as Settled Fatigue.
4. Clear the accumulated Attrition from that scene, unless a specific rule says otherwise.

When combat ends, Fatigue settles.

---

## Fatigue Thresholds

Fatigue is determined by comparing accumulated Attrition with the character’s Endurance.

| Level | Condition |
| --- | --- |
| Fatigue 0 | Attrition is lower than Endurance |
| Fatigue 1 | Attrition is equal to or greater than Endurance |
| Fatigue 2 | Attrition is equal to or greater than 2 × Endurance |
| Fatigue 3 | Attrition is equal to or greater than 3 × Endurance |
| Fatigue 4 | Attrition is equal to or greater than 4 × Endurance |
| Fatigue 5 | Attrition is equal to or greater than 5 × Endurance |

The base scale does not exceed Fatigue 5.

If a mechanic adds Fatigue while the character is already at Fatigue 5, the character becomes **Incapacitated by exhaustion**.

---

## Example of Thresholds

If a character has Endurance `7`:

| Accumulated Attrition | Projected or Settled Fatigue |
| ---: | ---: |
| 0–6 | Fatigue 0 |
| 7–13 | Fatigue 1 |
| 14–20 | Fatigue 2 |
| 21–27 | Fatigue 3 |
| 28–34 | Fatigue 4 |
| 35 or more | Fatigue 5 |

Fatigue 5 is not a tactical margin that can be sustained voluntarily. It is the final point before operational collapse.

---

## Fatigue Effects

Fatigue effects are **cumulative**. Reaching Fatigue 3 means the character is under the effects of Fatigue 1, 2, and 3 simultaneously. Each level closes off or increases the cost of something distinct — it is not simply more of the same modifier.

| Level | Effect |
| --- | --- |
| **Fatigue 1** | Physical `S.R.` rolls require a successful `R.R.` Tenacity before execution. On failure, the `S.R.` is lost. |
| **Fatigue 2** | Actions with a rhythm cost of `5` or higher are not available. |
| **Fatigue 3** | All non-free actions cost `+1` additional Attrition. |
| **Fatigue 4** | Reactions are not available. Only Active Actions can be taken. |
| **Fatigue 5** | Techniques resolve only their primary effect (`A.R.`, `I.R.`, or base utility effect). Free repositioning, applied Alterations, and position control do not activate. |

If a mechanic adds Fatigue while the character is already at Fatigue 5, the character becomes **Incapacitated**.

---

## Incapacitated by Exhaustion

A character **Incapacitated by exhaustion** cannot take:

- Active Actions
- Reactions
- Techniques

They must begin resting as soon as the scene allows it.

If the environment prevents rest, they need help, shelter, transport, or a specific rule to avoid being removed from action.

---

## Carrying Capacity

Sustained load does not use scene Attrition when measured as prolonged travel, exploration, transport, or physical work.

In those cases, it generates Fatigue directly over time.

Carrying capacity depends on three factors:

- creature size
- Strength
- Tenacity

To prevent a character with Strength `0` or Tenacity `0` from having capacity `0`, use minimum effective values.

```text
Effective Strength = max(Strength, 1)
Effective Tenacity = max(Tenacity, 1)
Carrying capacity = Effective Strength × Effective Tenacity × size multiplier
```

| Size | Carrying capacity |
| --- | --- |
| Tiny | Effective Strength × Effective Tenacity × 1 kg |
| Small | Effective Strength × Effective Tenacity × 15 kg |
| Medium | Effective Strength × Effective Tenacity × 35 kg |
| Large | Effective Strength × Effective Tenacity × 80 kg |
| Huge | Effective Strength × Effective Tenacity × 200 kg |
| Gigantic | Effective Strength × Effective Tenacity × 800 kg |

---

## Load Type

Load type is determined by the percentage of total capacity being used.

| Load type | Weight carried | Sustained load Fatigue |
| --- | --- | --- |
| Light Load | Up to 50% of capacity | Does not generate automatic Fatigue |
| Medium Load | More than 50% and up to 75% | +1 Fatigue level every 2 hours |
| Heavy Load | More than 75% and up to 100% | +1 Fatigue level every 1 hour |

A load above `100%` of capacity cannot be carried functionally without help, equipment, Technique, pack creature, or a specific rule.

Sustained load Fatigue does not check Attrition thresholds. It is added directly over time.

If a new application of sustained load Fatigue would push the character beyond Fatigue 5, they become **Incapacitated by exhaustion**.

---

## Quick Summary

| Element | Rule |
| --- | --- |
| Attrition | Accumulates from meaningful actions under pressure |
| Endurance | `3 + (Tenacity × 2)` |
| Projected Fatigue | Calculated during the scene, but not settled yet |
| Settled Fatigue | Applied when the hostile scene ends or intensity drops |
| Fatigue 1 | Attrition equal to or greater than Endurance |
| Fatigue 5 | Maximum base Fatigue level |
| Beyond Fatigue 5 | Incapacitated by exhaustion |
| Sustained load | Adds Fatigue directly over time, not through Attrition thresholds |

---

## Example

A creature with Endurance `7` participates in a long combat.

During the scene, it accumulates `15` points of Attrition. While combat remains active, that Fatigue is projected.

```text
Endurance = 7
Accumulated Attrition = 15
Projected Fatigue = 2
```

The character continues acting while the scene continues, unless another rule says otherwise.

When combat ends, Fatigue settles. The character receives Fatigue 2 and clears the accumulated Attrition from that scene.

If they rest later, they can reduce Fatigue according to the Rest rules.
