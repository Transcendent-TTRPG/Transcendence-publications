---
title: "Publication Visual Style Guide"
type: canon
language: both
status: draft
canonical: true
tags: [style, visual, layout, corebook, character-sheets, cards, print]
related:
  - canon/style-guide.md
  - canon/corebook-writing-checklist.md
  - character-sheets/transcendence-character-sheet/styles/character-sheet.css
  - technique-cards/transcendence-technique-cards/styles/technique-cards.css
  - build/styles/corebook.css
---

# Publication Visual Style Guide

This file defines the shared visual direction for Transcendence publication artifacts.

It governs:

- core book layout;
- character sheets;
- Technique cards;
- future printable aids;
- digital exports that imitate printed material.

The goal is not to make every object look identical. The goal is to make every object feel produced by the same world.

---

## Core Direction

Transcendence publications should feel like functional documents that have passed through an old archive: physical, annotated, worn by handling, but still precise.

The visual language should combine:

- aged paper;
- dark green ink;
- restrained editorial grids;
- sharp ruled tables;
- ritual or archival framing;
- controlled texture;
- minimal ornament;
- high mechanical legibility.

The style should avoid:

- clean white software UI;
- glossy fantasy parchment;
- heavy medieval decoration;
- bright game-card saturation;
- decorative gradients;
- excessive texture behind long reading passages;
- one-note beige or green without contrast.

---

## Family, Not Clones

Each product should use the same material vocabulary at a different intensity.

| Product | Visual role | Texture intensity | Primary need |
| --- | --- | --- | --- |
| Core book | Editorial archive / rule manuscript | Low to medium | Long-form readability |
| Character sheet | Field document / player instrument | Medium | Fast table use and handwriting |
| Technique cards | Tactile object / tactical reference | Medium to high | Identity, quick parsing, future image space |
| Handouts | In-world document when appropriate | Variable | Scene tone and physicality |

### Core book

The core book should be the calmest member of the family.

It can use aged paper and visible texture, but the texture must not fight paragraphs, tables, or examples. Reading endurance matters more than atmosphere.

Use:

- a warm paper base;
- texture-safe accents that do not rasterize each page;
- restrained green rules;
- clear section hierarchy;
- stable table styles;
- rule callouts with quiet contrast;
- decorative elements only at chapter starts, dividers, or major reference blocks.

Avoid:

- heavy texture under every paragraph;
- fine repeating grids, fibers, or noise patterns in exported PDFs;
- dense borders around all content;
- large ornamental frames;
- card-like blocks for ordinary text.

### Character sheets

Character sheets are tools first. They can carry stronger texture because most content is written into boxes, tables, and fixed fields.

Use:

- medium paper texture;
- clear ink borders;
- panel headers;
- ruled tables;
- dense but breathable layout;
- handwriting-friendly empty space.

Avoid:

- texture so dark that pencil becomes hard to read;
- decorative marks inside data fields;
- large atmospheric art that competes with writing space.

### Technique cards

Technique cards can be the most object-like and expressive. They should feel held, sorted, and played.

Use:

- stronger paper texture;
- framed edges;
- compact icon language;
- future image window;
- strong title hierarchy;
- clear mechanical stats;
- short effect text.

Avoid:

- text blocks so large that the card becomes a mini rulebook;
- repeated labels that icons can carry;
- origin or design metadata that players do not use at the table.

---

## Palette

Use a narrow but not monochrome palette.

### Core tokens

| Token | Use | Suggested value |
| --- | --- | --- |
| `paper` | primary paper surface | `#efe8d5` |
| `paper-light` | softer field / table cell | `#f7f1df` |
| `paper-shadow` | outer page surround | `#d8d2bf` |
| `ink` | main text | `#102016` |
| `ink-soft` | secondary text | `#395d40` |
| `rule` | borders and table lines | `#385f3d` |
| `rule-soft` | thin internal lines | `rgba(56, 95, 61, 0.62)` |
| `dark-panel` | table headers / strong labels | `#142c18` |
| `warm-mark` | stains, age, low contrast warmth | `rgba(113, 84, 45, 0.13)` |

### Accent guidance

Accent colors should be muted and material-based:

- oxidized green;
- dark umber;
- dull teal;
- old brass;
- dried blood only for severe warning elements.

Do not use saturated neon, bright elemental colors, or purple-blue gradients as the general brand surface. Elemental or spectrum-specific accents may appear in diagrams or cards, but should be constrained.

---

## Texture

Texture should suggest paper grain, not visual noise.

The current printable artifacts use layered CSS backgrounds:

- faint square grid;
- thin diagonal fibers;
- low-opacity radial stains;
- soft paper base.

This is the correct direction.

### Recommended intensity

| Artifact | Grid | Fiber | Stains | Notes |
| --- | --- | --- | --- | --- |
| Core book | very faint | faint | rare and pale | long reading surface |
| Character sheet | faint | visible | moderate | supports physical sheet identity |
| Technique card | visible | visible | moderate | small object, less reading fatigue |

### Print rule

All backgrounds must be tested with:

```css
-webkit-print-color-adjust: exact;
print-color-adjust: exact;
```

If print output becomes muddy, reduce opacity before changing the palette.

---

## Typography

The current pairing is approved:

- `Cinzel` for titles, headings, panel labels, table headers;
- `Crimson Text` for body, rules, examples, and long reading.

### Usage

| Type | Font | Rule |
| --- | --- | --- |
| Chapter title | Cinzel | uppercase, spacious, strong hierarchy |
| Section heading | Cinzel | clear but not oversized |
| Panel/table heading | Cinzel | compact uppercase |
| Body text | Crimson Text | readable line length and generous leading |
| Rule example | Crimson Text | direct, not ornamental |
| Mechanical term | Body font or bold | do not over-style canonical terms |

Letter spacing should stay modest. Avoid negative letter spacing.

---

## Layout Principles

### Core book

Use a book layout, not a worksheet layout.

Default rules:

- generous margins;
- readable line length;
- clear H1/H2/H3 hierarchy;
- tables only when they improve lookup;
- callouts for examples, designer notes, warnings, and rule summaries;
- avoid putting every subsection inside a bordered box.

### Character sheets

Use dense tables and panels.

Default rules:

- fixed page size;
- stable rows;
- no shifting content;
- boxes sized for handwriting;
- repeated tracking elements should be compact;
- icons only where they speed recognition.

### Cards

Use compact object layout.

Default rules:

- title first;
- rank below title;
- future image space preserved;
- icon stat grid;
- requirements short;
- effect short enough to read during play.

---

## Component Guidance

### Tables

Tables should use dark green headers with light text when lookup speed matters.

Core book tables should be calmer than sheet tables:

- thinner borders;
- less saturated row fills;
- more padding for reading.

Character sheet and card tables can be denser:

- stronger borders;
- smaller type;
- more fixed dimensions.

### Rule callouts

Use callouts for:

- rule summaries;
- examples;
- narrator-facing warnings;
- important edge cases.

Do not use callouts for every paragraph.

Suggested callout families:

| Class | Use | Tone |
| --- | --- | --- |
| `rule-summary` | compact rule recap | precise |
| `example` | table scenario | concrete |
| `narrator-note` | adjudication guidance | restrained |
| `danger` | severe consequence | rare |
| `reference` | lookup-only block | dense |

### Icons

Icons belong primarily in cards, sheets, and quick references.

In the core book, icons should be rare and functional:

- chapter navigation;
- reference tags;
- repeated mechanical categories;
- diagrams.

Do not replace prose headings with icons in the core book.

---

## Core Book Adaptation Plan

The core book should inherit the same physical material language as the sheets and cards, but softened.

Recommended changes to `build/styles/corebook.css`:

1. Move core colors into `:root` tokens matching sheets and cards.
2. Change the page background from clean grey-green to aged paper.
3. Apply the paper texture to the reading page, not only the browser background.
4. Reduce texture opacity inside long text areas.
5. Update table fills to translucent paper panels instead of flat green-grey.
6. Add callout classes before heavy layout work begins.
7. Keep chapter headers strong, but avoid making every section feel like a card.

This should be done gradually and tested through PDF export after each major pass.

---

## Shared CSS Token Direction

All printable artifacts should converge on similar names:

```css
:root {
  --paper: #efe8d5;
  --paper-light: #f7f1df;
  --paper-panel: rgba(249, 243, 226, 0.52);
  --paper-cell: rgba(246, 239, 217, 0.34);
  --ink: #102016;
  --ink-soft: #395d40;
  --rule: #385f3d;
  --rule-soft: rgba(56, 95, 61, 0.62);
  --dark-panel: #142c18;
}
```

Individual artifacts may add local tokens, but should not invent unrelated palettes unless the product has a specific reason.

---

## Review Checklist

Before approving a visual pass:

- [ ] It belongs to the same material family as sheets and cards.
- [ ] It is still readable when printed.
- [ ] It does not rely on atmosphere to carry rules clarity.
- [ ] Tables remain scannable.
- [ ] Empty spaces serve writing, rest, or hierarchy.
- [ ] Texture does not overpower body text.
- [ ] The palette is not a single hue repeated at different brightness levels.
- [ ] Mechanical reference blocks are faster to use than plain prose.
- [ ] The artifact has a clear role: book, sheet, card, or handout.

---

## Current Decision

Use the same visual family across the core book, character sheets, and Technique cards.

Do not use the same intensity everywhere.

The sheets and cards can feel more tactile. The core book should feel like the same archive translated into a long-form reading object.
