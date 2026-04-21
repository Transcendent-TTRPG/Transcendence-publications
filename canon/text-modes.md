---
title: "Text Modes"
type: canon
language: both
status: draft
canonical: true
tags: [writing, prose, narrative, rules, examples, editorial]
related:
  - canon/style-guide.md
  - canon/voice-samples.md
  - canon/glossary.md
---

# Text Modes

This file defines the approved writing modes for Transcendence publications.
Its purpose is operational: an agent or contributor should be able to decide what kind of text to write before drafting the paragraph.

Use this file to answer:

- what the passage is trying to do
- what kind of information it is allowed to contain
- what it must avoid
- how it should relate to adjacent passages

If a passage is unclear, decide its mode first. Do not write until the mode is explicit.

---

## Core rule

Choose one primary mode per passage.

A file may contain multiple modes, but a single paragraph or table should not try to perform more than one primary function at once.

When a passage needs both explanation and atmosphere, separate them explicitly:

1. rules or description first
2. example or flavor second

Do not blend system explanation and atmospheric narration in the same paragraph.

`writing_mode` is declared at file level and should describe the dominant mode of the document.
When a file is structurally mixed, use `section_modes` in frontmatter to mark the sections
that intentionally diverge from that dominant mode.

---

## Mode summary

| Mode | Primary purpose | Common location |
| --- | --- | --- |
| `rules` | Define mechanics, procedures, constraints, formulas | Corebook rules chapters, supplements |
| `example` | Show how a rule or process applies in a concrete situation | Corebook side examples, teaching passages |
| `description` | Present observable state, environment, object, place, or condition without unfolding a full dramatic scene | Setting text, environment passages, item/location presentation |
| `narrative` | Present events unfolding through perception and consequence | Fiction passages, in-world scene fragments, atmospheric inserts |
| `flavor` | Add brief tonal or in-world texture without carrying mechanical explanation | Blockquotes, chapter openers, brief inserts |
| `reference` | Summarize or index information for lookup speed | Appendices, tables, indexes, quick references |

---

## Rules

**Use when:** the reader must understand how the game works, what choices exist, what a term means, or what consequence follows from an action.

**Goal:** enable decisions and remove ambiguity.

**Allowed:**

- definitions
- formulas
- procedures
- thresholds
- costs
- restrictions
- consequences
- explicit exceptions

**Avoid:**

- atmosphere for its own sake
- unexplained metaphors
- emotional framing
- hidden implications that the reader must infer

**Shape:**

- short to medium declarative sentences
- one mechanism or consequence per sentence
- one rule cluster per paragraph
- close on the trade-off, limitation, or operational consequence

**When not to use:**

- when the goal is to show felt experience rather than define mechanics
- when a concrete example would teach better than another abstract explanation

---

## Example

**Use when:** the reader already has or is being given a rule, and now needs to see how that rule behaves in practice.

**Goal:** bridge rule and application.

**Allowed:**

- concrete actors
- explicit sequence of events
- actual values or plausible sample values
- brief situational framing

**Avoid:**

- unresolved atmosphere
- hidden mechanics
- introducing new canonical information not already defined in rules

**Shape:**

- concrete and brief
- no atmosphere-heavy language
- no ambiguity about what is happening
- ideally follows the rule it illustrates

**Rule of use:**

If a mechanic is easy to misread, use an example.
If the passage is emotionally evocative but not pedagogically useful, it is not an example; it is flavor or narrative.

---

## Description

**Use when:** the text needs to present what something is like in an observable, stable way without turning the passage into a dramatic scene.

**Goal:** orient the reader to a place, object, state, creature, or condition.

**Allowed:**

- physical properties
- observable behavior
- stable spatial or sensory relationships
- measured contrast between expected and actual state

**Avoid:**

- full event progression
- interiority unless the text is explicitly viewpoint-bound
- explaining hidden causes
- generic mood adjectives without physical grounding

**Shape:**

- centered on what can be perceived
- usually static or slow-changing
- strong fit for environment, item, faction, or phenomenon presentation

**Difference from narrative:**

Description presents a state.
Narrative presents change over time.

---

## Narrative

**Use when:** the passage must show events unfolding through perception, action, reaction, and consequence.

**Goal:** guide lived experience, not explain systems.

**Allowed:**

- sensory perception
- temporal progression
- character response
- unresolved tension
- anomaly, pressure, or consequence when appropriate to the scene

**Avoid:**

- explaining mechanics directly
- stating hidden causes the viewpoint cannot know
- mixing unrelated sensory channels without purpose
- decorative metaphor stacks

**Shape:**

- one active perceptual thread per paragraph
- progression from base state to deviation to consequence
- physical, restrained language

**Important scope rule:**

Not every narrative paragraph in the whole project must contain an extranatural anomaly.
That requirement applies strongly to horror-facing or Limbo-facing passages.

For ordinary fiction scenes, the paragraph still needs a perceivable point of tension, change, pressure, or consequence — but not necessarily an anomalous phenomenon.

---

## Flavor

**Use when:** the passage exists to reinforce tone, worldview, or atmosphere in a compact way.

**Goal:** add texture without carrying rule logic.

**Allowed:**

- short in-world lines
- chapter openers
- brief mood-setting blockquotes
- compact atmospheric inserts

**Avoid:**

- carrying essential mechanics
- replacing definitions
- becoming so long that it turns into narrative without structure

**Shape:**

- short
- optional to read without losing comprehension
- usually set apart visually

---

## Reference

**Use when:** the reader needs fast retrieval, not cadence or atmosphere.

**Goal:** maximize lookup speed.

**Allowed:**

- tables
- lists
- condensed definitions
- indexes
- quick comparisons

**Avoid:**

- rhetorical buildup
- atmospheric prose
- repeated explanation already covered elsewhere

**Shape:**

- dense but clear
- highly structured
- optimized for scanning

---

## Decision tree

Use this decision order before drafting:

1. If the reader needs to operate a mechanic, write `rules`.
2. If the reader needs to see a mechanic applied, write `example`.
3. If the reader needs to understand what something is like, write `description`.
4. If the reader needs to experience events unfolding, write `narrative`.
5. If the reader only needs tonal reinforcement, write `flavor`.
6. If the reader needs quick retrieval, write `reference`.

If two answers seem true, split the passage.

---

## Mixing modes inside one file

These combinations are valid:

- `rules` -> `example`
- `description` -> `flavor`
- `description` -> `rules`
- `reference` -> short `rules`

These combinations should usually be split instead of blended:

- `rules` + `narrative` in one paragraph
- `example` + `flavor` in one paragraph
- `reference` + `narrative` in one section

---

## Mapping by product type

### Corebook

- default modes: `rules`, `example`, `reference`
- secondary modes: `description`, `flavor`
- `narrative` should be deliberate and usually short unless the chapter explicitly calls for scene text

### Supplement

- default modes depend on supplement type
- mechanical supplements lean toward `rules` and `reference`
- world supplements lean toward `description` with controlled `flavor`

### Novel / light fiction

- default modes: `narrative`, `description`, `flavor`
- `rules` should not appear in-story except as diegetic exposition transformed into fiction

---

## Agent instructions

Before writing:

1. Name the mode.
2. Confirm the mode matches the file purpose.
3. Load the required canon files.
4. Draft only within that mode's allowed behaviors.

If the passage starts drifting, stop and reclassify it before continuing.
