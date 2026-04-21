# Transcendence Corebook

This folder contains the manuscript structure for the main TTRPG corebook.

## Language Policy

Each section contains:

- `es/` as the source manuscript in Spanish
- `en/` as the mirror translation in English

When content changes in `es/`, the corresponding `en/` file should be updated in the same cycle.

## Current Folder Order

- 00 Project Admin
- 01 Front Matter
- 02 Introduction
- 03 Core Rules
- 04 Character Creation
- 05 Species
- 06 Backgrounds and Origins
- 07 Techniques
- 08 Skills and Proficiencies
- 09 Equipment and Resources
- 10 Conflict and Combat
- 11 Cosmic Horror and Corruption
- 12 GM Toolkit
- 13 Adversaries and Bestiary
- 14 Setting and Factions
- 15 Scenarios and Adventures
- 16 Appendices
- 17 Reference Index
- 98 Layout Export
- 99 Release

This is the current filesystem scaffold. It does not need to match the final reader-facing order.

## Recommended Reader-Facing Order

The corebook should be organized primarily for player onboarding and table use.
The Narrator is expected to read the whole book anyway; the player is not.
For that reason, the reading order should prioritize:

- what the player needs to understand the game
- what the player needs to build a character
- what the player needs to actually play a scene
- only after that, deeper Narrator-facing systems and reference material

Recommended order:

1. 01 Front Matter
2. 02 Introduction
3. 03 Core Rules
4. 08 Skills and Proficiencies
5. 04 Character Creation
6. 05 Species
7. 06 Backgrounds and Origins
8. 10 Conflict and Combat
9. 07 Techniques
10. 09 Equipment and Resources
11. 11 Cosmic Horror and Corruption
12. 12 GM Toolkit
13. 13 Adversaries and Bestiary
14. 14 Setting and Factions
15. 15 Scenarios and Adventures
16. 16 Appendices
17. 17 Reference Index

### Rationale

- `Introduction`, `General Rules`, and `Rolling System` belong early because they teach how play works.
- `Skills and Proficiencies` should appear before deep character detail because specializations are a core identity layer of the game.
- `Character Creation`, `Species`, and `Backgrounds` should come after the player understands rolls and specializations.
- `Conflict and Combat` should come before `Techniques`, because techniques depend on actions, timing, conflict flow, fatigue, rest, and the tactical grammar of play.
- `Equipment and Resources` should come after the core combat engine unless equipment choices are required earlier in character creation.
- `Environmental Conditions` and related scene-pressure logic are structurally important, but more Narrator-facing than player-facing.
- `GM Toolkit`, bestiary, scenarios, and most reference-heavy material belong after the player-facing gameplay core.

## Editorial Note

For now, folder numbering can remain stable for pipeline safety.
If the manuscript continues to mature under this order, a later pass can renumber sections and update references in a controlled migration.
