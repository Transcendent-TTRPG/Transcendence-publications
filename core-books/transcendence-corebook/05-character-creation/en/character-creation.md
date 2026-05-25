---
title: "Character Creation"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 5
status: review
canonical: false
tags: [character-creation, species, background, specializations, synapsis, attributes, personality-traits, derived-attributes]
related:
  - core-books/transcendence-corebook/05-character-creation/es/character-creation.md
  - core-books/transcendence-corebook/03-core-rules/en/02-rolling-system-and-competencies.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/01-specializations.md
authority_refs:
  - Transcendence-design/docs/system/backgrounds.md
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/docs/system/characteristics.md
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/docs/adr/system-abilities-and-specializations.md
  - Transcendence-design/docs/adr/system-specialization-rank-restructure.md
  - Transcendence-design/data/system/backgrounds.yaml
  - Transcendence-design/data/system/attrition-fatigue.yaml
  - Transcendence-design/data/system/specializations.yaml
  - Transcendence-design/data/system/specializations-catalog.yaml
  - Transcendence-design/data/system/competencies.yaml
section_modes:
  - heading: "Brief Example"
    writing_mode: example
  - heading: "Example"
    writing_mode: example
---

# Character Creation

Character creation defines who you are at the start of the adventure, where you come from, and what capabilities you have developed before entering play.

To create a character, follow these steps in order:

1. Define the concept.
2. Record base characteristics.
3. Choose species.
4. Choose background.
5. Select starting specializations.
6. Apply Synapsis.
7. Calculate derived attributes.
8. Choose Personality Traits.
9. Record additional species attributes.

The order matters. Some steps modify values used later.

---

## 1. Define the Concept

Before choosing numbers, define a brief idea of the character.

You do not need to write a full backstory. Answer three questions:

| Question | Expected answer |
| --- | --- |
| What kind of person or creature are they? | Their general identity |
| What drives them? | Their main motivation |
| How do they face the world? | Their attitude toward danger, conflict, other characters, or uncertainty |

A concept should not be only a mechanical function.

Do not write only:

- “a strong character”
- “someone stealthy”
- “an intelligent character”

Frame the character as a concrete person:

- a patient hunter who learned to survive alone
- an old custodian who fears forgetting what they swore to protect
- an insecure noble trying to keep authority in a world that no longer respects it
- a fighter raised to endure pain before understanding it

Use this concept as a guide when choosing species, background, specializations, and Personality Traits.

At the end of this step, write a short concept phrase on your sheet.

---

## 2. Record Base Characteristics

All characteristics begin at `0`.

This value does not mean the character is incompetent. It is a neutral baseline. Species and Synapsis will increase these values during character creation.

| Group | Characteristic | What it represents |
| --- | --- | --- |
| Physical | Strength | Physical power, pushing, carrying, striking, and raw exertion |
| Physical | Agility | Coordination, mobility, balance, and bodily reaction |
| Physical | Tenacity | Physical endurance, pain tolerance, fatigue, and prolonged strain |
| Mental | Intellect | Reasoning, memory, study, and formal understanding |
| Mental | Cunning | Improvisation, deception, practical creativity, and reading opportunities |
| Mental | Wisdom | Perception, intuition, judgment, and applied experience |
| Social | Composure | Self-control, emotional stability, and calm under pressure |
| Social | Aura | Natural and involuntary impression projected by the character |
| Social | Presence | Active projection, authority, influence, and social impact |

At the end of this step, your sheet should have every characteristic at `0`.

---

## 3. Choose Species

Species defines the character’s biological and cultural foundation.

When you choose species, record everything indicated in its profile.

| Element | What to record |
| --- | --- |
| Longevity | Typical lifespan |
| Size | Size category |
| Height and weight | Physical reference range |
| Languages | Languages known at the start |
| Speed | Distance covered with a movement action |
| Characteristic bonuses | Starting increases granted by species |
| Other equivalent starting values | Competencies, senses, innate traits, or other special values |
| Heritage | Vulnerability, limitation, or ancestral mark |
| Legacy | Innate advantages or shared adaptations |
| Bodily attacks or natural weapons | Claws, fangs, horns, tail, pincers, stingers, or other natural combat forms |
| Variant | Internal adaptation of the species, if one exists |

### Apply Species Bonuses

After choosing species, increase the characteristics indicated by its profile.

```text
Current characteristic = 0 + species bonus
```

The complete description of each species appears in the **Species** chapter.

At the end of this step, your sheet should have:

- chosen species
- species attributes recorded
- characteristic bonuses applied

---

## 4. Choose Background

Background represents the character’s life before the adventure.

Each background grants two things:

| Benefit | Function |
| --- | --- |
| Major affinity | Reduces required progress in one specialization category |
| Starting specializations | Defines three practices the character already developed before play |

A specialization with major affinity needs `5` progress points to gain a level.

All other specializations need `10` progress points.

---

## Available Backgrounds

### Martial Artist

The Martial Artist has devoted their life to bodily refinement, combat, or physical endurance.

| Trait | Value |
| --- | --- |
| Major affinity | Physical |
| Starting specializations | 2 Physical + 1 Mental, Social, or Knowledge |
| Additional rule | May replace any number of starting species natural-weapon competencies with crafted-weapon competencies. |

---

### Artisan

The Artisan transforms matter, tools, and resources into useful, beautiful, or dangerous objects.

| Trait | Value |
| --- | --- |
| Major affinity | Arts and Crafts |
| Starting specializations | 2 Arts and Crafts + 1 from any category |

---

### Wanderer

The Wanderer was shaped by the road, adaptation, observation, and survival away from a stable place.

| Trait | Value |
| --- | --- |
| Major affinity | Mental |
| Starting specializations | 2 Mental + 1 Physical, Social, or Knowledge |

---

### Custodian

The Custodian comes from traditions, institutions, or duties tied to protecting knowledge, memory, or relics.

| Trait | Value |
| --- | --- |
| Major affinity | Knowledge |
| Starting specializations | 2 Knowledge + 1 Physical, Mental, or Social |

---

### Noble

The Noble was raised among hierarchy, education, influence, duty, or social ties.

| Trait | Value |
| --- | --- |
| Major affinity | Social |
| Starting specializations | 1 Social + 2 from any other category |

---

At the end of this step, record:

- your background
- your major affinity
- the categories allowed for your three starting specializations

---

## 5. Select Starting Specializations

Each character begins with three specializations granted by background.

These specializations must follow the restrictions of the chosen background.

Each starting specialization:

- begins at level `1`
- begins at Novice rank
- activates Synapsis
- cannot be repeated during character creation

```text
Starting specialization = level 1 / Novice rank
```

In addition, every character receives one universal starting Tenacity specialization.

Choose one:

- **March**
- **Acclimation**
- **Tolerance**

This specialization also begins at level `1`, Novice rank, and activates Synapsis.

You cannot choose the same specialization twice. If a specialization was already chosen through background, it cannot be repeated as the universal choice.

At the end of this step, your character should have four starting specializations:

| Source | Amount |
| --- | --- |
| Background | 3 specializations |
| Universal Tenacity choice | 1 specialization |
| Total | 4 starting specializations |

The complete list of specializations appears in the **Specialization Catalog**.

---

## 6. Apply Synapsis

Synapsis represents how practice modifies the character’s characteristics.

Each specialization is associated with a characteristic. When a specialization reaches a new rank, that characteristic increases by `+1`.

During character creation, all starting specializations begin at Novice rank. For that reason, each one grants `+1` to its associated characteristic.

```text
Synapsis from starting specialization = +1 to associated characteristic
```

This includes:

- the three background specializations
- the universal Tenacity specialization

### How to Apply Synapsis

For each starting specialization:

1. Check its associated characteristic.
2. Add `+1` to that characteristic.
3. Repeat this process for all four starting specializations.

If several specializations are associated with the same characteristic, their increases stack.

```text
Final characteristic = species bonus + applied Synapsis
```

At the end of this step, all final characteristics should be calculated.

---

## 7. Calculate Derived Attributes

Derived attributes are calculated after applying species and Synapsis.

During character creation, calculate these derived attributes:

- **Preparation**
- **Resilience**
- **Endurance**
- **Sanity**

These values use the character’s final characteristics.

---

### Preparation

Preparation measures how well the character anticipates, reacts, and acts under pressure.

```text
Preparation = (Agility + Cunning + Composure) / 3
```

Minimum value: `1`.

---

### Resilience

Resilience measures the character’s ability to resist and recover from adverse alterations.

```text
Resilience = (Tenacity + Wisdom + Composure) / 3
```

Minimum value: `1`.

---

### Endurance

Endurance measures how much accumulated strain the character can sustain before entering Fatigue.

```text
Endurance = 3 + (Tenacity × 2)
```

The universal starting Tenacity specialization is already included indirectly, because it applies Synapsis and increases Tenacity during character creation.

---

### Sanity

Sanity measures the character’s base mental and emotional stability against extreme pressure, horror, corruption, or effects that attack internal balance.

```text
Sanity = 3 + (Composure × 2)
```

The full interaction between Sanity, cosmic horror, corruption, and equipment appears in their corresponding sections. During character creation, record the base value so the sheet is complete.

---

### Rounding

If Preparation or Resilience produces fractions or decimals, round up.

```text
1.1 → 2
1.6 → 2
2.0 → 2
```

Endurance and Sanity do not require rounding with their current formulas.

If a permanent characteristic increases later, recalculate any derived attribute that depends on it.

---

## Brief Example

After applying species and Synapsis, a character has:

| Characteristic | Value |
| --- | --- |
| Agility | 2 |
| Cunning | 1 |
| Composure | 1 |
| Tenacity | 2 |
| Wisdom | 1 |

Calculate Preparation:

```text
Preparation = (2 + 1 + 1) / 3
Preparation = 4 / 3
Preparation = 2
```

Calculate Resilience:

```text
Resilience = (2 + 1 + 1) / 3
Resilience = 4 / 3
Resilience = 2
```

Calculate Endurance:

```text
Endurance = 3 + (2 × 2)
Endurance = 7
```

Calculate Sanity:

```text
Sanity = 3 + (1 × 2)
Sanity = 5
```

Preparation and Resilience are rounded up.

---

## 8. Choose Personality Traits

Personality Traits describe how the character thinks, feels, and responds to the world.

They can also be used in play. If a trait clearly influences a scene, the player may propose a **Personality Trait Roll** instead of a Characteristic Roll or Specialization Roll. The Narrator decides whether the justification is valid.

You can choose traits in two ways.

---

### Structured Option

Choose one trait for each factor:

| Factor | What it describes |
| --- | --- |
| Openness to Experience | Relationship with the new, uncertain, abstract, or imaginative |
| Conscientiousness | Discipline, order, consistency, and responsibility |
| Extraversion | Way of occupying social space |
| Agreeableness | Empathy, cooperation, trust, or reserve toward others |
| Neuroticism | Emotional stability and response to anxiety, pressure, or internal conflict |

Each trait must have an intensity:

- high
- low

Intensity does not mean “better” or “worse.” It defines how that factor expresses itself in the character.

---

### Free Option

Choose five traits without assigning them to factors.

They can be single words or short phrases:

- restless
- analytical
- loyal
- impulsive
- somber
- distrustful
- protective
- curious

This option works the same in play. Any trait can be invoked if the player explains how it affects the scene and the Narrator accepts the justification.

---

At the end of this step, your character should have:

- five Personality Traits, or
- one trait for each factor with high or low intensity

The complete list of suggested traits appears in the **Personality Traits** section.

---

## 9. Record Additional Species Attributes

Before finishing, review the full profile of your species and record any element not already written on the sheet.

This may include:

- size
- height and weight
- languages
- speed
- heritage
- legacy
- other equivalent starting values
- bodily attacks or natural weapons
- variant
- additional special capabilities
- usage restrictions
- situational bonuses

You do not need to copy all cultural or narrative information from the species entry. You should record every mechanical effect and functional trait that may be used during play.

---

## Character Creation Closure

At the end of character creation, your character should have:

| Element | Status |
| --- | --- |
| Concept | Defined |
| Species | Chosen |
| Background | Chosen |
| Major affinity | Recorded |
| Characteristics | Calculated with species and Synapsis |
| Starting specializations | 3 from background + 1 universal Tenacity choice |
| Preparation | Calculated |
| Resilience | Calculated |
| Endurance | Calculated |
| Sanity | Calculated |
| Personality Traits | Chosen |
| Additional species attributes | Recorded |

With this, the character is ready to enter play.

---

## Example

A player creates an explorer from a species with an Agility bonus.

First, they record every characteristic at `0`. Then they choose species and apply the Agility bonus along with any other characteristics indicated by that species.

Next, they choose a background that grants three starting specializations. They also choose **Acclimation** as the universal Tenacity specialization.

They now have four starting specializations. Each one is level `1`, Novice rank, so each one activates Synapsis and increases its associated characteristic by `+1`.

Only after applying species and Synapsis do they calculate Preparation, Resilience, Endurance, and Sanity.

The order matters because each step modifies the next.
