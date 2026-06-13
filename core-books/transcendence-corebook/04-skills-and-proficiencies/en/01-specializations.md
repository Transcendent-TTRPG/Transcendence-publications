---
title: "Specializations"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 4
section: specializations
status: review
canonical: false
tags: [specializations, progression, synapsis, competencies, character-development]
related:
  - core-books/transcendence-corebook/04-skills-and-proficiencies/es/01-especializaciones.md
  - core-books/transcendence-corebook/17-appendices/en/01-specialization-catalog.md
  - core-books/transcendence-corebook/05-character-creation/en/character-creation.md
  - core-books/transcendence-corebook/03-core-rules/en/02-rolling-system-and-competencies.md
authority_refs:
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/docs/system/competencies.md
  - Transcendence-design/docs/system/backgrounds.md
  - Transcendence-design/docs/system/characteristics.md
  - Transcendence-design/docs/adr/system-abilities-and-specializations.md
  - Transcendence-design/docs/adr/system-specialization-rank-restructure.md
  - Transcendence-design/data/system/specializations.yaml
  - Transcendence-design/data/system/specializations-catalog.yaml
  - Transcendence-design/data/system/competencies.yaml
  - Transcendence-design/data/system/backgrounds.yaml
section_modes:
  - heading: "Example"
    writing_mode: example
---

# Specializations

Specializations are trainable domains. They represent practices the character has developed: actions, trades, knowledge, or disciplines that can be attempted, failed, and refined over time.

A characteristic measures a base aptitude. A specialization measures what the character has practiced with that aptitude.

In play, specializations serve three functions:

- modify Specialization Rolls
- allow progression through Learning Advantage
- activate Synapsis when new ranks are reached

---

## What They Represent

A specialization is not a power the character simply possesses. It is a practice.

Two characters with the same characteristic can act in different ways if they have trained different domains. A character with high Wisdom and Medicine interprets wounds, symptoms, and treatments. Another with high Cunning and Survival reads tracks, weather, routes, and signs in the environment.

The characteristic gives the base. The specialization defines how that base becomes action.

---

## Starting Specializations

During character creation, every character begins with four starting specializations:

| Source | Amount | Starting level | Starting rank |
| --- | --- | --- | --- |
| Background | 3 | 1 | Novice |
| Universal Tenacity choice | 1 | 1 | Novice |

The universal Tenacity specialization must be one of the following:

- **March**
- **Acclimation**
- **Tolerance**

The same specialization cannot be chosen twice during character creation.

All specializations not chosen begin at level `0`, rank **Untrained**.

Starting specializations already grant the Synapsis corresponding to Novice rank during character creation.

---

## Categories

Specializations are grouped into five categories. The category indicates what kind of domain the specialization represents; it does not determine which characteristic it uses by itself.

| Category | Type of domain |
| --- | --- |
| Physical | Bodily technique, movement, effort, and practiced physical control |
| Mental | Interpretation, cunning, attention, situational reading, and adaptive reasoning |
| Social | Influence, expression, projection, deception, and interpersonal control |
| Arts and Crafts | Practical trades and concrete artistic disciplines, such as music, dance, juggling, puppetry, or stage performance |
| Knowledge | Formal study, academic interpretation, structured knowledge, and technical understanding |

A Physical specialization may be linked to Strength, Agility, or Tenacity depending on what it covers. A Social specialization may be linked to Cunning, Composure, Aura, or Presence.

The category organizes the domain. The characteristic determines which value is added to the roll.

The complete list of specializations, their associated characteristics, and their common uses appears in the **Specialization Catalog**, located in the appendices.

---

## Specialization Roll

When a character acts through a specialization, they make a **Specialization Roll** (**S.R.**).

```text
S.R. = 1d10 + competency level + competency rank + associated characteristic + additional bonuses
```

| Component | What it represents |
| --- | --- |
| **Competency level** | Numeric progress reached in that specialization |
| **Competency rank** | Current degree of mastery |
| **Associated characteristic** | Characteristic linked to the specialization used |
| **Additional bonuses** | Situational modifiers, equipment, active Techniques, or other applicable effects |

Use an S.R. when the action depends on a concrete practice: climbing, swimming, tracking, healing, persuading, crafting, disarming traps, interpreting symbols, or any other domain defined as a specialization.

---

## Untrained

Any character can attempt a roll in a specialization they do not have trained.

An **Untrained** character uses only the die and the associated characteristic.

```text
Untrained S.R. = 1d10 + associated characteristic
```

Level and rank are `0`.

Lack of training does not prevent the attempt. It limits what the character can reach. An advanced test may exist in the fiction, but remain outside the mechanical reach of someone without practice.

Developing a specialization does not enable the action. It makes it sustainable.

---

## Levels and Ranks

Each specialization has a level and a rank.

| Rank | Name | Levels |
| --- | --- | --- |
| 0 | Untrained | 0 |
| 1 | Novice | 1–2 |
| 2 | Adept | 3–4 |
| 3 | Expert | 5–6 |
| 4 | Master | 7–8 |
| 5 | Consummate | 9–10 |
| 6 | Transcendent | 11+ |

The level measures numeric advancement. The rank summarizes the degree of mastery reached.

Each new rank can unlock new possibilities, activate Synapsis, and serve as a requirement for Techniques.

---

## Progression

Specializations progress through use under pressure.

For an S.R. to generate progress, three conditions must be met:

- the character uses **Learning Advantage**
- the test difficulty is appropriate for their current rank
- the learning die exceeds the progress condition

```text
Learning die > die used + competency rank
```

If these conditions are met, the character marks `1` progress point in that specialization.

Progress does not appear only because the player chooses to learn. The action must demand something real, and the declared specialization must match what the character is doing.

---

## Progress Required per Level

The amount of progress required depends on the character's affinity.

| Affinity | Progress required to gain 1 level |
| --- | --- |
| No major affinity | 10 points |
| Major affinity | 5 points |

Major affinity comes from the character's background.

A character with a martial background may have major affinity in Physical specializations. A character with an artisan background may have it in Arts and Crafts.

Major affinity does not block other specializations. It only reduces the cost of progressing in those that belong to that category.

---

## Appropriate Tests for Progression

Not every action teaches. For a specialization to progress, the difficulty must be coherent with the character's current rank.

| Current rank | Can progress with tests of... |
| --- | --- |
| Novice | Any tier |
| Adept | Fundamental or higher |
| Expert | Challenging or higher |
| Master | Rigorous or higher |
| Consummate | Demanding or higher |
| Transcendent | Extreme |

A test that is too simple does not generate progress for someone who already dominates that kind of action.

---

## Narrator Validation

The Narrator validates whether the declared specialization matches the real action.

The player must explain how they use that specialization in the scene. If the justification does not match the declared domain, the roll may be resolved with another specialization, with a Characteristic Roll, or without the possibility of progress.

A character cannot use Traps to analyze a creature's behavior only because the player wants to progress Traps. There must be a concrete relationship between the action and the domain used.

The practiced domain must reflect the real action.

---

## Synapsis

Synapsis represents the way practice modifies the character.

Each specialization is associated with a characteristic. When the specialization reaches a new rank, the character gains a permanent `+1` to that characteristic.

| Rank | Name | Synapsis on entry |
| --- | --- | --- |
| 0 | Untrained | — |
| 1 | Novice | +1 to characteristic |
| 2 | Adept | +1 to characteristic |
| 3 | Expert | +1 to characteristic |
| 4 | Master | +1 to characteristic |
| 5 | Consummate | +1 to characteristic |
| 6 | Transcendent | +1 to characteristic |

Synapsis applies when entering a new rank, not each time a level is gained.

During character creation, starting specializations begin at Novice rank. For that reason, each one immediately grants `+1` to its associated characteristic.

---

## Broad or Deep Growth

A player can develop many specializations or concentrate on only a few.

Developing many specializations can activate Synapsis across several characteristics and widen the character's options.

Deepening a single specialization increases its S.R. bonuses and can grant access to more advanced Techniques.

Neither path is superior by default. Each one prioritizes a different form of growth.

---

## Direct Use and Techniques

Using a specialization produces a narrative result within the scene.

The character may observe, interpret, build, repair, persuade, remember, move, or act according to the domain used. That use can open information, routes, narrative advantages, or new possible actions.

By itself, direct use of a specialization does not automatically change the mechanical state of the scene, unless a rule, consequence, or Narrator decision says so.

A **Technique** is different. It is a specific application the character unlocks by reaching a certain competency level in one or more specializations.

Unlike direct use, a Technique produces a defined mechanical consequence when activated.

This distinction is structural:

| Use | Result |
| --- | --- |
| Direct specialization use | Opens narrative or practical possibilities |
| Technique | Produces a defined mechanical consequence |

---

## Quick Summary

| Element | Rule |
| --- | --- |
| Starting specialization | Level 1 / Novice rank |
| Untrained | Level 0 / rank 0 |
| Trained S.R. | `1d10 + level + rank + characteristic + bonuses` |
| Untrained S.R. | `1d10 + characteristic` |
| Progress with major affinity | 5 points per level |
| Progress without major affinity | 10 points per level |
| Synapsis | +1 to characteristic when entering each new rank |
| Technique | Requires a specific domain and produces a defined mechanical consequence |

---

## Example

A character uses Survival to read broken tracks at the edge of a flooded road.

The roll may reveal where a group passed, which route remains viable, and which signs in the terrain should be avoided. That result opens information and options.

By itself, that use does not damage an enemy, change initiative, or impose a mechanical condition.

If the character later unlocks a Technique tied to tracking or field reading, that Technique can add a defined mechanical consequence to the same kind of trained action.
