# 08-conflict-and-combat

Language folders:

- es/ source in Spanish
- en/ mirror translation in English

## Recommended Internal Order

This chapter should teach the tactical engine in the order a player needs it:

1. `atb-combat-timeline.md` / `atb-linea-de-tiempo.md`
2. `actions.md` / `acciones.md`
3. `attrition-endurance-fatigue.md` / `desgaste-aguante-fatiga.md`
4. `rest.md` / `descanso.md`

## Purpose Of Each File

### ATB Combat Timeline

Explains the temporal structure of combat:

- opening value
- track position
- rhythm cost
- turn order changes over time

This file should come first because the rest of the combat chapter depends on understanding how time is represented.

### Actions

Explains what a character can do inside that temporal structure:

- active actions
- reactions
- free actions
- base action families

This file should not re-teach the full ATB model. It should assume the reader already understands the track and focus on what actions do, what they cost, and how they differ.

### Attrition, Endurance, and Fatigue

Explains the pressure economy of combat:

- what effort costs
- how much pressure a character can absorb
- when accumulated strain becomes real impairment

This file should come after actions, because attrition only makes full sense once the reader already understands what kinds of actions exist and how often they are taken.

### Rest

Explains how pressure is reduced between scenes:

- short rests
- full rests
- recovery limits
- interruption risk

This file closes the cycle by showing how the tactical system leaves lasting cost and how characters regain margin afterward.

## Editorial Guidance

- `ATB` owns the explanation of timeline, opening, rhythm bands, and why actions reorder combat.
- `Actions` owns the explanation of action categories and base action families.
- `Attrition` owns the explanation of pressure, endurance, fatigue, and action strain.
- `Rest` owns recovery and recovery risk.

To avoid drift:

- do not duplicate full action-cost tables in both `ATB` and `Actions` unless one is clearly a short summary
- do not explain `Techniques` in full inside `Actions`; only define their role and point to their dedicated chapter
- keep Narrator-facing rest-risk tools clearly separated from player-facing recovery rules
