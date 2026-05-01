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
  - core-books/transcendence-corebook/16-appendices/en/01-specialization-catalog.md
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

Specializations are trainable domains. They do not represent powers a character simply possesses, but practices they have developed: actions that can be attempted, failed, and refined over time.

A characteristic measures a base aptitude. A specialization measures what the character has chosen to practice with that aptitude.

During character creation, specializations help define what the character knows how to do, how they approach problems, and why they differ from others with similar characteristics.

---

## What They Are For

Transcendence does not use classes to assign fixed roles. The difference between characters depends on what each one develops.

Two characters with similar Wisdom can act in different ways if one has practiced Medicine and the other has practiced Survival. The characteristic gives them a comparable base. The specialization defines how they turn that base into action.

Specializations also enable access to Techniques. A Technique does not arise from generic competency: it requires a specific domain the character has already worked on. Without the base specialization, the Technique does not exist.

Each time a character reaches a new rank in a specialization, they gain `+1` to the characteristic associated with that domain. This increase is called **Synapsis**. Characteristics do not increase through free assignment; they increase as a direct consequence of practiced use.

---

## Starting Specializations

Every character begins with four specializations at level 1, Novice rank.

Three come from the character's background, according to its category restrictions. The fourth is a universal choice tied to **Tenacity**: **March**, **Acclimation**, or **Tolerance**.

Every character chooses one of these three options, regardless of background. This choice does not replace species bonuses to Tenacity; both are applied.

The same specialization cannot be chosen twice during character creation. All others begin at level 0, Untrained rank.

Starting specializations already grant the Synapsis corresponding to Novice rank during character creation.

---

## Categories

Specializations are grouped into five categories according to the kind of domain they represent. These categories are not closed compartments. A specialization belongs to a category because of what it covers, not because of the characteristic linked to it.

| Category | Type of domain |
| --- | --- |
| Physical | Bodily technique, movement, effort, and practiced physical control |
| Mental | Interpretation, cunning, attention, situational reading, and adaptive reasoning |
| Social | Influence, expression, projection, deception, and interpersonal control |
| Arts and Crafts | Practical trades and concrete artistic disciplines, such as music, dance, juggling, puppetry, or stage performance |
| Knowledge | Formal study, academic interpretation, structured knowledge, and technical understanding |

A Physical specialization may be linked to Strength, Agility, or Tenacity depending on what it covers. A Social specialization may be linked to Cunning, Composure, Aura, or Presence.

The category organizes the domain. The characteristic determines which value is added to the Specialization Roll.

Artistic disciplines belong to **Arts and Crafts**. Their development and practical use are described in the **Specialization Catalog**, located in the appendices.

---

## Specialization Roll

When a character acts through a specialization, the result is determined with a **Specialization Roll** (**S.R.**).

```text
S.R. = 1d10 + competency level + competency rank + associated characteristic + additional bonuses
```

| Component | What it represents |
| --- | --- |
| **Competency level** | Numeric progress reached in that specialization |
| **Competency rank** | Current degree of mastery: Novice, Adept, Expert, Master, Consummate, or Transcendent |
| **Associated characteristic** | Characteristic linked to the specialization used |
| **Additional bonuses** | Situational modifiers, equipment, active Techniques, or other applicable effects |

### Untrained

Any character can attempt a roll in any specialization, even if they have never practiced it. An **Untrained** character uses only the die and the associated characteristic.

```text
Untrained S.R. = 1d10 + associated characteristic
```

Level and rank are 0. Lack of training does not prevent the attempt, but it limits the results the character can reach. Advanced tests remain possible in the fiction, but they are usually outside the mechanical reach of an untrained character.

Developing a specialization does not enable the action. It makes it sustainable.

---

## How They Are Acquired

Specializations develop through use under pressure. Each time a character uses **Learning Advantage** on an S.R., the roll can generate progress toward the next competency level.

Progress does not appear only because the player chooses to learn. The action must meet three conditions:

- the roll uses the declared specialization
- the difficulty is appropriate for the character's current rank
- the learning die exceeds the progress condition of Evolutionary Advantage

```text
Learning die > die used + competency rank
```

If these conditions are met, the character marks 1 progress point in that specialization.

| Affinity | Progress required per level |
| --- | --- |
| No major affinity | 10 points |
| Major affinity | 5 points |

Major affinity is determined by background. A character with a martial background may have major affinity in Physical specializations. A character with an artisan background may have it in Arts and Crafts.

Major affinity does not block access to other specializations. It only reduces the cost of progressing in those that match the background.

The Narrator validates whether the specialization used is supported by the fiction before it can generate progress. The character's intent must match the declared domain. A character cannot use Traps to analyze a creature's behavior unless there is a concrete reason that justifies it.

The practiced domain must reflect the real action.

There is no limit to how many specializations a character can develop. The limit is practical: each specialization requires time, rolls, and decisions. Prioritizing one slows the others.

---

## Ranks and Synapsis

Competency in a specialization is measured in levels and ranks. Each rank groups two levels and represents a degree of mastery.

| Rank | Name | Levels | Synapsis on entry |
| --- | --- | --- | --- |
| 0 | Untrained | 0 | — |
| 1 | Novice | 1–2 | +1 to characteristic |
| 2 | Adept | 3–4 | +1 to characteristic |
| 3 | Expert | 5–6 | +1 to characteristic |
| 4 | Master | 7–8 | +1 to characteristic |
| 5 | Consummate | 9–10 | +1 to characteristic |
| 6 | Transcendent | 11+ | +1 to characteristic |

When the character reaches the threshold level of a new rank, they automatically gain `+1` to the characteristic associated with that specialization.

This is **Synapsis**: the increase of a characteristic as a direct consequence of practicing domains linked to it.

The tension is structural. Reaching Novice rank in many different specializations generates Synapsis across several characteristics. Deepening a single specialization generates higher S.R. bonuses and access to more advanced Techniques.

Neither path is superior by default. Each one prioritizes a different form of growth.

---

## Direct Use and Techniques

Using a specialization produces a narrative result within the scene. The character observes, interprets, builds, repairs, persuades, remembers, moves, or acts according to the domain used.

That use can open information, routes, narrative advantages, or possible actions. It does not automatically change the mechanical state of the scene unless a rule, consequence, or Narrator decision says so.

A **Technique** is different. It is a specific application the character unlocks by reaching a certain competency level in one or more specializations.

Unlike direct use, a Technique produces a defined mechanical consequence when activated. Its full details appear in the corresponding chapter.

This distinction is structural. Direct use of a specialization opens possibilities. A Technique turns one of those possibilities into an immediate mechanical consequence.

---

## Example

A character uses Survival to read broken tracks at the edge of a flooded road. That use may reveal where a group passed, which route remains viable, and which signs in the terrain should be avoided.

By itself, that use does not damage an enemy, change initiative, or impose a mechanical condition.

If the character later unlocks a Technique tied to tracking or field reading, that Technique can add a defined mechanical consequence to the same kind of trained action.
