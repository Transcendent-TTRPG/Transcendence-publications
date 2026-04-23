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
  - core-books/transcendence-corebook/04-skills-and-proficiencies/es/especializaciones.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/specializations-catalog.md
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

Specializations are trainable domains. They do not represent powers a character simply possesses, but disciplines they have practiced: things that can be attempted, failed, and refined over time. A characteristic measures what the character is naturally capable of. A specialization measures what they have chosen to practice.

During character creation, specializations help define what the character knows how to do, how they approach problems, and why they differ from others with similar characteristics.

---

## What They Are For

Without classes to assign roles, differentiation between characters depends on what each one chooses to develop. Two characters with similar Wisdom can behave in radically different ways if one has practiced Medicine and the other has practiced Survival. The domain does not define them; it defines how they approach the same problems.

Specializations enable access to Techniques. A Technique does not emerge from a generic competency: it grows from a specific domain the character has already worked at. Without the base specialization, the Technique does not exist.

Every time a character reaches a new rank in a specialization, they gain +1 to the characteristic associated with that domain. This is called **Synapsis**. Characteristics do not increase through free point assignment; they increase as a direct consequence of practiced use.

---

## Starting Specializations

Every character begins with four specializations at Level 1 / Novice. Three come from their background, according to its category restrictions. The fourth is a universal **Tenacity** choice: **March**, **Acclimation**, or **Tolerance**.

This universal choice is linked to Tenacity. Every character starts with one of those three options regardless of the background chosen. It does not replace species bonuses to Tenacity — both accumulate.

The same specialization cannot be chosen twice at creation. All others begin at Level 0, Untrained.

---

## Categories

Specializations are grouped into five categories based on the type of domain they represent. These categories are not rigid divisions: a specialization belongs to a category because of what it covers, not because of which characteristic it is linked to.

| Category | Domain type |
| --- | --- |
| Physical | Bodily technique, movement, exertion, practiced physical control |
| Mental | Interpretation, cunning, attention, situational reading, adaptive reasoning |
| Social | Influence, expression, projection, deception, interpersonal control |
| Arts and Crafts | Broad category that gathers practical crafts and concrete artistic disciplines such as music, dance, juggling, puppetry, or stage acting |
| Knowledge | Formal study, academic interpretation, structured lore, technical understanding |

A Physical specialization may be linked to Strength, Agility, or Tenacity depending on what it covers. A Social specialization may be linked to Cunning, Composure, Aura, or Presence. The category organizes; the characteristic determines the roll formula.

Artistic disciplines are treated as part of **Arts and Crafts**. Their place in the system and their practical use are explained in the **Specializations Catalog**.

---

## Specialization Roll

When a character acts from a specialization, the result is determined by a **Specialization Roll (S.R.)**.

```text
S.R. = 1d10 + Level + Rank + Characteristic + Bonuses
```

| Component | What it represents |
| --- | --- |
| **Level** | Number of competency levels reached in that specialization |
| **Rank** | Current rank number (Novice = 1, Adept = 2, Expert = 3, Master = 4, Consummate = 5, Transcendent = 6) |
| **Characteristic** | Value of the characteristic linked to that specialization |
| **Bonuses** | Situational, equipment, or active Technique bonuses |

### Untrained

Any character can attempt a roll in any specialization, even if they have never practiced it. An **Untrained** character uses only the die and the associated characteristic:

```text
S.R. (untrained) = 1d10 + Characteristic
```

Level and Rank are both zero. The difficulty threshold does the rest: advanced tests are unreachable without training. Developing competency does not enable the attempt — it makes certain results achievable.

---

## How They Are Acquired

Specializations develop through use. Every time a character uses the **Learning Advantage** on an S.R., they accumulate **Progress** toward the next competency level. It is not the roll result that generates progress, but the deliberate choice to learn from it.

| Affinity | Progress needed per level |
| --- | --- |
| No major affinity | 10 |
| Major affinity | 5 |

Major affinity is determined by background. A character with a martial background has major affinity in Physical specializations; one with an artisan background, in Arts and Crafts disciplines. This does not block access to other specializations — it reduces the cost of advancing in their own.

The Narrator validates whether the specialization used is narratively grounded before it generates Progress. The character's intent must be consistent with the domain declared. A character cannot declare Traps to analyze the behavior of a creature unless there is a narrative reason that supports it. The domain being practiced must reflect the actual action.

There is no limit to how many specializations a character can develop. The limit is practical: each specialization demands time, rolls, and decisions. Prioritizing one slows the others.

---

## Ranks and Synapsis

Competency in a specialization is measured in ranks. Each rank spans two levels and carries a name that reflects the domain reached.

| Rank | Name | Levels | Synapsis on entry |
| --- | --- | --- | --- |
| 0 | Untrained | — | — |
| 1 | Novice | 1–2 | +1 to characteristic |
| 2 | Adept | 3–4 | +1 to characteristic |
| 3 | Expert | 5–6 | +1 to characteristic |
| 4 | Master | 7–8 | +1 to characteristic |
| 5 | Consummate | 9–10 | +1 to characteristic |
| 6 | Transcendent | 11+ | +1 to characteristic |

Reaching the threshold level of a new rank automatically grants +1 to the characteristic associated with that specialization. This is Synapsis: the increase of a characteristic as a direct consequence of practicing domains linked to it.

The trade-off is structural. Reaching Rank 1 in many different specializations generates Synapsis across multiple characteristics. Deepening one specialization generates higher S.R. bonuses and access to more advanced Techniques. Neither path is superior by default; each one prioritizes a different kind of growth.

---

## Direct Use and Techniques

Using a specialization produces a **narrative effect**. The character observes, interprets, acts — but the mechanical state of the scene does not change automatically. Changing that state requires additional actions that follow from what was learned.

A **Technique** is different. It is a specific application the character unlocks by reaching a certain competency level in one or more specializations. Unlike direct use, a Technique produces a defined mechanical consequence at the moment of activation. Its full detail belongs to the corresponding chapter.

This distinction is structural. Direct use of a specialization opens possibilities. A Technique converts one of those possibilities into an immediate mechanical consequence.

---

## Example

A character uses Survival to read broken tracks at the edge of a flooded road. That use may reveal where a group passed and what route remains viable, but it does not damage an enemy, change initiative, or impose a condition by itself. If the character later unlocks a Technique tied to tracking or field reading, that Technique can attach a defined mechanical consequence to the same kind of trained action.
