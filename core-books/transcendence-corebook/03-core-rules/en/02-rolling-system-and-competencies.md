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
  - core-books/transcendence-corebook/03-core-rules/en/03-environmental-conditions.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/specializations.md
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

## Rolling System

The Rolling System determines the outcome of actions in combat, exploration, or social interaction. Checks use a `d10` modified by characteristics, competencies, equipment, and circumstances.

Players choose how to approach certain actions through Evolutionary Advantage. NPCs and creatures use a simplified system aligned with their narrative function.

## Evolutionary Advantage

For Attack, Defense, Resistance, and Specialization checks, players can choose one of two approaches before rolling.

### Execution Advantage

The player rolls two dice and chooses the higher result. The learning opportunity from that check is forfeited.

### Learning Advantage

The player rolls two dice and uses the lower result to resolve the action.

The higher die is reserved for the learning check.

If that higher die exceeds the sum of the lower die and the rank of the competency designated by that roll's progression rule, the character marks one progress point in that competency.

## NPCs and Other Creatures

NPCs and monsters do not necessarily follow the same progression rules as player characters. Instead, they use Traits: advantages, disadvantages, or special capabilities tied to their nature, behavior, environment, emotional state, or combat role.

## Types of Rolls

The formulas in this chapter include **characteristics** such as Agility, Strength, Tenacity, Composure, and Resilience. These values are defined and assigned during character creation, in the corresponding chapter. They appear here as components of roll formulas.

### Attack Roll (A.R.)

The Attack Roll represents the character's ability to land an effective strike using a weapon, maneuver, skill, or object. It is used to hit a target and overcome its defense, resistance, or another opposed roll, as appropriate.

**Formula:**

`Attack Roll = 1d10 + Competency Level with weapon/object + Associated Characteristic`

Competency reflects the character's technical mastery with the medium being used, while the associated characteristic represents the physical, mental, or martial aptitude used to execute the action.

### Defense Roll (D.R.)

The Defense Roll represents the character's ability to avoid an incoming attack. It combines reflexes, mobility, evasive training, the armor type protecting the threatened zone, and any additional protection provided by shields or other defensive effects.

**Formula:**

`Defense Roll = 1d10 + Evasion Competency Level + Applicable Agility + Defense Bonuses`

Applicable Agility depends on the armor type protecting the resolved hit zone:

- light armor: use full Agility
- medium armor: use half Agility, minimum 1
- heavy armor: Agility does not apply

A shield contributes a general bonus to D.R. as part of defensive equipment, but shield competency progresses through shield-specific Techniques rather than through the generic defense roll.

Its goal is to match or exceed the opponent's offensive roll to avoid damage or additional effects. If it fails, armor in the resolved zone may still absorb part of the impact. Full details for zones, pieces, and block belong in the Equipment chapter.

### Impact Roll (I.R.)

The Impact Roll determines the real damage dealt to the target once the attack has surpassed defense or the corresponding opposed roll.

In this roll, competency rank defines how many damage dice the character can leverage, while the associated characteristic and weapon grade represent execution quality and equipment power.

**Formula:**

`Impact = (Competency Rank × Weapon Damage) + (Associated Characteristic × Weapon Grade)`

#### Weapon damage

A weapon's base damage is expressed by its corresponding die: `d4`, `d6`, `d8`, `d10`, or `d12`. That value is multiplied by the character's competency rank with the weapon used.

#### Impact with untrained weapons

When a character uses a weapon they have no competency with, they can still attack, but their ability to deal effective damage is significantly reduced.

**Formula:**

`Impact Roll = ((1 × Weapon Damage) + (Associated Characteristic × Grade)) / 2`

This represents inefficient execution and reduced ability to use the weapon effectively.

### Characteristic Roll (C.R.)

The Characteristic Roll is used when an action depends primarily on a general aptitude of the character, such as Strength, Agility, Tenacity, Wisdom, or any other relevant characteristic.

It does not represent specific training, but general capability applied to a concrete situation.

**Formula:**

`Characteristic Roll = 1d10 + Characteristic + Reference Level + Additional Bonuses`

It is used to resolve actions that depend on innate or developed qualities of the character, especially when a specific competency is not involved.

### Resistance Roll (R.R.)

The Resistance Roll represents the character's ability to withstand or overcome harmful effects such as poisons, infections, afflictions, curses, or alterations.

The base characteristic depends on the type of effect being faced, while competency in the corresponding resistance reflects the character's accumulated experience against that threat.

**Formulas:**

- Resistance to poisons or infections: `1d10 + Tenacity + Resistances + Additional Bonuses`
- Resistance to afflictions or curses: `1d10 + Composure + Resistances + Additional Bonuses`
- Resistance to alterations: `1d10 + Resilience + Resistances + Additional Bonuses`

The goal is to match or exceed the effect's difficulty to avoid, mitigate, or reduce its consequences.

### Specialization Roll (S.R.)

The Specialization Roll reflects the character's mastery in a specific skill, such as climbing, swimming, disarming traps, or escaping restraints. Unlike a Characteristic Roll, this one does involve specific training.

**Formula:**

`Specialization Roll = 1d10 + Specialization Competency Level + Competency Rank + Associated Characteristic + Additional Bonuses`

Competency level represents accumulated experience, while rank summarizes the overall degree of mastery reached in that specialization.

### Personality Trait Roll (P.R.)

During exploration or conflict, a player may propose that one of their Personality Traits decisively influences the situation. If the Narrator accepts the justification, the character can make a Personality Trait Roll instead of a Characteristic or Specialization Roll.

**Formula:**

`Personality Trait Roll = 2d10`

This roll does not depend on competencies, but on the narrative and psychological strength of the invoked trait.

## Difficulty Thresholds

Every roll is compared against a number. That number either comes from another participant's roll, or from a fixed threshold established by the system or the Narrator.

When the challenge comes from an active opponent, both parties roll and compare results directly. When it comes from the environment, from the intrinsic complexity of a task, or from another system, the Narrator sets a threshold using one of five difficulty tiers.

```text
Threshold = Base + NR
```

**Base** is the fixed value of the chosen difficulty tier. **NR** is the Reference Level of the context: the NR of the creature or entity posing the challenge, or the equivalent the Narrator assigns to the environment or the task.

| Tier | Base | Formula |
| --- | --- | --- |
| **Fundamental** | 5 | 5 + NR |
| **Challenging** | 8 | 8 + NR |
| **Rigorous** | 11 | 11 + NR |
| **Demanding** | 14 | 14 + NR |
| **Extreme** | 17 | 17 + NR |

These five tiers apply to all systems in the game: S.R., C.R., R.R., crafting, ailments, and any other test that requires beating a fixed number. The Narrator announces the tier before requesting the roll. The player knows the threshold before deciding between Execution Advantage and Learning Advantage.

---

## Competencies

Competencies represent the degree of mastery a character has in a specific field. Some are combat-oriented, others relate to survival, knowledge, or concrete skills.

Competencies fulfill two functions:

- they modify rolls
- they allow progression as the character puts them to the test in relevant situations

Competencies do not replace characteristics: both operate together. Characteristics express the character's potential; competencies express how much they have trained, practiced, or refined that potential.

### Competency levels and ranks

Each competency has a level and a rank.

- Competency level represents accumulated numeric progress.
- Competency rank represents the overall degree of mastery reached.

| Rank | Name | Levels |
| --- | --- | --- |
| 0 | Untrained | — |
| 1 | Novice | 1–2 |
| 2 | Adept | 3–4 |
| 3 | Expert | 5–6 |
| 4 | Master | 7–8 |
| 5 | Consummate | 9–10 |
| 6 | Transcendent | 11+ |

A new rank is reached every 2 competency levels. Specializations grant Synapsis on entering each new rank — see the Specializations chapter.

### Starting competencies

The character's background determines which competencies start trained. Competencies granted by background begin at level 1, equivalent to Novice rank.

All other competencies begin at level 0, so the character is considered Untrained in them.

### Competency progression

Competencies increase when the character uses them meaningfully and chooses a learning-oriented approach.

Each time a character uses Learning Advantage, the roll may generate progress in a different competency depending on the type of action and the result obtained.

To gain one competency level, the following are required:

- 5 progress points in major-affinity specializations.
- 10 progress points in all other competencies.

### Appropriate tests for progression

Not every action can improve a competency. For progression to occur, the situation must represent an appropriate challenge.

#### Martial competencies

Martial competencies progress when the character faces appropriately difficult adversaries and truly puts their training into practice.

In the case of weapons, the character must attack and hit creatures whose level is at least equal to their reference level -1.
In addition, for the competency to progress, that attack must deal effective damage.

#### Evasion, armor, shield, and resistance competencies

These competencies progress when the character becomes the target of relevant threats and responds to them in a way that produces real learning: avoiding, absorbing, surviving, or enduring the corresponding exposure.

#### Specialization competencies

Specializations only progress when test difficulty is coherent with the character's rank.

- Novice: can progress with tests of any level.
- Adept: progresses with Fundamental tests or higher.
- Expert: progresses with Challenging tests or higher.
- Master: progresses with Rigorous tests or higher.
- Consummate: progresses with Demanding tests or higher.
- Transcendent: progresses with Extreme tests.

## Competency Types and Their Effects

### Weapons

They represent mastery of a specific weapon type.

**Bonuses**

- Each weapon competency level grants `+1` to A.R.
- Each competency rank grants an additional `+1` to A.R. and one additional die to I.R.

**Progression**

Weapon competency increases when the character uses Learning Advantage, hits with that weapon or object, and deals effective damage in a relevant encounter.

### Armors

They reflect the character's ability to use armor efficiently. They are split by armor type: light, medium, and heavy.

**Bonuses**

- Each competency level increases by 1 the block of the corresponding armor type when that piece resolves the impact in its zone.

**Progression**

Armor competency increases on a failed D.R. with Learning Advantage, provided the impact resolves in a protected zone and the armor actually absorbs part of the damage. Progress applies to the armor type protecting that zone.

### Shields

They represent technical mastery of shield use in combat.

**Bonuses**

- Each competency rank grants access to additional maneuvers depending on shield type.
- Reaching Master reduces the movement penalty of the equipped shield by `grade`, minimum `0`.

**Progression**

Shield competency increases when the character effectively uses shield Techniques. It does not progress through generic D.R.

### Evasion

Evasion represents the character's skill at anticipating and avoiding attacks.

**Bonuses**

- Each competency level grants `+1` to D.R.
- Each competency rank grants `+1` to D.R.

**Progression**

Evasion increases on a successful D.R. with Learning Advantage, when the character avoids relevant attacks or threats through mobility and reflexes.

### Specialization

Specialization competency reflects technical mastery in a specific skill.

**Bonuses**

- Each competency level grants `+1` to S.R.
- Each competency rank grants an additional `+1` to S.R.

**Progression**

Specialization increases by overcoming tests appropriate to the character's current rank.

### Resistances

Resistances represent the character's ability to withstand specific types of danger. Unlike other competencies, they often develop through exposure, survival, and adaptation.

#### Elemental damage

**Bonus**

- Each competency level grants `+1` to R.R. against effects produced by elemental damage.

#### Physical

**Bonus**

- Each competency level grants `+1` to R.R. in general cases of physical resistance.

#### Poison

**Bonus**

- Each competency level grants `+1` to R.R. against poisons.

#### Infection

**Bonus**

- Each competency level grants `+1` to R.R. against infections.

#### Affliction

**Bonus**

- Each competency level grants `+1` to the corresponding roll against afflictions.
- Each competency rank grants `+1` to Affliction R.R. during meditation.

#### Alteration

**Bonus**

- Each competency level grants `+1` to R.R. against alterations.

#### Curses

**Bonus**

- Each competency level grants `+1` to the corresponding roll to detect or resist curses.

**General resistance progression**

Resistances increase on a failed R.R. with Learning Advantage, provided the character actually suffers and survives the corresponding effect. Completely negating a danger does not create the same kind of learning as enduring it.

## Reference Level

The Reference Level (RL) is a derived value that summarizes a character's overall competency. It is not chosen or assigned directly — it emerges from the full set of competencies the character has developed.

### Character RL

A character's RL is calculated as the ceiling of the average of all their base competencies:

`RLc = ⌈average of all the character's initial competencies⌉`

All competencies listed on the character sheet with an initial value other than "—" are included.

### Group RL

When the encounter involves multiple player characters, the group RL is:

`RLg = ⌈average of the RLc of all active PCs in the encounter⌉`

The Narrator uses the group RL to scale creatures, set base difficulty, and compare forces between sides without consulting each competency individually.

### Updating the RL

The RLc may be revised when:

- the character gains new competencies
- several relevant ranks increase
- at the start of an arc or episode

It does not need to be recalculated every session.

### RL in the Characteristic Roll

The RL enters directly into the Characteristic Roll. It represents the fact that as a character becomes more broadly competent, their capacity to respond in situations that depend on general aptitude — rather than specific training — also improves. A more capable character overall is also more capable in areas they have not trained in deeply.

---

## Relationship Between Rolls and Competencies

| Roll | Competency used | Progression with Learning Advantage |
| --- | --- | --- |
| A.R. | weapon or object competency | if the attack succeeds and deals damage, the weapon or object used progresses |
| D.R. | Evasion | if the roll succeeds, Evasion progresses; if it fails and armor absorbs impact, the armor type of the resolved zone progresses |
| I.R. | weapon competency rank (primary factor) | does not progress by itself |
| C.R. | none by default | does not progress by itself |
| R.R. | resistance corresponding to the effect type | if it fails and the effect is suffered, the corresponding resistance progresses |
| S.R. | specialization competency | if the roll succeeds, the specialization used progresses |
| P.R. | none | does not progress by itself |

Shield competency progresses separately, through successful shield Techniques.

---

## Example

A character tries to evade the strike of a heavy creature while using Learning Advantage. The D.R. is resolved with the lower die. If the character avoids the attack, the check may generate progress in Evasion. If the defense fails, but the armor in the resolved zone absorbs part of the impact, the same situation may generate progress in the corresponding armor type instead. The competency that progresses depends on the result of the roll, not only on the kind of action.
