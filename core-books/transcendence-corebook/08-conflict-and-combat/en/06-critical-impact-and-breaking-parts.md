---
title: "Critical Impact and Breaking Parts"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [critical-impact, breaking-parts, potency, durability, equipment, creature-parts, combat]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/06-impacto-critico-y-romper-partes.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/05-wounds-and-damage.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-actions.md
  - core-books/transcendence-corebook/03-core-rules/en/02-rolling-system-and-competencies.md
  - core-books/transcendence-corebook/10-equipment-and-resources/en/README.md
  - core-books/transcendence-corebook/13-adversaries-and-bestiary/en/README.md
authority_refs:
  - Transcendence-design/docs/system/wounds-and-damage.md
  - Transcendence-design/data/system/wounds-and-damage.yaml
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
  - Transcendence-design/data/system/equipment.yaml
section_modes:
  - heading: "Example: designated critical die"
    writing_mode: example
  - heading: "Example: failed break"
    writing_mode: example
  - heading: "Example: creature part"
    writing_mode: example
---

# Critical Impact and Breaking Parts

**Critical Impact** defines when a hit found an exceptional opening.

**Breaking Parts** defines what that hit can do to a concrete structure: an armor piece, shield, weapon, jaw, natural plate, or any part the encounter has made relevant.

This system does not turn every critical into automatic extra damage. It separates three questions:

1. Did the hit produce Critical Impact?
2. Is there a valid breakable target?
3. Does Critical Potency overcome the target’s Durability?

A critical opens an opportunity. Breaking determines whether that opportunity changes the target’s structure.

---

## Critical Impact

A **Critical Impact** occurs when the designated critical die of the Impact Roll shows its maximum value.

When an Impact Roll uses multiple dice, the attacker designates one die before rolling.

At the table, using a die of a different color is recommended. In digital play, the die may be marked with an equivalent label.

Only that die can validate Critical Impact.

| Impact die | Critical result |
| --- | ---: |
| d4 | 4 |
| d6 | 6 |
| d8 | 8 |
| d10 | 10 |
| d12 | 12 |

The other dice in the Impact Roll add damage or pressure normally. They do not validate a critical by themselves, even if they show their maximum value.

---

## Example: designated critical die

A character rolls `3d8` for Impact.

Before rolling, they declare the red die as the critical die.

If the red die shows `8`, Critical Impact occurs.

If the other two dice show `8` and the red die does not, their values still increase Impact, but no Critical Impact occurs.

---

## What Critical Impact Allows

Critical Impact grants access to critical options defined by the weapon, Technique, target, or encounter.

By default, it can allow:

- attempting to Break Parts against a declared breakable target
- applying critical damage if the NPC model defines it
- triggering a Technique that requires Critical Impact
- applying a physical consequence if the attack, part, or target declares it

Critical Impact does not force a Critical Wound against player characters by itself.

Wound severity still depends on the relation between Impact and Wound Threshold, unless a specific rule increases that severity.

---

## Declaring a Breakable Target

To attempt Breaking Parts, the attacker must declare a breakable target.

The declaration happens before resolving the break. Some Techniques may require the breakable target to be declared before the Attack Roll or before the Impact Roll.

A breakable target must meet three conditions:

1. The attack can reach it.
2. The surface can be broken, disabled, or rendered unusable by that type of force.
3. The scene, creature, equipment, or Technique recognizes that part as relevant.

Valid targets can include:

- weapon
- shield
- armor piece
- held or carried object
- jaw
- horn
- shell
- wing
- tail
- limb
- joint
- natural plate
- vital point
- destructible part defined by the encounter

Ordinary soft tissue is not treated as a breakable structure by default.

It can be the target of damage, Wound, or Ailment, but not of Breaking Parts unless the creature defines that zone as a structure, vital point, or destructible part.

---

## Critical Potency

**Critical Potency** measures whether the hit can break the declared structure.

```text
Critical Potency = Base Potency × Potency Multiplier
```

Base Potency comes from the weapon’s material, construction, or profile.

The Potency Multiplier comes from the weapon type.

If the result produces fractions or decimals, round up unless a specific rule says otherwise.

| Weapon type | Multiplier | Break reading |
| --- | ---: | --- |
| Spears | 80% | Focused point pressure. Better against openings than rigid mass. |
| Axes | 120% | Heavy cutting that opens material and compromises resistant edges. |
| Maces | 150% | Blunt impact against armor, bone, plate, and hard structure. |
| Long blades | 100% | Balance between broad cutting and stable force transfer. |
| Daggers | 50% | High precision, low break power against resistant structures. |
| Short blades | 75% | Fast cutting with moderate break power. |
| Thrown weapons | 40% | Precise contact, little mass for sustained breaking. |
| Ranged weapons | 60% | Puncture or impact at range with limited break power. |
| Flexible weapons | 30% | Control and imbalance more than direct material destruction. |

Concrete Base Potency values belong to the weapon, material, and creature-part catalogs.

This section defines how those values are used, not what Potency each material has.

---

## Resolving the Break

When a valid break attempt exists, compare Critical Potency against Durability.

```text
Critical Potency >= Target Durability
```

| Comparison | Result |
| --- | --- |
| Critical Potency >= Durability | The target breaks, is disabled, or becomes unusable. |
| Critical Potency < Durability | The target does not break and loses `1` Durability. |

Durability loss only occurs during a valid break attempt.

A valid attempt can come from:

- Critical Impact against a declared breakable target
- a Technique that permits breaking without Critical Impact
- a Technique that expands the break-validation range
- a specific weapon, creature, object, or scene rule

A normal attack does not reduce Durability by default.

---

## Example: failed break

An attacker produces Critical Impact and tries to break a shield with Durability `9`.

Their final Critical Potency is `7`.

The shield does not break, but loses `1` Durability and falls to `8`.

Its Block does not change from that loss. The shield keeps functioning until it breaks.

---

## Broken Equipment

A broken equipment piece stops providing the function that depended on its integrity.

If armor, shield, or protection contributed Block, it stops contributing that Block until repaired or replaced.

If a weapon breaks, it cannot be used for normal attacks or Techniques requiring that weapon, unless a rule permits using it while damaged.

Durability loss does not reduce Block gradually.

The piece functions until it breaks. This avoids recalculating smaller values after every hit and keeps the table focused on the moment of rupture.

---

## Breaking and the Current Hit

By default, breaking a piece does not retroactively remove the Block, defense, or effect that piece already contributed to the hit currently being resolved.

The break affects the piece’s state from that moment forward.

A Technique, weapon, creature rule, or specific effect may say otherwise. If it does, it must clearly state that the break affects the current Impact, ignores current Block, or modifies the resolution in progress.

---

## Creature Parts

A creature part can have:

- Defense Roll
- HP
- Block
- Potency
- Durability
- linked abilities

Breaking a part does not only reduce numbers. It changes what the creature can do.

A broken jaw can prevent a breath attack. A broken wing can prevent flight. A broken plate can open a vulnerable point. A broken horn can end a command signal.

The enemy stat block must state:

- which parts exist
- what values they have
- which abilities depend on them
- what happens when a part breaks

Important creatures should be organized into five major locations so the table can read them without getting lost in excessive anatomy.

---

## Example: creature part

An ice wolf has `Jaw` as a breakable part.

That part has its own Durability and supports the `Frost Breath` ability.

If the characters break the Jaw, the wolf cannot use `Frost Breath` while that part remains broken, even if the rest of the creature still has HP.

---

## Techniques and Breaking

Techniques can modify the normal relation between criticals and breaking.

A Technique can:

- allow a break attempt without Critical Impact
- expand the critical die results that validate breaking
- increase Critical Potency
- ignore part of Durability
- declare a part as breakable when it normally would not be
- apply an additional consequence if the break occurs
- make the break affect the current hit

A Technique must state exactly which of these things it allows.

If it only increases damage, it does not allow breaking by itself.

If it only expands break validation, it does not increase Critical Potency.

If it declares a new part as a target, there must still be a credible way to reach it.

---

## Resolution Order

When an attack can generate a break, use this order:

1. Declare the attack and normal target.
2. Declare the breakable target if the rule or Technique requires it.
3. Resolve Attack Roll against Defense Roll.
4. If the attack fails, no break occurs.
5. If the attack connects, make the Impact Roll.
6. Check whether the designated critical die validates Critical Impact, or whether a Technique permits breaking another way.
7. Calculate Critical Potency.
8. Compare Critical Potency against Durability.
9. Apply break or `1` Durability loss.
10. Resolve damage, Wound, HP, phase change, or additional consequence according to the target.

If a rule changes this order, it must say so.

A reactive Technique, trap, creature, or boss part can insert its own steps, but the table must always know when the breakable target was declared and when the break is validated.

---

## Limits

An attack does not break anything just because it was critical.

The target must be:

- reachable
- materially affectable
- relevant to the scene

A light weapon may find criticals often, but fail against high Durability.

A heavy weapon may break hard structures, but not perform the fine work of a dagger.

Weapon choice matters because breaking does not measure the same surface as damage.

Resource extraction rules are not resolved here. If a broken part loses value as material, trophy, or sample, that is defined in the extraction section.

---

## Quick Summary

| Element | Rule |
| --- | --- |
| Critical Impact | Occurs if the designated critical die shows its maximum value. |
| Multiple Impact dice | Only the designated die validates critical. |
| Breaking Parts | Requires Critical Impact or a rule that permits breaking. |
| Breakable target | Must be reachable, affectable, and relevant. |
| Successful break | Critical Potency >= Durability. |
| Failed break | The target loses `1` Durability. |
| Normal attacks | Do not reduce Durability by default. |
| Broken equipment | Loses the function that depended on its integrity. |
| Block | Does not decrease gradually from Durability loss. |
| Current hit | Breaking does not retroactively remove Block or defense unless a specific rule says so. |
