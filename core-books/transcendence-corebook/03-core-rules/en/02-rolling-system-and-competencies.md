---
title: "Rolling System and Competencies"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 3
status: review
canonical: false
tags: [rolling-system, competencies, attack, defense, impact, resistance, specialization, nr, reference-level, evolutionary-advantage]
related:
  - core-books/transcendence-corebook/03-core-rules/es/02-rolling-system-and-competencies.md
  - core-books/transcendence-corebook/03-core-rules/en/01-general-rules.md
  - core-books/transcendence-corebook/12-gm-toolkit/en/01-environmental-conditions.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/01-specializations.md
authority_refs:
  - Transcendence-design/docs/system/roll-types.md
  - Transcendence-design/docs/system/competencies.md
  - Transcendence-design/docs/system/difficulty-thresholds.md
  - Transcendence-design/docs/system/characteristics.md
  - Transcendence-design/data/system/roll-types.yaml
  - Transcendence-design/data/system/competencies.yaml
  - Transcendence-design/data/system/difficulty-thresholds.yaml
  - Transcendence-design/data/system/characteristics.yaml
section_modes:
  - heading: "Example"
    writing_mode: example
---

# Rolling System and Competencies

## Resolving a Roll

Rolls resolve actions when the outcome is not assured and a relevant consequence exists. They can appear in combat, exploration, social interaction, or any scene where pressure makes failure matter.

The base of a roll is a `d10`. Characteristics, competencies, equipment, traits, conditions, and other modifiers are added according to the type of action.

Player characters can risk certain rolls through **Evolutionary Advantage**. NPCs and other creatures use a more direct layer, based on Traits, special capabilities, and the function they serve within the scene.

Not every trained roll uses Evolutionary Advantage. Some rolls, such as Resistance Rolls, represent internal responses of the body, mind, or essence of the character and are resolved directly.

---

## Evolutionary Advantage

Evolutionary Advantage represents how a character approaches a trained action under pressure. Before rolling, the player chooses whether to prioritize immediate execution or the possibility of learning.

This choice only applies to rolls where the character has active control over execution:

- **Attack Roll**
- **Defense Roll**
- **Specialization Roll**

It does not apply to:

- **Resistance Roll**
- **Characteristic Roll**
- **Personality Trait Roll**

Resistances can progress, but not through Evolutionary Advantage. They progress through exposure, survival, and adaptation.

---

### Execution Advantage

The player rolls two dice and uses the higher result to resolve the roll.

The action is more likely to succeed, but it cannot generate progress. The character focuses on execution, not on exposing themselves to the kind of error that teaches.

---

### Learning Advantage

The player rolls two dice and uses the lower result to resolve the roll. The higher die is reserved as the learning die.

After the action is resolved, compare the learning die against the die used for the roll and the rank of the competency that can progress.

```text
Learning die > die used + competency rank
```

If the learning die exceeds that sum, the character marks `1` progress point in the corresponding competency, provided the action meets the progression conditions for its type.

A roll can fail and still teach. It can also succeed without generating progress. The competency that progresses depends on the type of action and what happened in the scene.

---

## NPCs and Other Creatures

NPCs, adversaries, and Narrator-controlled creatures do not follow the same progression rules as player characters. They do not choose Evolutionary Advantage or accumulate competency progress during play.

Instead, they use **Traits**: advantages, disadvantages, resistances, special capabilities, or behaviors tied to their nature, environment, emotional state, or combat role.

---

## Types of Rolls

The formulas in this chapter use characteristics such as Agility, Strength, Tenacity, Composure, and Resilience. These values are assigned during character creation. Here, they appear only as parts of each roll.

---

### Attack Roll (A.R.)

The Attack Roll measures whether an offensive action connects. It can come from a weapon, maneuver, skill, or object used under pressure. It is compared against defense, resistance, or another opposed roll when appropriate.

**Formula:**

```text
A.R. = 1d10 + competency level + competency rank + associated characteristic + additional bonuses
```

The competency level adds accumulated practice. The competency rank represents the degree of mastery reached. The associated characteristic adds the physical, mental, or sensory aptitude that supports execution.

---

### Defense Roll (D.R.)

The Defense Roll measures whether a creature avoids an incoming attack. It combines reflexes, mobility, evasive training, armor in the threatened zone, and additional protection from shields or other defensive effects.

**Formula:**

```text
D.R. = 1d10 + applicable Evasion + applicable Agility + defensive bonuses
```

**Applicable Evasion** includes the Evasion level and Evasion rank that can be used according to the armor protecting the resolved hit zone.

```text
Applicable Evasion = applicable Evasion level + applicable Evasion rank
```

Both Evasion and Agility depend on the armor type protecting the resolved hit zone:

| Armor in the zone | Applicable Evasion | Applicable Agility |
| --- | --- | --- |
| Unarmored | Full Evasion | Full Agility |
| Light | Full Evasion | Full Agility |
| Medium | Half Evasion, minimum 1 | Half Agility, minimum 1 |
| Heavy | 0 | 0 |

For medium armor, calculate half Evasion and half Agility separately. Each result is rounded up, unless a specific rule says otherwise.

A shield contributes a general bonus to D.R. as part of defensive equipment. Its competency does not progress through this generic roll; it progresses through shield Techniques and maneuvers.

D.R. must match or exceed the opponent's offensive roll to avoid damage or additional effects. If it fails, armor in the resolved zone may still absorb part of the impact. Full details for zones, pieces, and block are described in the Equipment chapter.

---

### Impact Roll (I.R.)

The Impact Roll is resolved after an attack beats defense or the corresponding opposed roll. It defines how much damage reaches the target.

I.R. does not use a base `d10`. It uses the weapon's damage die, multiplied by the character's competency rank with that weapon. The associated characteristic and weapon grade add execution and equipment power.

**Formula:**

```text
I.R. = (competency rank × weapon damage) + (associated characteristic × weapon grade)
```

#### Weapon Damage

The weapon's base damage uses the die indicated by its category: `d4`, `d6`, `d8`, `d10`, or `d12`.

If a character has rank 3 with a weapon that deals `d8` damage, they roll `3d8` as the base impact before adding the associated characteristic by weapon grade.

---

#### Impact with Untrained Weapons

A character can attack with a weapon they have no competency with. The strike can connect, but impact is reduced.

**Formula:**

```text
Untrained I.R. = ((1 × weapon damage) + (associated characteristic × weapon grade)) / 2
```

This formula keeps the weapon usable, but limits how much an untrained character can draw from it.

---

### Characteristic Roll (C.R.)

The Characteristic Roll is used when an action depends on a general aptitude: Strength, Agility, Tenacity, Wisdom, or any other relevant characteristic.

It does not use specific training. It takes the character's aptitude and applies it to a concrete situation.

**Formula:**

```text
C.R. = 1d10 + characteristic + Reference Level + additional bonuses
```

C.R. is used when no specific competency resolves the action better. It does not generate progress by itself.

---

### Resistance Roll (R.R.)

The Resistance Roll resolves whether a creature withstands, avoids, or reduces a harmful effect: poison, infection, affliction, curse, or alteration.

Unlike an Attack Roll, Defense Roll, or Specialization Roll, an R.R. does not represent voluntary execution by the character. It represents a response of the body, mind, or essence against a danger trying to affect it.

For that reason, an R.R. is resolved with a single die and does not use Evolutionary Advantage by default.

The base characteristic depends on the effect type. The corresponding resistance adds accumulated experience against that danger.

**Formulas:**

| Effect | Formula |
| --- | --- |
| Poisons or infections | `1d10 + Tenacity + corresponding resistance + additional bonuses` |
| Afflictions or curses | `1d10 + Composure + corresponding resistance + additional bonuses` |
| Alterations | `1d10 + Resilience + corresponding resistance + additional bonuses` |

The goal is to match or exceed the effect's difficulty to avoid, mitigate, or reduce its consequences.

An R.R. does not generate progress through Learning Advantage. Resistances progress through exposure, as described in the Resistances section.

A specific rule, Technique, Grievance, or exceptional effect can alter this structure, but it must say so explicitly.

---

### Specialization Roll (S.R.)

The Specialization Roll is used for trained skills: climbing, swimming, disarming traps, escaping restraints, or any practiced domain defined as a specialization.

**Formula:**

```text
S.R. = 1d10 + specialization competency level + competency rank + associated characteristic + additional bonuses
```

The level adds accumulated practice. The rank adds the degree of mastery reached in that specialization.

---

### Personality Trait Roll (P.R.)

During exploration or conflict, a player may propose that one of their Personality Traits influences the situation. If the Narrator accepts the justification, the character can make a Personality Trait Roll instead of a Characteristic Roll or Specialization Roll.

**Formula:**

```text
P.R. = 2d10
```

This roll does not depend on competencies and does not generate progress. It depends on the invoked trait, its weight in the scene, and the Narrator's approval.

---

## Difficulty Thresholds

Every roll is compared against a number. That number may come from another participant's roll or from a fixed threshold established by the system or the Narrator.

When the challenge comes from an active opponent, both parties roll and compare results directly. When it comes from the environment, the complexity of a task, or another system, the Narrator sets a threshold using one of five difficulty tiers.

```text
Threshold = base + RL
```

**Base** is the fixed value of the chosen difficulty tier. **RL** is the Reference Level of the context: the RL of the creature or entity posing the challenge, or the equivalent the Narrator assigns to the environment, obstacle, or task.

| Tier | Base | Formula |
| --- | --- | --- |
| **Fundamental** | 5 | 5 + RL |
| **Challenging** | 8 | 8 + RL |
| **Rigorous** | 11 | 11 + RL |
| **Demanding** | 14 | 14 + RL |
| **Extreme** | 17 | 17 + RL |

These five tiers apply to all systems that require beating a fixed threshold: S.R., C.R., R.R., crafting, Grievances, and equivalent tests.

The Narrator announces the difficulty tier before requesting the roll, unless revealing that information contradicts the nature of the scene.

If an A.R., D.R., or S.R. can generate progress through Learning Advantage, the player must know the threshold before choosing how to roll.

R.R. does not use Learning Advantage. If a Resistance can progress, it does so through exposure after the effect is resolved.

---

## Competencies

Competencies indicate what a character has practiced and how far that practice has gone. Some belong to combat. Others belong to survival, knowledge, crafts, movement, or concrete skills.

Competencies fulfill two functions:

- modify rolls
- allow progression when the character faces relevant situations

Not all competencies progress in the same way.

| Competency type | How it progresses |
| --- | --- |
| Weapons, Evasion, and Specializations | Through Learning Advantage |
| Armor | By absorbing damage after a failed D.R. |
| Shields | Through shield Techniques and maneuvers |
| Resistances | Through exposure, consequence, and survival |

Competencies do not replace characteristics. Characteristics provide the base. Competencies show how much the character has trained, practiced, refined, or adapted that base.

---

### Competency Levels and Ranks

Each competency has a level and a rank.

- **Competency level** records accumulated numeric progress.
- **Competency rank** summarizes the degree of mastery reached.

| Rank | Name | Levels |
| --- | --- | --- |
| 0 | Untrained | 0 |
| 1 | Novice | 1–2 |
| 2 | Adept | 3–4 |
| 3 | Expert | 5–6 |
| 4 | Master | 7–8 |
| 5 | Consummate | 9–10 |
| 6 | Transcendent | 11+ |

A new rank is reached every 2 competency levels. Specializations grant Synapsis when entering each new rank, as described in the Specializations chapter.

---

### Starting Competencies

The character's background determines which competencies begin trained. Competencies granted by background start at level 1, equivalent to Novice rank.

All other competencies begin at level 0. The character is considered Untrained in them.

---

### Competency Progression

Competencies increase when the character faces a situation that demands something real for their current rank and meets the progression conditions of that competency.

To gain one competency level, the following are required:

- 5 progress points in major-affinity specializations
- 10 progress points in all other competencies

A specialization's affinity is defined in the Specializations chapter.

Resistances do not use major affinity by base rule, unless a specific rule says otherwise.

---

### Appropriate Tests for Progression

Not every action teaches. For progress to occur, the situation must demand something real for the character's current rank.

#### Martial Competencies

Martial competencies progress when the character faces appropriately difficult adversaries and puts their training into practice.

In the case of weapons, the character must use Learning Advantage, attack, hit, and deal effective damage to a creature whose level is at least equal to the character's RL -1.

#### Evasion, Armor, and Shield

These competencies progress when the character is exposed to relevant threats and responds in a way that leaves learning behind: avoiding, absorbing, or intervening through a defensive technique.

- Evasion progresses with a successful D.R. under Learning Advantage.
- Armor progresses when a D.R. fails and armor absorbs part of the impact.
- Shield progresses through successful shield Techniques or maneuvers.

#### Resistances

Resistances progress when the character is exposed to a real danger, suffers its consequences, and survives.

They do not progress through Evolutionary Advantage.

#### Specialization Competencies

Specializations only progress when test difficulty is coherent with the character's rank.

| Current rank | Can progress with tests of... |
| --- | --- |
| Novice | Any tier |
| Adept | Fundamental or higher |
| Expert | Challenging or higher |
| Master | Rigorous or higher |
| Consummate | Demanding or higher |
| Transcendent | Extreme |

---

## Competency Types and Their Effects

### Weapons

Weapon competency measures mastery of a specific weapon type.

**Bonuses**

- Each weapon competency level grants `+1` to A.R.
- Each competency rank grants an additional `+1` to A.R.
- Each competency rank adds one damage die to I.R.

**Progression**

Weapon competency increases when the character uses Learning Advantage, hits with that weapon or object, and deals effective damage in a relevant encounter.

---

### Armor

Armor competency covers efficient use of defensive pieces. It is split by type: light, medium, and heavy.

**Bonuses**

- Each competency level increases the block of armor of that type by `1` when that piece resolves the impact in its zone.

**Progression**

Armor competency increases on a failed D.R., provided the impact resolves in a protected zone and the armor actually absorbs part of the damage.

The character does not choose Learning Advantage to progress armor. Armor teaches when it receives real pressure and absorbs part of the impact.

Progress applies to the armor type protecting that zone.

---

### Shields

Shield competency measures technical mastery of shield use in combat.

**Bonuses**

- Each competency rank grants access to additional Techniques according to shield type.
- Reaching Master reduces the movement penalty of the equipped shield by `grade`, minimum `0`.

**Progression**

Shield competency increases when the character uses shield Techniques or maneuvers successfully. It does not progress through generic D.R.

---

### Evasion

Evasion competency measures the character's skill at anticipating and avoiding attacks.

**Bonuses**

- Each competency level grants `+1` to Evasion.
- Each competency rank grants an additional `+1` to Evasion.
- Evasion is added to D.R. according to the armor type protecting the resolved hit zone.

**Progression**

Evasion increases on a successful D.R. with Learning Advantage, provided the character avoids a relevant attack or threat through mobility, anticipation, or reflexes.

---

### Specialization

Competency in a specialization measures technical mastery of a concrete skill.

**Bonuses**

- Each competency level grants `+1` to S.R.
- Each competency rank grants an additional `+1` to S.R.

**Progression**

Specialization increases by overcoming tests appropriate to the character's current rank and meeting the learning condition of Evolutionary Advantage.

---

### Resistances

Resistances cover specific dangers that poison, infect, alter, afflict, or curse a creature. They are not trained only through controlled repetition. They often grow through exposure, survival, and adaptation.

Resistances do not reduce Impact, elemental damage, or Wounds. Damage is resolved through the relationship between Impact, Block, and the Wound or HP rules. If a fire, water, light, or other elemental-origin attack deals damage, that damage follows the normal flow unless a specific rule says otherwise.

Resistances are added to the corresponding R.R., but they do not use Evolutionary Advantage.

---

#### Poison

**Bonus**

- Each competency level grants `+1` to R.R. against poisons.

---

#### Infection

**Bonus**

- Each competency level grants `+1` to R.R. against infections.

---

#### Affliction

**Bonus**

- Each competency level grants `+1` to R.R. against afflictions.
- Each competency rank grants `+1` to Affliction R.R. made during meditation.

---

#### Alteration

**Bonus**

- Each competency level grants `+1` to R.R. against alterations.

---

#### Curses

**Bonus**

- Each competency level grants `+1` to rolls made to detect or resist curses.

---

## Learning Through Exposure

Resistances increase when the character is exposed to a real danger, suffers it, and survives its consequences.

A Resistance can gain progress if all of the following conditions are met:

- the character makes an R.R. against the corresponding danger
- the danger is relevant for the character's current rank
- the character fails the R.R. or suffers a partial consequence from the effect
- the character survives the exposure

If these conditions are met, the character marks `1` progress point in the corresponding Resistance.

Completely resisting a danger does not generate progress by base rule. Resistance improves when the character is forced to adapt, not when they avoid all consequence.

The Narrator can deny progress if the exposure is trivial, controlled without real risk, repeated artificially, or insufficient to challenge the character's current rank.

A specific rule, Technique, Grievance, treatment, mutation, or special condition can modify this learning.

---

#### About Elemental Resistance

**Elemental Resistance** and **Elemental Vulnerability** are not competencies. They do not progress through Evolutionary Advantage and are not part of the character's trainable resistance competencies.

When a creature, material, object, Technique, or effect has resistance or vulnerability against an elemental origin, it is resolved through the rules for **Elemental Damage and Affinities**.

---

## Reference Level

The **Reference Level** (**RL**) summarizes a character's overall competency. It is not chosen or assigned directly. It comes from the set of competencies the character has developed.

---

### Character RL

A character's RL is calculated as the average, rounded up, of all their base competencies.

```text
RLc = ⌈average of all the character's base competencies⌉
```

All competencies listed on the character sheet with a numeric value are included. Competencies marked as `—` are not included in the calculation.

---

### Group RL

When the encounter involves multiple player characters, the group's RL is calculated as the average, rounded up, of the individual RL values of all active PCs in the encounter.

```text
RLg = ⌈average of the RLc of all active PCs in the encounter⌉
```

The Narrator uses group RL to scale creatures, set base difficulties, and compare forces between sides without reviewing every individual competency.

---

### Updating RL

A character's RL may be revised when:

- the character gains new competencies
- several relevant competencies increase in rank
- a new arc or episode begins

It does not need to be recalculated every session.

---

### RL in the Characteristic Roll

RL enters directly into the Characteristic Roll. As the character becomes more broadly competent, they respond better even when the action does not depend on specific training.

RL does not replace a trained competency. It prevents the character's overall experience from disappearing in basic tests.

---

## Relationship Between Rolls and Competencies

| Roll | Competency used | Progression |
| --- | --- | --- |
| A.R. | Competency of the weapon or object used | If it uses Learning Advantage, succeeds, and deals effective damage, the weapon or object used progresses. |
| D.R. | Applicable Evasion according to armor | If it uses Learning Advantage and succeeds, Evasion progresses. If it fails and armor absorbs impact, the armor type of the resolved zone progresses. |
| I.R. | Weapon competency rank | Does not progress by itself. |
| C.R. | None by default | Does not progress by itself. |
| R.R. | Resistance corresponding to the effect type | Does not use Evolutionary Advantage. If the character fails or suffers a partial consequence and survives a relevant danger, the corresponding Resistance progresses. |
| S.R. | Competency of the specialization involved | If it uses Learning Advantage, succeeds, and the difficulty is appropriate, the specialization used progresses. |
| P.R. | None | Does not progress by itself. |

Shield competency progresses separately, through successful shield Techniques and maneuvers.

---

## Example

A character tries to evade the strike of a heavy creature while using Learning Advantage. They roll two dice and resolve the D.R. with the lower die. The higher die is reserved as the learning die.

If the character avoids the attack and the learning die exceeds the progress condition, the situation can generate progress in Evasion.

If the D.R. fails, but the armor in the resolved zone absorbs part of the impact, the situation can generate progress in the corresponding armor type.

Later, the same character suffers a toxin and makes a Poison R.R. This roll is resolved with a single `d10`; it does not use Evolutionary Advantage.

If the character fails the R.R., suffers the effect, and survives, they can mark `1` progress in Poison Resistance, provided the exposure is relevant for their current rank.

The competency that progresses depends on the result of the scene, not only on the type of roll.
