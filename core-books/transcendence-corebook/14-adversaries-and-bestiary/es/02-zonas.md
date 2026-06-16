---
title: "Sistema de Zonas"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 14
status: draft
canonical: false
tags: [criaturas, zonas, núcleo, bloqueo, colapso, daño, pv, rol, naturaleza]
related:
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/01-doctrina.md
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/03-rasgos.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/
authority_refs:
  - Transcendence-design/docs/system/creatures.md
---

# Sistema de Zonas

Cada zona de una criatura tiene un comportamiento vinculado a ella y es estructural — sostiene parte del funcionamiento de la criatura. No existen zonas sin comportamiento. Si un comportamiento no tiene zona, no pertenece a la criatura.

---

## Tipos de zona

Hay dos designaciones posibles para una zona:

**Zona** — cualquier parte del cuerpo registrada por el sistema. Tiene un comportamiento específico vinculado. Al colapsar, ese comportamiento deja de estar disponible y cualquier ciclo autónomo anclado a ella se retira del ATB.

**Núcleo** — una zona (puede ser más de una en criaturas complejas) cuyo colapso es existencialmente significativo: termina a la criatura o activa una fase mayor. El Núcleo también tiene comportamiento — no es simplemente "el corazón" ni una abstracción de vida total. Es la zona que, al desaparecer, rompe el sistema completo.

La importancia táctica del Núcleo viene de lo que ocurre cuando colapsa. Una criatura cuyo Núcleo sea obvio desde el primer round es tácticamente trivial. Una cuyo Núcleo sea difícil de identificar o de alcanzar es un problema real.

---

## PV y Bloqueo

Los PV y el Bloqueo de cada zona se derivan del NR de la criatura, su rol y su naturaleza. La categoría (Común, Campeón, Elite) determina el alcance de los ciclos autónomos — la dureza de las zonas la da el NR.

### PV base

| Designación | PV base |
| --- | --- |
| Zona | NR × 10 |
| Núcleo | NR × 15 |

### Multiplicador de rol (sobre PV)

| Rol | Multiplicador |
| --- | --- |
| Protector | × 3 |
| Golpeador | × 2 |
| Soporte | × 1,5 |
| Lanzador | × 1 |

### Bloqueo base y multiplicador de naturaleza

El Bloqueo base de todas las zonas es `NR × 2`. La naturaleza lo escala:

| Naturaleza | Multiplicador de Bloqueo |
| --- | --- |
| Mortal | × 1 |
| Anomalía | × 1,5 |
| Primordial | × 2 |

### Modificador de Bloqueo por cobertura de zona

El Bloqueo base es un punto de partida a nivel criatura. Cada zona aplica un modificador según su cobertura biológica. Una criatura puede tener zonas con valores de Bloqueo muy distintos entre sí — eso es exactamente lo que crea puntos débiles reales y hace que la elección de zona importe.

| Cobertura | Modificador de Bloqueo |
| --- | --- |
| Tejido blando, membrana, vísceras | × 0,5 |
| Piel, plumas, pelaje | × 1 |
| Escamas, cuero grueso | × 1,5 |
| Caparazón, placas óseas, exoesqueleto | × 2 |

### Primordiales y daño físico

Las zonas de los Primordiales son **inmunes al daño físico**. Cualquier ataque físico produce 0 de daño independientemente del Impacto. El multiplicador de naturaleza × 2 aplica únicamente al daño de Tauma (Aspectos). Para herir a un Primordial, los jugadores necesitan Aspectos y deben identificar qué zonas pueden recibir daño de Tauma dada la lógica estructural del ser.

### Ejemplo

Un Golpeador Mortal con NR 5 — zona de escamas:
- **Zona:** PV = (5 × 10) × 2 = **100** · Bloqueo = (5 × 2) × 1 × 1,5 = **15**
- **Núcleo:** PV = (5 × 15) × 2 = **150** · Bloqueo = **15**

Una Lanzadora Anomalía con NR 5 — zona de piel expuesta:
- **Zona:** PV = (5 × 10) × 1 = **50** · Bloqueo = (5 × 2) × 1,5 × 1 = **15**
- **Núcleo:** PV = (5 × 15) × 1 = **75** · Bloqueo = **15**

---

## Daño a zonas

El daño a una zona es Impacto − Bloqueo de esa zona (mínimo 0). Se aplica directamente a los PV de la zona. El Narrador registra un número por zona. Sin seguimiento de heridas, sin ranuras.

---

## Colapso de zona

Cuando una zona llega a 0 PV:

- La zona queda destruida.
- El comportamiento vinculado a ella deja de estar disponible.
- Cualquier ciclo autónomo anclado a esa zona se retira del ATB.
- El comportamiento de la criatura cambia según lo definido en su entrada.
- Si la zona es Núcleo: la criatura es derrotada o se activa una fase de Metamorfosis (solo Elite).

El colapso de zonas que no son Núcleo no derrota a la criatura. La cambia.

---

## Derrota

Una criatura es derrotada cuando su Núcleo colapsa, o — solo para criaturas Elite — cuando el Golpe Final se ejecuta con éxito durante la Apoteosis.
