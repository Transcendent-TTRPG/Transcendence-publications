---
title: "Rest"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [rest, short-rest, full-rest, attrition, recovery, afflictions, maintenance]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/04-descanso.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-attrition-endurance-fatigue.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/05-wounds-and-damage.md
authority_refs:
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/docs/system/wounds-and-damage.md
  - Transcendence-design/docs/system/mechanics-overview.md
  - Transcendence-design/data/system/attrition-fatigue.yaml
  - Transcendence-design/data/system/wounds-and-damage.yaml
section_modes:
  - heading: "Example"
    writing_mode: example
---

# Rest

Rest is the primary way a character recovers control after a demanding scene.

A combat, a chase, a hostile traverse, or an intense confrontation leaves more than visible Wounds. It also leaves heavy breathing, tension, mental saturation, loss of composure, and Fatigue.

Resting does not reset a character. It restores part of the margin they lost.

Rest serves four functions:

- reduce Fatigue
- allow Wound treatment
- allow maintenance, repair, and preparation
- give the group space to reorganize before returning to danger

Not all rest offers the same recovery. A brief pause can return some control, but it can also expose the group to interruption. A long rest allows deeper recovery, but it requires time, adequate conditions, and relative safety.

---

## Rest, Attrition, and Fatigue

During a hostile scene, the character accumulates **Attrition**.

While the scene remains active, that Attrition may complete **Endurance** thresholds and translate into **Projected Fatigue**. The Attrition boxes used to complete each threshold are cleared at that moment. If any Attrition boxes remain that do not reach a new threshold, they stay marked as leftover Attrition.

When the scene ends or clearly drops in intensity, Projected Fatigue becomes Settled Fatigue. Leftover Attrition that did not become Projected Fatigue is not cleared by default: it stays marked and becomes the starting point for the next hostile scene.

Rest does not exist to erase an infinite Attrition count. It exists to reduce **Settled Fatigue** and allow the character to recover functionality.

In summary:

| Moment | What happens |
| --- | --- |
| During the scene | The character accumulates Attrition, completes thresholds, and generates Projected Fatigue |
| When the scene ends | Projected Fatigue becomes Settled Fatigue; leftover Attrition remains marked |
| During rest | The character can reduce Settled Fatigue and perform recovery tasks |

---

## Types of Rest

There are two main forms of rest:

- **Short Rest**
- **Full Rest**

Each responds to a different need.

| Rest | Duration | Main function |
| --- | ---: | --- |
| Short Rest | 15, 30, or 60 minutes | Partial recovery, stabilization, and immediate preparation |
| Full Rest | 8 hours or more | Deep recovery, treatment, and extended reorganization |

---

## Short Rest

A **Short Rest** represents a brief pause to catch breath, stabilize the body, check resources, and recover some control before continuing.

It does not mean leaving danger behind completely. It is a functional pause within the adventure.

The group can choose one of three durations:

- 15 minutes
- 30 minutes
- 60 minutes

The longer the rest, the greater the possible recovery. It also increases the risk of being detected, interrupted, or caught off guard if the location is not safe.

---

### 15-Minute Rest

A 15-minute rest represents a brief respite.

It is enough to slow breathing, organize equipment, drink water, check the group’s condition, and recover a minimum of control.

**Effect:**

- reduces `1` level of Settled Fatigue from one character, if they have Fatigue 1 or higher
- allows `1` brief maintenance or preparation task

Available brief tasks:

- adjust a strap or piece of equipment
- reorganize a weapon or tool
- quickly check a Wound
- exchange immediate information
- decide a route or simple tactical priority
- assign basic watch or positions

This rest is useful when the group does not want to stop for long, but needs to stabilize before pressing forward.

---

### 30-Minute Rest

A 30-minute rest represents a real brief recovery pause.

It is more than catching breath. It allows the group to recover functional margin and dedicate attention to one more meaningful task.

**Effect:**

- reduces `1` level of Settled Fatigue from each resting character
- allows `1` significant maintenance, treatment, or preparation task

Available significant tasks:

- stabilize a Light Wound with Medicine, if the proper kit is available
- study a recent clue
- review tracks, maps, or notes
- distribute resources
- clean or adjust equipment used in the previous scene
- prepare an immediate route

This is the most stable form of Short Rest. It offers useful recovery without fully abandoning the rhythm of the expedition.

---

### 60-Minute Rest

A 60-minute rest represents a deep pause within the day, without becoming a full sleep.

The character has enough time to recover bodily control, clear the mind, and address immediate consequences more effectively.

**Effect:**

- reduces `2` levels of Settled Fatigue from each resting character
- allows up to `2` maintenance, treatment, or preparation tasks

If conditions are favorable, the Narrator may allow one of these additional benefits:

- reduce `1` additional level of Settled Fatigue
- allow one additional task
- reduce the risk of an unexpected event

The Narrator may consider conditions favorable if the group has:

- reasonable shelter
- warmth or protection from the elements
- water and food
- organized watch
- space to sit or lie down
- appropriate tools for treating the body or equipment

During a 60-minute Rest, a character can attempt to stabilize a Severe Wound with Medicine, if the proper kit is available.

This rest does not free Wound Slots.

---

## Short Recovery Limit

To prevent the group from chaining pauses until all adventure pressure disappears, only the first Short Rest taken after a significant scene reduces Fatigue normally.

Subsequent pauses before a new significant scene can still be used to:

- talk
- plan
- keep watch
- reorganize equipment
- treat Wounds
- prepare resources
- review information

But they do not reduce Fatigue again unless a specific rule allows it.

A brief pause can stabilize you. It does not replace real recovery and cannot be repeated indefinitely to erase the cost of danger.

---

## Full Rest

A **Full Rest** represents a true interruption of the day.

It requires at least `8` hours of rest, sleep, or equivalent recovery under reasonably adequate conditions.

It is not only a physical need. It is also the moment when characters recenter themselves, organize the next day, share information, repair equipment, address persistent consequences, and recover part of what the adventure has taken from them.

---

### 1. Fatigue Recovery

A Full Rest reduces the character’s Settled Fatigue by `3` levels.

```text
Fatigue recovered by Full Rest = 3 levels
```

If conditions are especially favorable, the Narrator may allow the character to recover `1` additional Fatigue level.

Especially favorable conditions may include:

- safe shelter
- uninterrupted sleep
- enough food and water
- adequate temperature
- available medical attention
- no immediate threats

Fatigue cannot drop below `0`.

---

### 2. Leftover Attrition Recovery

Attrition that did not reach a new Projected Fatigue threshold may remain marked between scenes.

A Full Rest reduces that leftover Attrition by an amount equal to:

```text
2 × Endurance
```

If the character has no leftover Attrition marked, this step does not apply.

---

### 3. Wound Treatment

During a Full Rest, a creature can receive Medicine treatment to free Wound Slots.

Treatment does not happen just because 8 hours pass. The Wound must be stabilized and someone must treat the Zone with appropriate tools.

If the treatment succeeds, the patient frees `1` Wound Slot from that Zone.

| Rest | Can stabilize | Can treat | Can free slots |
| --- | --- | --- | ---: |
| 15 minutes | Not by base rule | No | 0 |
| 30 minutes | Light Wound | No | 0 |
| 60 minutes | Severe Wound | No | 0 |
| Full Rest | Critical Wound or any stabilized Wound | Yes, with Medicine | 1 slot per treated character |

The full rules for difficulty, kits, and adjustment by occupied slots are in **Wounds and Damage**.

This section only defines what each rest duration permits.

---

### 4. Equipment Repair

During a Full Rest, a character can attempt to repair damaged equipment.

If they succeed at the appropriate roll based on the required specialization and the item’s grade, they recover up to `5` Durability points on each relevant piece.

This can apply to:

- weapons
- armor
- shields
- tools
- special equipment that allows repair

The Narrator determines which specialization applies according to the object.

---

### 5. Affliction Progression or Relief

Each day of Full Rest reduces the intensity of each active Affliction by `1`, unless a specific rule says otherwise.

This represents that certain consequences require time, care, and real recovery before they begin to ease.

An Affliction does not necessarily disappear after one night of sleep. This effect reduces its intensity according to the Affliction rules.

---

### 6. Day Preparation

During a Full Rest, the group can reorganize for what comes next.

The group may:

- review maps and notes
- discuss the route ahead
- reorganize provisions
- prepare tools
- exchange information about threats
- decide priorities
- reinforce bonds
- address narrative tensions

This moment does not only recover resources. It also lets the group decide how they will continue.

---

## On Physical Recovery

A Full Rest does not automatically remove a Severe Wound, fracture, mutilation, or persistent condition.

It restores an important part of the character’s functionality, but it does not replace stabilization, treatment, Medicine, or prolonged healing when those are necessary.

Sleeping well can return your margin. It cannot always return your integrity.

---

## Risks of Resting

Resting is not always safe.

Recovery is a general rule. Risk depends on the fiction of the scene.

Stopping can mean:

- being found
- losing position
- suffering an environmental shift
- being exposed to nearby threats
- giving the situation time to worsen
- allowing an enemy to reorganize

When the group rests in an unsafe, uncertain, or actively hostile location, the Narrator may make a secret roll to determine whether an unexpected event occurs.

---

## When to Roll Risk

The risk roll should not be made by habit. It should be used when resting genuinely exposes the group to consequences.

This includes situations such as:

- hostile territory
- active pursuit
- likely presence of predators or enemies
- severe weather
- unstable or unknown areas
- resting near an active threat
- scenes where stopping has clear narrative consequences

If the group rests in a safe, controlled, or well-protected shelter, the Narrator may skip the roll.

---

## Base Risk by Duration

When a risk roll is appropriate, the Narrator rolls `1d100` in secret and applies the modifier for the rest’s duration.

| Duration | Base modifier |
| --- | ---: |
| 15 minutes | +0 |
| 30 minutes | +10 |
| 60 minutes | +20 |
| Full Rest | +30 |

The Narrator may apply additional modifiers according to the situation.

| Situation | Modifier |
| --- | ---: |
| Safe shelter | -20 |
| Organized watch | -10 |
| Bad weather | +10 |
| Hostile territory | +10 |
| Active pursuit | +20 |
| Nearby enemies | +20 |
| Hidden or hard-to-track location | -10 |

These modifiers are not mandatory or exclusive. They help the risk depend on the world, not only the clock.

---

## Unexpected Events

If the Narrator determines the rest is subject to risk, consult the following table after the secret roll.

| 1d100 | Event | Description |
| --- | --- | --- |
| 1–45 | No incidents | The rest passes without interruption and the group can recover normally. |
| 46–55 | Unsettling sign | The group detects recent tracks, distant sounds, a strange smell, or signs of nearby activity. There is no immediate interruption, but tension rises. |
| 56–65 | Environmental shift | Weather worsens, visibility drops, temperature changes, or the terrain becomes more difficult. The rest is completed, but the overall situation worsens. |
| 66–75 | Discomfort or displacement | The location proves less safe than expected: moisture, small collapses, aggressive frost, noises, or discomfort force the group to move or interrupt part of the rest. |
| 76–85 | Lost position or bearing | The group is forced to change location, loses orientation, or must spend additional time regaining a safe position or reliable route. |
| 86–93 | Hostile interruption | A creature, enemy scout, or environmental threat interrupts the rest. It may not immediately become combat, but it forces the group to react. |
| 94–100 | Dire event | A serious complication occurs: ambush, dangerous revelation, betrayal, environmental collapse, or a narrative turn that severely alters the situation. |

The unexpected event roll is always secret and made by the Narrator.

---

## Quick Summary

| Rest | Recovery | Tasks | Base risk |
| --- | --- | --- | ---: |
| 15 minutes | -1 Fatigue from one character | 1 brief task | +0 |
| 30 minutes | -1 Fatigue from each resting character | 1 significant task | +10 |
| 60 minutes | -2 Fatigue from each resting character | Up to 2 tasks | +20 |
| Full Rest | -3 Fatigue from each resting character | Treatment, repair, and broad preparation | +30 if the location is unsafe |

The first Short Rest after a significant scene reduces Fatigue normally. Later Short Rests before another significant scene do not reduce Fatigue again unless a specific rule allows it.

---

## Example

The group attempts a 30-minute Short Rest inside abandoned ruins. They know enemy scouts are nearby.

The Narrator decides the rest is possible, but risky. They roll `1d100` in secret and apply modifiers for hostile territory and nearby enemies.

The rest may be completed, but the result can produce an unsettling sign, an environmental shift, lost position, or hostile interruption.

Rest is recovery time. It is not immunity from consequence.
