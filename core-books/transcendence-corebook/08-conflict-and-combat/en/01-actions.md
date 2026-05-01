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
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-acciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/02-atb-combat-timeline.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-attrition-endurance-fatigue.md
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
  - heading: "Two-Handed Weapon"
    writing_mode: flavor
  - heading: "Two Weapons"
    writing_mode: flavor
  - heading: "Interact"
    writing_mode: flavor
  - heading: "Hide"
    writing_mode: flavor
  - heading: "Specialization"
    writing_mode: flavor
  - heading: "Techniques"
    writing_mode: flavor
  - heading: "Drop"
    writing_mode: flavor
  - heading: "Speak"
    writing_mode: flavor
  - heading: "Example"
    writing_mode: example
---

# Actions

In combat and high-tension scenes, everything a character does has a place and a cost within the temporal flow. Not all actions occupy that place the same way.

Some demand full commitment and alter a character's rhythm. Others occur as a response to an immediate threat. Others are brief enough that they do not justify a time or effort cost on their own.

Actions are divided into three types:

- **Active Actions**
- **Reactions**
- **Free Actions**

This division does not replace the ATB timeline. It exists to clarify how each type of action enters the temporal flow of combat once that system is already in play.

---

## Active Actions

Active Actions are those a character performs deliberately during their normal activation on the ATB timeline. They represent what the character commits their body, attention, or primary intent to in that moment.

An Active Action:

- occurs during the character's normal activation
- has a rhythm cost that advances their marker on the timeline
- may generate Attrition
- clearly alters the state of the scene

They are the most common form of action in combat and high-tension scenes.

---

## Reactions

Reactions are actions enabled by a trigger. They do not occur because the character's natural activation has arrived, but because something in the scene offers — or demands — an immediate response.

A Reaction can be used to:

- interrupt an incoming action
- protect oneself or cover another character
- deflect an attack
- exploit an enemy's mistake or opening
- respond to a telegraphed action or an imminent threat

**Reactions are not free.**

Even though they occur outside the character's natural activation, they remain within the same temporal system. A Reaction can therefore:

- have a rhythm cost
- generate Attrition
- modify the character's future position on the ATB

---

## Free Actions

Free Actions are brief enough that they do not justify a rhythm cost or Attrition on their own.

They cover minimal gestures, immediate coordination, or details that keep the scene flowing without turning everything into a formal activation.

Examples:

- dropping an object
- saying a brief phrase with no tactical weight
- pointing in a direction
- nodding, shaking a head, or issuing a short warning
- slightly adjusting posture without altering the scene

### Important

An action is not free just because it seems small. If an action:

- meaningfully changes the state of the scene
- demands real precision under pressure
- substitutes something that would normally be an Active Action
- is repeated abusively to multiply effects without cost

the Narrator may decide it is no longer free and assign it a rhythm cost, Attrition, or both.

Free Actions exist to maintain naturalness and flow — not to multiply advantages without cost.

---

## Relation to the ATB

| Type | When it occurs | ATB effect |
| --- | --- | --- |
| Active Action | During the character's normal activation | Advances marker by rhythm cost |
| Reaction | By trigger, outside natural activation | Also advances the marker |
| Free Action | At any reasonable moment | Does not normally alter position, unless the Narrator decides otherwise |

---

## Base Actions

The following actions are available to any character in a combat or high-tension scene. Each entry specifies its type, rhythm cost, and base Attrition cost.

---

### Movement

A Movement represents the character's deliberate displacement through the combat space. Closing in on an advantageous position, retreating from a threat, flanking an enemy, crossing a dangerous zone — any change of position with tactical intent is a Movement. The distance covered and the difficulties encountered depend on the type of terrain and the circumstances of the scene.

**Type:** Active Action  
**Rhythm cost:** 5 (Standard)  
**Attrition:** 1

The base distance comes from the character's species speed values. Terrain does not change the rhythm cost: what changes is how far the character advances, whether the path requires a roll, and the consequences of the movement.

| Condition | Effect on distance |
| --- | --- |
| Difficult terrain | Half speed |
| Crawling | Half speed |
| Running | Double speed |

Swimming, climbing, and jumping each require a Specialization Roll using their matching specialization — Swim, Climb, or Jump. The Narrator calls for it before or during the Movement, depending on what the path demands.

---

### Attack

An attack is a direct attempt to deal damage or physical pressure to a target. The attack family determines how the action resolves and where it sits on the ATB.

#### Natural Weapons

Natural weapons are claws, bite, horns, tail — any offensive element that is part of the creature's body. They require no equipment, cannot be disarmed, and are available as long as the character's body is functioning.

**Type:** Active Action  
**Rhythm cost:** 5 (Standard)  
**Attrition:** 1

Resolved with a standard A.R. using the corresponding competency and associated characteristic.

#### One-Handed Weapon

A one-handed weapon attack covers the full family of offensive weapons held and operated with a single hand: short swords, axes, maces, combat daggers, and similar. It is the most versatile base attack: it leaves the other hand free and lets the character return to the ATB without significant delay. What distinguishes one weapon from another in this family is not the base rhythm cost but the effects they deal, the traits they carry, and the Techniques each one can activate.

**Type:** Active Action  
**Rhythm cost:** 5 (Standard)  
**Attrition:** 1

Resolved with a standard A.R.

#### Two-Handed Weapon

Some weapons demand the whole body — greatswords, war axes, spears held with both hands, great mauls. What they gain in reach, mass, or threat has a price: execution is slower, recovery longer, and mistimed strikes leave real openings. They are weapons that alter the tempo of combat for both the one who wields them and those who face them.

**Type:** Active Action  
**Rhythm cost:** 7 (Heavy)  
**Attrition:** 1

Resolved with a standard A.R. The character returns to the ATB later than with any other base attack.

#### Two Weapons

Fighting with a weapon in each hand allows the character to chain more strikes within a single activation. The dominant hand attacks without penalty; what determines how many additional hits land is the character's ability to sustain that coordination under pressure. It is not simply two attacks — it is a sequence that can collapse if skill does not keep up.

**Type:** Active Action  
**Rhythm cost:** 7 (Heavy)  
**Attrition:** 1

1. **Initial A.R.** with the dominant hand. No penalty.
2. **S.R. for dual-wield combat** against the target's D.R. If the S.R. beats the D.R., the character may declare additional attacks.
3. **Additional attacks:** 1 per 2 points of the character's Agility (minimum 1). Attacks alternate between both hands.

The S.R. uses the dual-wield combat specialization with Agility as the associated characteristic.

---

### Interact

Interact covers brief physical interventions that are neither attacks nor movement: picking up an object, opening or closing something, grabbing something within reach, activating a mechanism, adjusting equipment. These are actions that occur within the flow of combat but are not directed at an adversary. They require physical presence and attention — which is why they carry a rhythm cost — but they do not demand the commitment of an attack or the scope of a movement.

**Type:** Active Action  
**Rhythm cost:** 3 (Quick)  
**Attrition:** 1\*

**Weapon change:** Changing the weapon in hand requires two Interact actions — one to set aside the current weapon and one to draw the new one. If the character drops the current weapon first (Free Action), only one Interact action is needed to draw the next.

\* Attrition is generated only when the interaction occurs under real scene pressure. Trivial or unpressured interactions generate no Attrition.

---

### Hide

Hide is the deliberate attempt to leave the enemies' precise localization. It does not make the character invisible and does not erase physical evidence: it creates tactical uncertainty about where the character is and where they may act from.

**Type:** Active Action  
**Rhythm cost:** 5 (Standard)  
**Attrition:** 1

To use this action, the character needs a real opening. They must have Medium or Total Cover, be outside effective visual range, exploit reduced Visibility, use a sufficient distraction, or rely on a Technique, trait, artifact, or preparation that allows hiding.

A character cannot simply vanish in plain sight while a relevant enemy clearly has them localized through an applicable sense. If someone can see, hear, smell, or otherwise perceive them without obstruction, the character must first break that localization.

Hide is resolved with an appropriate Specialization Roll according to the fiction — such as Stealth, Survival, or another specialization authorized by a Technique — against the environment difficulty or enemy Perception. On success, the character gains Concealment against the affected enemies. The full rules for Concealment, approximate position, and detection are found in Cover, Visibility, and Concealment.

---

### Specialization

A Specialization represents the use of any trained skill in the context of a hostile scene: jumping an obstacle, climbing under threat, swimming against a current while combat continues, tracking in motion, deciphering an inscription before the enemy arrives, reading an adversary's body language, crafting something under pressure. The skill may be physical, mental, or social — the scene imposes the same pressure regardless of which one is being used.

**Type:** Active Action  
**Rhythm cost:** 5 (Standard)  
**Attrition:** 1

A Specialization produces a narrative effect: the character clears the gap, deciphers the code, detects the trap. If that result has direct mechanical consequences, those effects are resolved through the actions that follow or through a Technique.

---

### Techniques

Techniques are the result of accumulated training expressed in a concrete action. Where a Specialization produces a narrative effect, a Technique adds a defined mechanical effect within the same activation — no additional steps, no waiting for the next action. That ability to combine what is done with what is produced mechanically is what distinguishes them, and what justifies that they are only accessible through competencies.

**Type:** Variable  
**Rhythm cost:** Defined by the Technique  
**Attrition:** Defined by the Technique

Most are Active Actions; some function as Reactions and may trigger outside the normal sequence if their condition allows it.

The full catalog of Techniques and their activation conditions is found in the Techniques chapter.

---

### Drop

There are moments when the most useful thing is simply to open the hand: releasing the off-hand weapon to use that hand for something else, letting go of an object that is no longer part of the action, freeing something before the next movement begins. When the object is not involved in any active maneuver, doing so costs nothing.

**Type:** Free Action  
**Rhythm cost:** 0  
**Attrition:** 0

This covers:

- releasing a weapon in the off-hand while the main hand acts
- letting go of an object before or after the main action
- releasing something that is no longer part of what the character is doing

An object that is actively part of a grip or committed joint maneuver cannot be released for free — that requires an Interact action (rhythm cost 3).

### Speak

Not everything said requires time. A warning, a signal, a name called out to the nearest ally — words that transmit information without interrupting the character's flow or advancing their marker on the ATB.

**Type:** Free Action  
**Rhythm cost:** 0  
**Attrition:** 0

This covers:

- a tactical signal or brief warning
- a one-word or short-phrase command directed at an ally
- an involuntary exclamation

Deceiving, persuading, negotiating, or applying social pressure is not free. The distinction is not one of length but of function: transmitting information is free; attempting to influence is not.

---

## Example

A character is holding a corridor while an ally withdraws. The character can shout "Left side!" as a Free Action because that line only transmits immediate information. If the same character tries to calm a panicking ally, provoke an enemy, or force a surrender, that is no longer free: the action is now trying to alter another participant's decision state and must be resolved through the appropriate action structure.
