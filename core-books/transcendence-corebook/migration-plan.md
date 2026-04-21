---
title: "Corebook Migration Plan"
type: admin
content_kind: reference
writing_mode: reference
language: en
chapter: 0
status: draft
canonical: false
tags: [migration, restructuring, editorial, corebook, chapter-order]
related:
  - core-books/transcendence-corebook/README.md
---

# Corebook Migration Plan

This document defines the planned structural migration of the `transcendence-corebook` manuscript from the current scaffold order to the intended reader-facing order.

Its purpose is to let the manuscript mature under a stable editorial plan before physical folder renumbering begins.

## Current Principle

The corebook should be organized primarily for player readability and onboarding.

The Narrator is expected to read the entire book. The player is not.

Because of that, the structure should prioritize:

1. how the game works
2. how a player builds a character
3. how a player acts in scenes
4. only after that, deeper Narrator-facing systems and reference material

## Target Reader-Facing Order

1. `01-front-matter`
2. `02-introduction`
3. `03-core-rules`
4. `08-skills-and-proficiencies`
5. `04-character-creation`
6. `05-species`
7. `06-backgrounds-and-origins`
8. `10-conflict-and-combat`
9. `07-techniques`
10. `09-equipment-and-resources`
11. `11-cosmic-horror-and-corruption`
12. `12-gm-toolkit`
13. `13-adversaries-and-bestiary`
14. `14-setting-and-factions`
15. `15-scenarios-and-adventures`
16. `16-appendices`
17. `17-reference-index`

## Future Folder Order

This is the recommended physical order once the migration actually happens.

1. `01-front-matter`
2. `02-introduction`
3. `03-core-rules`
4. `04-skills-and-proficiencies`
5. `05-character-creation`
6. `06-species`
7. `07-backgrounds-and-origins`
8. `08-conflict-and-combat`
9. `09-techniques`
10. `10-equipment-and-resources`
11. `11-cosmic-horror-and-corruption`
12. `12-gm-toolkit`
13. `13-adversaries-and-bestiary`
14. `14-setting-and-factions`
15. `15-scenarios-and-adventures`
16. `16-appendices`
17. `17-reference-index`

## Chapter Mapping

| Current folder | Planned folder | Reason |
| --- | --- | --- |
| `01-front-matter` | `01-front-matter` | unchanged |
| `02-introduction` | `02-introduction` | unchanged |
| `03-core-rules` | `03-core-rules` | remains first rules block |
| `04-character-creation` | `05-character-creation` | moves after specializations |
| `05-species` | `06-species` | follows character creation |
| `06-backgrounds-and-origins` | `07-backgrounds-and-origins` | follows species |
| `07-techniques` | `09-techniques` | moves after combat block |
| `08-skills-and-proficiencies` | `04-skills-and-proficiencies` | becomes early player-facing identity chapter |
| `09-equipment-and-resources` | `10-equipment-and-resources` | moves after techniques |
| `10-conflict-and-combat` | `08-conflict-and-combat` | becomes central tactical block |
| `11-cosmic-horror-and-corruption` | `11-cosmic-horror-and-corruption` | unchanged |
| `12-gm-toolkit` | `12-gm-toolkit` | unchanged |
| `13-adversaries-and-bestiary` | `13-adversaries-and-bestiary` | unchanged |
| `14-setting-and-factions` | `14-setting-and-factions` | unchanged |
| `15-scenarios-and-adventures` | `15-scenarios-and-adventures` | unchanged |
| `16-appendices` | `16-appendices` | unchanged |
| `17-reference-index` | `17-reference-index` | unchanged |

## Internal Ordering Decisions Already Made

### `03-core-rules`

This block is considered mature enough to remain early in the book.

Its active internal order is:

1. `01-general-rules`
2. `02-rolling-system-and-competencies`
3. `03-environmental-conditions`

### `08-skills-and-proficiencies`

This chapter has already been adjusted to function as an early player-facing chapter:

- onboarding language improved
- starting specializations surfaced earlier
- `Techniques` mention softened so it does not depend on later tactical detail

### `04-character-creation`

This chapter has already been adjusted to function more independently:

- practical process summary added
- chapter made more self-guiding
- editorial “incomplete chapter” language removed from the manuscript

### `10-conflict-and-combat`

Its recommended internal order is:

1. `ATB: Línea de Tiempo de Combate`
2. `Acciones`
3. `Desgaste, Aguante y Fatiga`
4. `Descanso`

Ownership by file:

- `ATB` explains time, opening, rhythm bands, and initiative flow
- `Actions` explains action categories and base action families
- `Attrition` explains effort pressure, endurance, and fatigue
- `Rest` explains recovery and recovery risk

## Preconditions Before Physical Migration

Do not renumber folders until all of the following are true:

1. The target reader-facing order is considered final for this version.
2. `03`, `04`, `08`, and `10` are editorially stable enough to keep their new positions.
3. The role of `07-techniques` and `09-equipment-and-resources` is clear enough to place them confidently after combat.
4. No additional large structural inversions are expected in the player-facing half of the book.

## What Must Be Updated During Migration

When the actual renumbering happens, the following must be updated in the same cycle:

- folder names
- chapter numbers in frontmatter
- `related` paths
- chapter READMEs
- root `README.md`
- references inside manuscript prose that mention chapter numbers or names
- build scripts and export order if they depend on current folder numbering
- layout / TOC configuration
- any `Transcendence-design` references that still point to old publication paths
- any release or packaging scripts that assume current ordering

## Migration Sequence

Recommended execution order:

1. create a clean commit before restructuring
2. rename folders in one controlled pass
3. update frontmatter chapter numbers
4. update `related` paths and internal references
5. update `README` files and table-of-contents sources
6. run `./pipeline/scripts/editorial-check.sh`
7. build HTML/PDF outputs
8. manually review the generated TOC and chapter order
9. only then commit the structural migration

## What Not To Do

- do not move folders gradually across many unrelated commits
- do not renumber chapters before the intended order is frozen
- do not leave mixed old/new chapter numbers in frontmatter
- do not rely on memory to update references; use a tracked migration pass

## Current Status

This migration is planned but not yet executed.

The manuscript may continue to mature under the target reader-facing order while the filesystem remains unchanged.
