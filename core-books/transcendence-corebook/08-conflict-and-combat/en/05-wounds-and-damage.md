---
title: "Wounds and Damage"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 8
status: draft
canonical: false
tags: [wounds, damage, impact, block, critical-impact, injury, combat]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/05-heridas-y-dano.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/06-critical-impact-and-breaking-parts.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-actions.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/04-rest.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-attrition-endurance-fatigue.md
  - core-books/transcendence-corebook/03-core-rules/en/02-rolling-system-and-competencies.md
authority_refs:
  - Transcendence-design/docs/system/wounds-and-damage.md
  - Transcendence-design/data/system/wounds-and-damage.yaml
  - Transcendence-design/docs/system/roll-types.md
  - Transcendence-design/docs/system/equipment-overview.md
  - Transcendence-design/docs/system/ailments.md
section_modes:
  - heading: "Example"
    writing_mode: example
  - heading: "Progression examples"
    writing_mode: example
---

# Wounds and Damage

Wounds define what happens when an attack surpasses defense. They do not replace the Attack Roll or the Impact Roll. They enter afterward, when effective contact exists and the scene needs to know which body zone, equipment piece, or creature part carried the consequence.

Transcendence separates two damage surfaces. When a player character strikes an NPC, creature, or monster, the attack uses the target's damage model. When an NPC strikes a player character, the hit is recorded as a localized wound by zone.

This split lets enemies use HP, zones, phases, breakable parts, or vital points of their own, while player characters do not depend on a general life bar. A received hit leaves a physical mark. That mark occupies space, limits function, and can collapse a zone.

---

## Attack Flow

A physical attack follows this sequence:

1. The attacker declares the attack.
2. Resolve the Attack Roll against the target's Defense Roll.
3. If the Attack Roll does not beat the Defense Roll, the attack does not connect effectively.
4. If the attack connects, the attacker makes the Impact Roll.
5. Determine the applicable Block.
6. Convert the result into damage, wound, break, or effect according to the target.

The Impact Roll is not made if the attack does not find an opening. Defense decides whether the hit connects. Block decides how much of that pressure reaches the body, piece, or part struck.

---

## Impact Roll

The Impact Roll measures the pressure transmitted by the attack after it surpasses defense.

```text
Impact = (Competency Rank x Weapon Damage) + (Associated Characteristic x Weapon Grade)
```

Impact is not only raw force. It includes mass, angle, execution, weapon quality, contact point, and the attacker's ability to turn an opening into consequence.

---

## Critical Impact

Critical Impact occurs when the designated critical die of the Impact Roll shows its maximum value.

If the Impact Roll uses multiple dice, the attacker must designate one before rolling. At the table, use a die of a different color. In digital play, the die may be marked with an equivalent label. Only that die validates Critical Impact; the other dice add Impact normally.

| Impact die | Critical result |
| --- | ---: |
| d4 | 4 |
| d6 | 6 |
| d8 | 8 |
| d10 | 10 |
| d12 | 12 |

Weapons with smaller dice generate criticals more often. Weapons with larger dice generate criticals less often, but usually transmit more Impact. Increasing rank raises total Impact, but does not increase critical chance by itself, because only the designated die can validate it.

A Critical Impact can allow the attacker to:

- apply critical damage against an NPC if its model defines it;
- attempt to break a part, equipment piece, or protection;
- trigger a Technique that requires Critical Impact;
- apply a physical consequence if the attack or target declares it.

Critical Impact does not grant a universal list of effects. The weapon, Technique, target, or scene defines which options are available.

---

## Critical Potency

Critical Potency measures the weapon's ability to break, deform, open, or disable a resistant structure during a Critical Impact.

```text
Critical Potency = Base Potency x Weapon Potency Multiplier
```

Base Potency comes from the weapon's material, construction, or profile. The multiplier depends on weapon type and expresses how that weapon transmits force on a critical.

| Weapon type | Multiplier | Ideal use |
| --- | ---: | --- |
| Spears | 80% | Piercing small points and light protections. |
| Axes | 120% | Opening material and splitting rigid surfaces. |
| Maces | 150% | Breaking heavy armor and crushing resistant structures. |
| Long blades | 100% | Broad cuts against medium-resistance surfaces. |
| Daggers | 50% | Frequent criticals against vulnerable or unprotected zones. |
| Short blades | 75% | Fast attacks with moderate potency. |
| Thrown weapons | 40% | Precise ranged impacts with low structural break power. |
| Ranged weapons | 60% | Puncture or impact from range. |
| Flexible weapons | 30% | Control, restraint, and imbalance. |

Material does not necessarily change a weapon's damage die. An iron khopesh and an adamantium khopesh may use the same base damage. The difference appears in Potency and Durability: the first may cut the same way, but the second breaks better and resists longer.

---

## Breaking Parts

Breaking Parts is a strategic option available when an attack produces Critical Impact and a breakable target has been declared.

The target must be something the attack can plausibly reach and affect: a weapon, shield, armor piece, limb, jaw, horn, shell, tail, wing, joint, vital point, or destructible part defined by the encounter.

To resolve the break, compare Critical Potency against Durability.

```text
Critical Potency >= Target Durability
```

| Comparison | Result |
| --- | --- |
| Critical Potency >= Durability | The part breaks, is disabled, or becomes unusable. |
| Critical Potency < Durability | The part does not break and loses 1 Durability. |

Durability loss only occurs during a valid break attempt: through Critical Impact, through a Technique that permits breaking without a critical, or through a specific attack rule. Normal attacks do not reduce Durability by default.

If a broken piece contributed Block, it stops contributing Block until repaired or replaced. Durability loss does not reduce Block by itself; the piece functions until it breaks, unless a rule says otherwise.

Breaking a part can disable an attack option, reduce defense, destroy equipment, prevent a dependent Technique, reduce mobility, alter a behavior pattern, open a vulnerable point, or change an encounter phase.

---

## Block

When a hit connects against a protected zone, that zone contributes Block.

```text
Block = BB + MB + DC + PQ
```

| Component | Meaning |
| --- | --- |
| BB | Base Block by armor category. |
| MB | Material Bonus. |
| DC | Defensive Competency with the armor in the zone. |
| PQ | Piece quality or grade. |

| Armor | BB |
| --- | ---: |
| Light | 2 |
| Medium | 4 |
| Heavy | 6 |

```text
MB = floor(Durability / 5)
```

Defensive Competency equals the competency level in the armor type protecting the struck zone. It only applies if that armor is actually participating in absorbing the Impact.

---

## Players Against NPCs

When a player character strikes an NPC, creature, monster, or adversary, the attack uses the target's damage model.

```text
Effective Damage = Impact - Target Block
```

That damage applies to the HP, reserve, zone, vital point, phase, or subsystem the enemy defines.

A common enemy may use simple HP. An important creature may have zones with their own values. A champion may use vital points, breakable parts, and phases that change when a structure falls.

Critical Impact resolves against that model. Not every enemy needs breakable parts, but enemies that have them must state what happens when a part breaks.

---

## NPCs Against Players

When an NPC strikes a player character, general HP is not used. The hit is recorded as a wound in the struck zone.

Resolve in this order:

1. Determine the struck zone.
2. Identify the armor in that zone.
3. Resolve the Defense Roll with the Agility applicable to that armor.
4. If the attack connects, roll Impact.
5. Calculate the zone's Block.
6. Compare Impact against Block.
7. Record the wound if applicable.

| Relation | Result | Slots |
| --- | --- | ---: |
| Impact <= Block x 1 | No wound | 0 |
| Impact > Block x 1 and < Block x 2 | Light Wound | 1 |
| Impact >= Block x 2 and < Block x 3 | Severe Wound | 2 |
| Impact >= Block x 3 | Critical Wound | 3 |

A Critical Wound does not force a Resistance Roll by default. It already occupies 3 slots and can saturate or collapse a zone by itself.

A Resistance Roll is only forced if:

- the Critical Wound causes Collapse in a vital zone, such as Head or Torso;
- the attack, NPC, or Technique says so;
- the associated Ailment requires a Resistance Roll;
- the Narrator declares it due to an extreme scene circumstance.

The Resistance Roll used by vital Collapse is an Alteration Resistance Roll. It represents bodily shock, functional loss, internal trauma, or physical interruption of the body.

---

## Wound Slots

Each character zone has a number of wound slots.

| Zone | Slots |
| --- | ---: |
| Head | 3 |
| Torso | 5 |
| Arms | 4 |
| Legs | 4 |
| Feet | 3 |

A wound always attempts to occupy its full slots in the struck zone.

If the zone has enough free slots, mark them normally. If it does not have enough free slots, mark the remaining slots and the excess causes Overflow.

| Zone state | Condition | Effect |
| --- | --- | --- |
| Functional | The zone has at least 1 free slot. | Applies no zone penalty by itself. |
| Saturated | The zone reached its slot maximum exactly. | Applies Saturation Penalty. |
| Collapsed | A wound did not fit fully, or a Saturated zone received another wound. | Applies that zone's Collapse effect. |

### Example

A character has Torso at 4 of 5 occupied slots. They receive a Severe Wound to the Torso, which should occupy 2 slots. Only 1 slot remains free, so that slot is marked and the other produces Overflow. The Torso becomes Collapsed.

---

## Saturation Penalty

When a zone is Saturated, its base penalty equals the number of occupied slots in that zone.

```text
Saturation Penalty = occupied slots in the zone
```

| Saturated zone | Base penalty |
| --- | ---: |
| Head | -3 |
| Torso | -5 |
| Arms | -4 |
| Legs | -4 |
| Feet | -3 |

This penalty only applies to rolls and actions that clearly depend on that zone. It is not a universal character penalty.

| Zone | Saturated | Collapsed |
| --- | --- | --- |
| Head | Saturation Penalty to mental Specialization Rolls and visual or auditory perception. Saturation Penalty to Preparation. | Applies Stunned. The character must pass an Alteration Resistance Roll against the severity of the wound that caused Collapse or become Unconscious. |
| Torso | Saturation Penalty to Tolerance, demanding physical actions, heavy defenses, holding posture under Impact, and Techniques that strain the torso. | The character becomes Incapacitated until stabilized. If the wound that caused Collapse was Critical, they also enter Agony. |
| Arms | Saturation Penalty to Attack Rolls, Impact Rolls, and physical Specialization Rolls that depend on arms, grip, shield, weapons, or manipulation. | One arm, grip, or execution line becomes unusable. The character cannot use two-handed weapons, shields, or limb-dependent Techniques if they rely on that collapsed part. May apply Impeded. |
| Legs | Movement is halved. Saturation Penalty to Strength or Tenacity physical Specialization Rolls that depend on legs. | The character cannot walk functionally without support or help. They cannot charge, run, or jump. |
| Feet | The character cannot sprint. Saturation Penalty to Agility physical Specialization Rolls that depend on fine footing. | The character can move only with support, help, or an appropriate Specialization Roll. If they try to move under pressure without support and fail, they become Knocked Down. |

The suggested difficulty for the Resistance Roll caused by Collapse depends on the wound that produced Overflow.

| Wound that caused Collapse | Difficulty |
| --- | --- |
| Light | Challenging |
| Severe | Rigorous |
| Critical | Demanding |

---

## Body States

Body States describe a creature's general condition once damage is no longer only local.

| State | Meaning |
| --- | --- |
| Operational | Can act with any penalties from zone, Ailment, Fatigue, or Attrition. |
| Incapacitated | Cannot perform meaningful actions. May speak, crawl, hold something, or react weakly if the fiction permits. |
| Unconscious | Cannot act or perceive usefully. Cannot defend actively. |
| Agony | At risk of dying without stabilization. Cannot act meaningfully. |
| Dead | The creature cannot be recovered by normal scene-level means. |

If a zone that is already Collapsed receives another wound, apply or refresh the zone's Collapse effect. If the zone is Head or Torso, the character must pass an Alteration Resistance Roll against the severity of the new wound. On failure, Head escalates toward Unconscious and Torso escalates toward Agony.

If a character in Agony receives another Critical Wound to Head or Torso, they die unless a specific rule, Technique, immediate intervention, or table decision establishes another outcome.

---

## Zones and Location

For NPC attacks against player characters, location is determined before resolving defense. This prevents the Narrator from always choosing the most damaged zone.

| 1d100 | Zone |
| --- | --- |
| 01-04 | Head |
| 05-10 | Feet |
| 11-45 | Torso |
| 46-65 | Arms |
| 66-100 | Legs |

Player attacks against NPCs do not use this table by default. The player declares target, intent, Technique, or vulnerable point according to what the scene and available information allow.

---

## Stabilize, Treat, and Heal

Transcendence separates three recovery steps.

| Step | Function | Frees slots |
| --- | --- | ---: |
| Stabilize | Stops immediate deterioration, active shock, open bleeding, or Collapse that keeps worsening. | No |
| Treat | Cares for a zone during a Full Rest to prepare recovery. | Not by itself |
| Heal | Frees occupied slots through Full Rest with successful treatment. | Yes |

Medicine covers stabilization, treatment, and healing of bodily damage. Herbalism, alchemy, objects, Techniques, and artifacts may modify these rules from their own sections.

### Stabilization

To stabilize a wound, a character makes a Medicine Specialization Roll with Wisdom.

| Wound | Difficulty | Required kit | Time |
| --- | --- | --- | --- |
| Light | Challenging | Basic | 30 minutes |
| Severe | Rigorous | Advanced | 60 minutes |
| Critical | Demanding | Specialized | Full Rest |

On success, the wound is stabilized. Its immediate effects stop worsening. On failure, the wound remains active and the attempt may consume time, resources, or create a complication if the scene remains under pressure.

### Treatment and healing

Wounds must be stabilized before slots can be freed. An active wound must be stabilized first.

| Rest | Can stabilize | Can treat | Can free slots |
| --- | --- | --- | ---: |
| 30 minutes | Light Wound | No | 0 |
| 60 minutes | Severe Wound | No | 0 |
| Full Rest | Critical Wound or any stabilized wound | Yes, with Medicine | 1 slot per treated character |

When treating a zone during a Full Rest, the character caring for the patient makes a Medicine Specialization Roll with Wisdom. The base difficulty and required kit depend on the most severe slot still occupied in that zone.

| Most severe occupied slot | Difficulty | Required kit |
| --- | --- | --- |
| Light | Challenging | Basic |
| Severe | Rigorous | Advanced |
| Critical | Demanding | Specialized |

Then increase the Reference Level according to how many slots are occupied in the same zone at the start of the Full Rest.

| Occupied slots in the zone | Adjustment |
| ---: | --- |
| 1 | No adjustment |
| 2-3 | +1 Reference Level |
| 4-5 | +2 Reference Level |
| Collapsed zone | +1 additional Reference Level |

On success, the patient frees 1 occupied slot from that zone. The freed slot must belong to a stabilized wound. On failure, the zone frees no slots.

When several stabilized wounds exist in the same zone, the treating character declares which slot they are trying to free before rolling. The Narrator may require the most severe wound to be reduced first if that injury maintains Agony, Collapse, or dominant functional loss.

### Progression examples

A Light Wound occupies 1 slot. If it is stabilized and receives successful treatment during a Full Rest, it frees that slot and disappears.

A Severe Wound occupies 2 slots. After a Full Rest with successful treatment, it frees 1 slot and becomes a Light Wound. It needs another Full Rest with successful treatment to disappear.

A Critical Wound occupies 3 slots. After a Full Rest with successful treatment, it frees 1 slot and becomes Severe. After another Full Rest with successful treatment, it becomes Light. After another, it disappears.

---

## Creature Parts and Enemies

Enemies do not need to use the same anatomical zones as a player character. An important creature uses the zones its anatomy and encounter design require.

By default, an important creature should be organized into five major locations for table readability. Those locations might be skull, jaw, torso, legs, and tail; core, dorsal plates, limbs, wings, and tail; or any equivalent distribution.

Each creature part can have:

| Field | Use |
| --- | --- |
| Defense Roll | Defense or difficulty to strike that part. |
| HP | Normal damage reserve for the part. |
| Block | Impact reduction while the part remains functional. |
| Potency | Offensive or structural capacity if that part attacks or breaks. |
| Durability | Resistance of the part against breaking. |
| Linked abilities | Attacks, Techniques, traits, or phases that depend on the part. |

Breaking a creature part limits enemy options. If an ice wolf has Frost Breath linked to its jaw, breaking the jaw prevents that ability until the enemy stat block says otherwise.

Resource extraction rules are resolved in their own section. Here, only three questions matter: whether the part remains functional, whether it provides Block, and which enemy options remain available.
