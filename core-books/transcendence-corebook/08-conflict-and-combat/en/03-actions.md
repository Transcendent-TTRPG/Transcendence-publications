---
title: "Actions"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [actions, combat, atb, active-actions, reactions, free-actions, movement, attack, techniques, attrition]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-acciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-atb-combat-timeline.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/02-attrition-endurance-fatigue.md
authority_refs:
  - Transcendence-design/docs/system/atb-reference.md
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/docs/adr/combat-atb-rhythm-costs.md
  - Transcendence-design/docs/adr/combat-atb-timeline.md
  - Transcendence-design/data/system/atb-combat.yaml
  - Transcendence-design/data/system/attrition-fatigue.yaml
  - Transcendence-design/data/system/specializations.yaml
section_modes:
  - heading: "Example"
    writing_mode: example
---

# Actions

In combat and high-pressure scenes, every action has a place within the temporal flow. Some actions consume a creature’s normal activation. Others happen in response to a trigger. Others are brief enough that they do not need a cost of their own.

Actions are divided into three types:

- **Active Actions**
- **Reactions**
- **Free Actions**

This division does not replace the **ATB** timeline. It indicates how each action enters that system.

---

## Action Types

| Type | When it occurs | ATB effect |
| --- | --- | --- |
| Active Action | During the creature’s normal activation | Advances the marker by rhythm cost |
| Reaction | When a trigger allows a response outside normal activation | Advances the marker if the reaction has a rhythm cost |
| Free Action | At a reasonable moment in the scene | Does not usually advance the marker |

---

## Active Actions

An **Active Action** is a deliberate action performed during a creature’s normal activation on the ATB timeline.

An Active Action:

- occurs during the creature’s normal activation
- has a rhythm cost
- may generate Attrition
- clearly changes the state of the scene

Attacking, moving, hiding, interacting under pressure, or using a specialization in combat are usually Active Actions.

---

## Reactions

A **Reaction** is an action allowed by a trigger.

It does not occur because the creature has reached its normal activation, but because something in the scene allows or demands an immediate response.

A Reaction can be used to:

- respond to an incoming threat
- protect oneself
- cover another creature
- interrupt an action
- deflect an attack
- exploit an opening
- activate a Technique with a reactive trigger

Reactions are not free. If a Reaction has a rhythm cost, it advances the creature’s marker on the ATB. If it generates Attrition, that Attrition is accumulated normally.

A creature can only use a Reaction when a rule, Technique, maneuver, trait, or specific situation allows it.

---

## Free Actions

A **Free Action** is a brief action that does not justify a rhythm cost or Attrition by itself.

It is used for minimal gestures, immediate coordination, or details that let the scene flow without turning everything into a formal activation.

Examples:

- dropping an object
- saying a brief phrase
- pointing in a direction
- nodding or shaking the head
- issuing a short warning
- adjusting posture without changing the situation

An action is not free only because it seems small. If it changes the scene in a meaningful way, demands precision under pressure, substitutes an Active Action, or is repeated to create advantages without cost, the Narrator may assign rhythm cost, Attrition, or both.

Free Actions exist to preserve flow, not to multiply effects without cost.

---

## Rhythm Costs

Rhythm costs indicate how far the creature’s marker advances on the ATB timeline after acting.

| Category | Rhythm cost |
| --- | --- |
| Free | 0 |
| Quick | 3 |
| Standard | 5 |
| Heavy | 7 |
| Variable | Defined by the rule, Technique, or effect |

Rhythm cost does not always measure physical duration. It also measures recovery, exposure, commitment, and lost opportunity within combat.

Specific actions and Techniques may also use intermediate values such as `6` or
`8` when they clearly fall between the anchor bands in play feel.

---

## Base Actions

These actions are available to any character in combat or in a high-pressure scene.

| Action | Type | Rhythm | Base Attrition |
| --- | --- | --- | --- |
| Movement | Active Action | 5 | 1 |
| Natural weapon attack | Active Action | 6 | 1 |
| One-handed weapon attack | Active Action | 6 | 1 |
| Two-handed weapon attack | Active Action | 7 | 1 |
| Two-weapon attack | Active Action | 8 | 1 |
| Interact | Active Action | 3 | 0 or 1 |
| Hide | Active Action | 6 | 1 |
| Use Specialization | Active Action | 4 | 1 |
| Use Technique | Variable | Variable | Variable |
| Drop | Free Action | 0 | 0 |
| Speak briefly | Free Action | 0 | 0 |

The listed Attrition is the base cost. Rules, conditions, Techniques, or circumstances may modify it.

---

## Movement

A **Movement** represents deliberate displacement within a combat or high-pressure scene.

It can be used to:

- advance toward a position
- retreat
- flank
- cross a dangerous zone
- reach cover
- separate from a threat

**Type:** Active Action  
**Rhythm cost:** 5  
**Attrition:** 1

The base distance comes from the character’s species speed. Terrain does not change the rhythm cost. It changes how far the character moves, whether the path requires a roll, or what consequences the movement produces.

| Condition | Effect on distance |
| --- | --- |
| Difficult terrain | Half speed |
| Crawling | Half speed |
| Running | Double speed |

Swimming, climbing, and jumping are part of Movement when used to travel through space. Each may require an appropriate Specialization Roll: **Swim**, **Climb**, or **Jump**.

The Narrator calls for the roll before or during the Movement depending on the risk of the path.

---

## Attack

An attack is a direct attempt to deal damage or physical pressure to a target.

Every attack is resolved with an **Attack Roll** (**A.R.**) unless a specific rule states otherwise. The attack family determines rhythm cost, Attrition, and any additional procedure.

---

### Natural Weapons

Natural weapons are offensive body parts: claws, bite, horns, tail, pincers, stingers, or similar structures.

They require no equipment and cannot be disarmed as long as the creature’s body can use them.

**Type:** Active Action  
**Rhythm cost:** 6  
**Attrition:** 1

Resolved with a standard A.R. using the corresponding competency and associated characteristic.

---

### One-Handed Weapon

A one-handed weapon attack uses a weapon that can be held and operated with one hand: short sword, axe, mace, combat dagger, or equivalent weapon.

This attack leaves the other hand free.

**Type:** Active Action  
**Rhythm cost:** 6  
**Attrition:** 1

Resolved with a standard A.R.

---

### Two-Handed Weapon

A two-handed weapon attack uses a weapon that requires full-body commitment: greatsword, war axe, spear held with both hands, great maul, or equivalent weapon.

These weapons often have greater reach, mass, or threat, but they delay the user’s next intervention.

**Type:** Active Action  
**Rhythm cost:** 7  
**Attrition:** 1

Resolved with a standard A.R.

The character returns to the ATB later than with other base attacks.

---

### Two Weapons

Fighting with two weapons allows the character to chain attacks within the same activation. The main hand performs the initial attack. Additional attacks depend on the character’s coordination under pressure.

**Type:** Active Action  
**Rhythm cost:** 8  
**Attrition:** 1

Procedure:

1. Make an **initial A.R.** with the main hand, without penalty.
2. Make a **dual-wield combat S.R.** against the target’s D.R.
3. If the S.R. exceeds the D.R., you may declare additional attacks.
4. Additional attacks alternate between both hands.

The S.R. uses the **Dual-Wield Combat** specialization and **Agility** as the associated characteristic.

The character gains `1` additional attack for every `2` points of Agility, with a minimum of `1`.

---

## Interact

**Interact** covers brief physical interventions that are neither attacks nor movement.

It can be used to:

- take an object
- pick something up from the ground
- open or close something
- activate a mechanism
- adjust equipment
- store or draw an accessible object
- quickly clean, remove, disentangle, or reset something that is interfering with immediate function

**Type:** Active Action  
**Rhythm cost:** 3  
**Attrition:** 1 under real pressure

Attrition is only generated when the interaction occurs under active scene pressure. A trivial interaction with no immediate risk does not generate Attrition.

### Brief procedural responses

Some Techniques, conditions, or hazards do not mainly answer through direct damage
but through a practical step: cleaning a wound, stripping residue, freeing a
snagged line, removing an irritant, clearing a mechanism, or restoring a body
part to usable function.

When the answer is mostly physical, brief, and does not require trained
diagnosis, it usually resolves as **Interact**.

Suggested cost under active pressure:

- **quick self-response:** `Rhythm 3 / Attrition 1`

This does not replace more specific rules. If the situation requires diagnosis,
technical treatment, or a trained roll, it moves to **Use Specialization**.

### Weapon Change

Changing the weapon the character holds requires two Interact actions:

1. set aside or store the current weapon
2. draw the new weapon

If the character first drops the current weapon as a Free Action, only one Interact action is needed to draw the new weapon.

---

## Hide

**Hide** is the deliberate attempt to leave the enemies’ precise localization.

It does not make the character invisible. It does not erase tracks. It creates doubt about exactly where the character is and where they can act from.

**Type:** Active Action  
**Rhythm cost:** 6  
**Attrition:** 1

To hide, the character needs a real opportunity. They must meet at least one of these conditions:

- have Medium or Total Cover
- be outside effective visual range
- exploit reduced Visibility
- use a sufficient distraction
- have a Technique, trait, artifact, or preparation that allows hiding

A character cannot vanish in plain sight while a relevant enemy clearly has them localized through an applicable sense. If someone sees, hears, smells, or otherwise perceives them without obstruction, the character must first break that localization.

Hide is resolved with a Specialization Roll appropriate to the fiction, such as **Stealth**, **Survival**, or another specialization authorized by a Technique.

The roll is compared against the environment difficulty or enemy Perception. On success, the character gains the **`Hidden`** state against the affected enemies.

The full rules for the `Hidden` state, approximate position, and detection are found in **Cover, Visibility, and Concealment**.

---

## Use Specialization

Using a **Specialization** means applying a trained skill within a hostile or high-pressure scene.

It can cover actions such as:

- jumping an obstacle
- climbing under threat
- swimming against a current
- tracking while moving
- interpreting an inscription before an enemy arrives
- reading an adversary’s body language
- crafting or adjusting something under pressure
- identifying a residue, signal, ailment, or alteration before responding
- applying technical treatment, trained cleaning, or containment under pressure

**Type:** Active Action  
**Rhythm cost:** 4  
**Attrition:** 1

A Specialization produces a narrative or practical result: the character clears the gap, deciphers the code, detects the trap, or reaches a position.

If that result has a direct mechanical consequence, that consequence must come from a specific rule, a later action, or a Technique.

### Trained procedural responses

When a Technique or condition creates a problem that cannot be answered by merely
pulling something off or stepping clear, the proper answer is usually **Use
Specialization**.

Common examples:

- reading what kind of contamination or mark is present
- deciding how to treat a fouled wound
- containing a dangerous spill before it worsens
- disentangling a restraint without making it worse

Suggested costs under active pressure:

- **quick identification:** `Rhythm 3 / Attrition 1`
- **aided or technical treatment:** `Rhythm 6 / Attrition 1`

The actual Specialization depends on the fiction: **Medicine**, **Containment**,
**Dexterity**, **Tracking**, **Grappling**, or another one if a Technique or rule
explicitly authorizes it.

---

## Use Technique

A **Technique** is a trained application that produces a defined mechanical consequence.

Where a Specialization opens a possibility, a Technique turns that possibility into an immediate effect.

**Type:** Variable  
**Rhythm cost:** Defined by the Technique  
**Attrition:** Defined by the Technique

Most Techniques are Active Actions. Some function as Reactions if they have a trigger that allows it.

The full catalog of Techniques and their activation conditions is found in the **Techniques** chapter.

---

## Drop

**Drop** covers letting go of an object the character is holding, as long as that object is not committed to an active maneuver.

**Type:** Free Action  
**Rhythm cost:** 0  
**Attrition:** 0

This covers:

- dropping a weapon from the inactive hand
- letting go of an object before or after the main action
- releasing something that is no longer part of what the character is doing

An object that is part of an active grapple, struggle, block, joint maneuver, or committed situation cannot be dropped for free. In that case, it requires an Interact action.

---

## Speak

**Speak** covers brief communication that does not try to alter another creature’s will, emotion, or decision.

**Type:** Free Action  
**Rhythm cost:** 0  
**Attrition:** 0

This covers:

- a brief warning
- a tactical signal
- a short command directed at an ally
- an involuntary exclamation
- a phrase that transmits immediate information

Deceiving, persuading, negotiating, intimidating, calming, or provoking is not free. The distinction does not depend only on the length of the phrase, but on its function.

Transmitting immediate information can be free. Trying to influence another participant requires an appropriate action.

---

## Example

A character holds a corridor while an ally withdraws.

They can shout “Left!” as a Free Action because the phrase only transmits immediate information.

If that same character tries to calm a panicking ally, provoke an enemy, or force a surrender, it is no longer free. The action now tries to alter another participant’s decision state and must be resolved through the appropriate action structure.
