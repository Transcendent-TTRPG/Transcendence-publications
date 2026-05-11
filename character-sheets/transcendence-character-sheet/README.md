# Transcendence Character Sheet

Printable character sheet prototype for tabletop play.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Printable sheet prototype: page 1 for character core, page 2 for table rolls, page 3 for competencies |
| `styles/character-sheet.css` | Print-first visual styling |

## Open

Open `index.html` directly in a browser.

## Print

Use the browser print dialog and select:

| Setting | Value |
| --- | --- |
| Paper size | Letter |
| Scale | 100% |
| Margins | Default or none |
| Background graphics | Enabled |

## Notes

- `Aguante` uses the formula from `Transcendence-design/data/system/attrition-fatigue.yaml`: `3 + (TEN * 2)`.
- `Cordura` is shown as `CMP * 2`, matching the current equipment dependency note. It should eventually move into a dedicated character or sanity rules source.
- Page 2 keeps attack names free so natural weapons and manufactured weapons can share the same space.
- Page 2 currently models medium armor defense as full Evasion and half Agility, and heavy armor as half Evasion and zero Agility, matching the current candidate rebalance in the design docs.
- Page 3 uses two specialization blocks of 16 rows each so the sheet exports as 3 pages at Letter / 100% scale.
