---
title: "Ailments"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 11
status: draft
canonical: false
tags: [ailments, agravios, alterations, afflictions, poisons, infections, curses, conditions, severity]
related:
  - core-books/transcendence-corebook/11-ailments/es/01-agravios.md
  - core-books/transcendence-corebook/11-ailments/en/02-alterations.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/02-attrition-endurance-fatigue.md
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/en/
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Ailments

An **Ailment** is a harmful altered state that settles on a creature and changes how it functions until it is removed, relieved, or naturally ends.

What defines an Ailment is not its source but the nature of the state it creates. An Ailment may come from a creature, a weapon, the environment, prolonged exposure, an object, or a scene hazard. What matters is what the state does once it exists on the target.

---

## Ailment Families

| Family | What it affects |
| --- | --- |
| **Alterations** | Direct physiological disruptions of the body |
| **Afflictions** | Mental, perceptual, or inner-state disruptions |
| **Poisons** | Toxins introduced through a delivery method |
| **Infections** | Biological or contaminant agents that persist in the organism and may spread |
| **Curses** | Hostile extranatural rules bound to beings, objects, places, or ties |

---

## Universal Severity

All Ailments use three severity levels:

- **Minor** (Leve)
- **Moderate** (Moderado)
- **Severe** (Grave)

The three-level structure is the same across all families. What changes at each level depends on the specific Ailment — severity does not always intensify a numeric penalty. In some Ailments it primarily determines what additional restrictions activate, how hard the state is to resist, or how costly it is to remove.

### Default Application Thresholds

Unless the Ailment entry states otherwise, the thresholds for applying or escalating an Ailment by severity are:

| Severity | Base threshold |
| --- | --- |
| Minor | `8 + NR` |
| Moderate | `13 + NR` |
| Severe | `17 + NR` |

### Numeric Penalties and Severity

When an Ailment's main ongoing burden is a **numeric penalty**, that penalty comes from the **rank bonus of the source** that applied it — not from severity alone. In those cases, severity determines what additional restrictions appear and how hard the state is to remove.

More structural or binary Ailments — blindness, paralysis, knockdown, full restraint — use severity primarily for application pressure, recovery difficulty, and persistence rather than scaling a numeric penalty band.

---

## Duration

Ailments do not count rounds. The duration models are:

| Model | Meaning |
| --- | --- |
| `until_removed` | Persists until actively removed |
| `until_trigger` | Ends when a specific condition occurs |
| `scene` | Ends when the hostile scene concludes |
| `while_source_persists` | Ends when the causing source stops acting |
| `while_condition_persists` | Ends when the fictional condition sustaining it disappears |

Duration states how long the Ailment persists. Recovery states what is needed to end or relieve it. These are two separate things.

---

## Strongest Condition Rule

Ailments follow the **strongest condition** rule:

- equal effects never stack in parallel
- a stronger application replaces a weaker one
- an equal application refreshes or resets the existing one if it lasts longer or is harder to remove

The system does not create parallel copies of the same harmful state just because the source changes.

---

## Resistance Roll Formulas

Each Ailment family has its own `R.R.` formula:

| Family | `R.R.` formula |
| --- | --- |
| Alterations | `1d10 + Resilience + Alteration Resistance level + additional bonuses` |
| Afflictions | `1d10 + Composure + Affliction Resistance level + additional bonuses` |
| Curses | `1d10 + Composure + Curse Resistance level + additional bonuses` |
| Poisons | `1d10 + Tenacity + Poison Resistance level + additional bonuses` |
| Infections | `1d10 + Tenacity + Infection Resistance level + additional bonuses` |

---

## Catalogs

Each family has its own catalog of entries:

- Alterations → `02-alterations.md`
- Afflictions → `03-afflictions.md`
- Poisons → `04-poisons.md`
- Infections → `05-infections.md`
- Curses → `06-curses.md`
