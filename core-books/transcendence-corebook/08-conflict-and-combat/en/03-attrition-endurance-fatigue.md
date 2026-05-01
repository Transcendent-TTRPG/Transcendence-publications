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
  - heading: "Example of thresholds"
    writing_mode: example
---

# Attrition, Endurance, and Fatigue

Combat and high-tension scenes do not only put a character's life at risk — they also wear down their body, mind, and composure. Acting under pressure has a cost. That cost is tracked through the Attrition, Endurance, and Fatigue system.

This system does not replace damage or the activation order. It tracks how much effort a character can sustain before they begin to deteriorate.

Attrition represents the accumulated burden of acting under pressure.
Endurance represents how much of that burden a character can bear.
Fatigue represents the deterioration that appears when Attrition exceeds its limits.

A character can keep fighting, analyzing, resisting, and reacting for a time — but not indefinitely.

---

## Attrition

Attrition is the accumulated burden a character bears when executing meaningful actions in a hostile scene.

It does not represent direct physical damage. Nor is it an exclusive measure of muscular exhaustion. Attrition includes everything that forces a character to keep performing under tension: physical effort, concentration, tactical reading, emotional control, and immediate response in the face of danger.

A character can accumulate Attrition from:

- attacking, defending, or moving in combat
- reacting to sudden threats
- analyzing a creature under pressure
- sustaining a demanding maneuver
- applying mental or social pressure in the middle of a conflictive scene
- acting while suffering adverse conditions or environmental pressure

Not every action generates Attrition. Only those that demand real effort and carry weight within the scene do.

---

## Endurance

Endurance represents a character's capacity to keep functioning before they begin suffering Fatigue.

Every character has a minimum reserve of functionality across three planes of conflict:

- the **body**, which sustains effort, impact, and movement
- the **mind**, which sustains attention, reading, and interpretation
- **composure**, which sustains control, intent, and clarity under tension

Every character starts with a Base Endurance Reserve of 3. To that base is added the character's final physical resilience, expressed through Tenacity.

### Endurance Formula

Endurance = 3 + (Tenacity × 2)

Endurance depends on two things:

- natural capacity to bear effort (Tenacity)
- a universal minimum representing continued function across body, mind, and composure

### Example

A character with final Tenacity 2 after applying their starting Tenacity Synapsis has:

Endurance = 3 + (2 × 2) = 7

---

Every character begins with one starting Tenacity specialization at Level 1 / Rank 1: March, Acclimation, or Tolerance. Operating under serious pressure requires some trained form of resilience, but not the same expression for every character.

---

## Fatigue

Fatigue is the progressive deterioration that appears when a character accumulates more Attrition than they can sustain.

It does not arise from a single isolated action, but from accumulation. As Attrition increases, the character begins to lose effectiveness. Maintaining precision becomes harder. Sustaining their pace grows more difficult. Clarity is harder to preserve. Responses come with less firmness.

Fatigue does not represent only physical exhaustion. It can also reflect:

- bodily saturation
- cognitive overload
- loss of composure
- increasing difficulty sustaining the same level of performance

### Projected Fatigue and Settled Fatigue

During a hostile scene, a character can keep acting even after accumulating considerable Attrition. For this reason, the system distinguishes between two distinct moments:

#### Projected Fatigue

While the combat or dangerous situation remains active, the player tracks how much Attrition has been accumulated and can see what level of Fatigue the character would suffer if the scene ended at that moment.

This does not mean the full penalty applies immediately. It means the character is already pushing their margin — and that if they continue, they will leave the scene in worse condition.

#### Settled Fatigue

When the hostile scene ends or clearly drops in intensity, adrenaline stops artificially sustaining performance. At that moment, Projected Fatigue becomes real Fatigue and its effects are applied.

- During combat, Fatigue is projected.
- When combat ends, Fatigue settles.

### Fatigue Thresholds

Fatigue is determined by comparing the character's accumulated Attrition against their Endurance.

| Level | Condition |
| --- | --- |
| Fatigue 0 | Attrition is less than Endurance |
| Fatigue 1 | Attrition is equal to or greater than Endurance |
| Fatigue 2 | Attrition is equal to or greater than 2 × Endurance |
| Fatigue 3 | Attrition is equal to or greater than 3 × Endurance |
| Fatigue 4 | Attrition is equal to or greater than 4 × Endurance |
| Fatigue 5 | Attrition is equal to or greater than 5 × Endurance |

### Example of thresholds

If a character has Endurance 7:

- Attrition 0 to 6 → no Fatigue
- Attrition 7 to 13 → Fatigue 1
- Attrition 14 to 20 → Fatigue 2
- Attrition 21 to 27 → Fatigue 3
- Attrition 28 to 34 → Fatigue 4
- Attrition 35 or more → Fatigue 5

The base scale does not exceed Fatigue 5. If a rule adds Fatigue while the character is already at Fatigue 5, the character becomes Incapacitated by exhaustion.

A character Incapacitated by exhaustion cannot take Active Actions, Reactions, or Techniques. They must begin resting as soon as the scene allows it. If the environment prevents rest, they need help, shelter, transport, or a specific rule to avoid being taken out of action.

Fatigue 5 is not a tactical margin that can be sustained voluntarily. It is the final point before operational collapse.

---

## Carrying Capacity

Sustained load does not use scene Attrition when measured as prolonged travel, exploration, transport, or physical work. In that case, it generates Fatigue directly over time.

Carrying capacity depends on creature size, Strength, and Tenacity.

To prevent a character with Strength 0 or Tenacity 0 from having capacity 0, use minimum effective values:

```text
Effective Strength = minimum 1
Effective Tenacity = minimum 1
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

Load type is determined by the percentage of that capacity being used.

| Load type | Weight carried | Sustained load Fatigue |
| --- | --- | --- |
| Light Load | Up to 50% of capacity | No automatic Fatigue. |
| Medium Load | More than 50% and up to 75% | +1 Fatigue level every 2 hours. |
| Heavy Load | More than 75% and up to 100% | +1 Fatigue level every 1 hour. |

A load above 100% capacity cannot be carried functionally without help, equipment, Technique, pack creature, or a specific rule.

Sustained load Fatigue does not check Attrition thresholds. It is added directly over time. If a new application of sustained load would push the character beyond Fatigue 5, they become Incapacitated by exhaustion and must rest or receive help.

---

## Attrition Costs

Not all actions generate the same level of burden. To reflect this, the system uses a simple cost scale.

### Attrition Scale

| Cost | Action type |
| --- | --- |
| 0 | action with no real demand |
| 1 | standard meaningful action |
| 2 | high-demand action |
| 3 | extreme or overextension action |

### 0 Attrition

Trivial or purely narrative actions that impose no real effort within the scene.

Examples:

- an obvious observation
- a brief remark with no tactical weight
- a minor action with no immediate threat

### 1 Attrition

Standard meaningful actions.

Examples:

- a standard attack
- a simple defense
- a significant movement under pressure
- an active observation of the enemy
- a basic reading of a creature's behavior

### 2 Attrition

High-demand actions.

Examples:

- intercepting a charge
- protecting another character by absorbing pressure
- deeply analyzing an enemy in the middle of combat
- executing a maneuver that genuinely changes the rhythm of the scene
- using a mental or social action that removes an important advantage

### 3 Attrition

Extreme or overextension actions.

Examples:

- a limit-effort when the character is already under heavy pressure
- a heroic intervention clearly beyond their safe margin
- an especially demanding maneuver that forces the character beyond their normal pace

---

## Physical, Mental, and Social Actions

Attrition does not depend on the type of attribute used — it depends on the real demand of the action.

A mental or social action generates Attrition if it:

- requires genuine focus under threat
- alters the tactical situation
- competes with other important combat actions
- forces the character to sustain reading, control, or pressure in the middle of chaos

Not every mental or social action generates Attrition. Those that provide a real advantage or impose a meaningful burden under pressure do.

Reading a creature, breaking its pattern, forcing a reaction, or destabilizing its behavior can cost as much as attacking or defending — when the situation warrants it.

---

## Reactions and Attrition

Reactions are not costly because they are reactions — they are costly because of the demand they typically imply.

Responding outside a character's natural rhythm usually requires more precision, tension, and speed. For this reason, a reaction may cost more or less Attrition depending on how difficult it is to execute.

- a simple reaction may cost 1
- a demanding reaction may cost 2
- a limit reaction may cost 3

What matters is not its category, but its intensity within the scene.
