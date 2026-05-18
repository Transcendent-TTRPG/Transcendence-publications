# Transcendence Technique Cards

Printable tarot-size cards for table play.

## Physical format

- Sheet format: US Letter
- Sheet capacity: up to `4` tarot cards per page
- Card size: `70 mm x 120 mm`
- Intended use: print at `100%`, cut the four cards, and sort them by species or loadout

This means the project should distinguish between:

1. **card source files**
2. **print sheets**

## Storage model

### 1. One card per source file

Each Technique card should exist as its own source file.

Current source root:

- `cards/`

Current example:

- `cards/es/naghii/cerrar-la-linea.html`

Recommended path pattern:

- `cards/<language>/<species-or-group>/<slug>.html`

This makes it easier to:

- keep cards ordered by species
- revise one card without touching a whole print sheet
- review card text in Git
- later generate or assemble sheets automatically

### 2. One or more print sheets

Printable sheets should group up to `4` cards on a US Letter page.

For now:

- `index.html` is the current print sheet prototype

Later this can become:

- one sheet per species batch
- one sheet per player loadout
- or a generated print output assembled from the per-card source files

## Current status

- `Cerrar la Línea` is the current canonical pilot
- the print sheet currently contains only that card
- the remaining space on the page is intentionally blank until more finalized cards are added

## Workflow intent

The long-term intended flow is:

1. authority Technique
2. core-facing final play surface
3. one card source file per Technique
4. print sheet assembly with up to four cards per page

## Usage

Open `index.html` in a browser and print at `100%` scale.
