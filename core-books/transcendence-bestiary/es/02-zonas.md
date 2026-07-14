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

Cada criatura es una anatomía. No una barra de vida — una estructura física con partes que hacen cosas concretas y un interior que las mantiene vivas. Cuando los jugadores atacan, atacan partes específicas del cuerpo. El sistema necesita una respuesta para cada parte que puedan ver y alcanzar.

---

## Dos capas anatómicas

Una criatura tiene siempre dos capas:

**Zonas** — todo lo exterior y atacable. Cada zona es una parte del cuerpo con PV y Bloqueo. Algunas sostienen comportamientos tácticos; otras son puramente estructurales. Cuando una zona colapsa, pierde su función y, según la anatomía, puede abrir paso al interior.

**Núcleo** — el interior vital. Las vísceras, el corazón, el sistema nervioso central, los pulmones — lo que sea que mantenga viva a la criatura. El Núcleo tiene PV pero no tiene Bloqueo: una vez alcanzado, el daño entra sin filtro. No es una zona con posición atacable directamente desde fuera — está siempre detrás de las zonas que lo rodean.

La criatura muere cuando el Núcleo llega a 0 PV.

---

## Cobertura anatómica

Las zonas deben cubrir **todo lo que un jugador pueda percibir y atacar**. Eso incluye partes sin comportamiento especial: patas, flancos, cabeza, cola, superficie dorsal. Si un jugador declara que ataca una parte del cuerpo, el sistema necesita tener números para eso.

No toda zona necesita un comportamiento táctico. Una zona puede existir únicamente para describir cuánto aguanta esa parte del cuerpo y qué cambia cuando colapsa. Lo que no puede existir es una parte visible sin zona.

---

## Zonas: PV y Bloqueo

Los PV y el Bloqueo de cada zona se derivan del NR de la criatura, su rol y su naturaleza.

### PV base por zona

| Designación | PV base |
| --- | --- |
| Zona | NR × 10 |

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

Cada zona aplica un modificador según el tejido que la compone. Esto crea puntos débiles reales entre zonas de la misma criatura.

| Cobertura | Modificador de Bloqueo |
| --- | --- |
| Tejido blando, membrana, vísceras expuestas | × 0,5 |
| Piel, plumas, pelaje | × 1 |
| Escamas, cuero grueso | × 1,5 |
| Caparazón, placas óseas, exoesqueleto | × 2 |

### Daño a zonas

El daño a una zona es `Impacto − Bloqueo de esa zona`. Se aplica directamente a los PV de la zona. El Narrador registra un número por zona.

---

## Núcleo: PV sin Bloqueo

El Núcleo representa el interior vital de la criatura — lo que la mantiene funcionando. No tiene Bloqueo: es tejido blando expuesto, sin armadura natural.

### PV del Núcleo

| Designación | PV base |
| --- | --- |
| Núcleo | NR × 15 |

El multiplicador de rol aplica igual que en las zonas.

### Acceso al Núcleo

El Núcleo no puede atacarse directamente desde el exterior bajo condiciones normales. Para alcanzarlo, el ataque debe llegar a través de una zona colapsada que anatómicamente rodee o cubra el interior vital.

Qué zonas permiten acceso al Núcleo al colapsar es una decisión de diseño por criatura, no una regla de sistema. Depende de la anatomía: destruir el torso de un cuadrúpedo expone sus órganos internos; destruir sus patas lo inmoviliza pero no abre acceso a las vísceras.

Cada zona que otorga acceso al Núcleo al colapsar debe declararlo en su entrada: **"Al colapsar: expone el Núcleo."**

### Daño al Núcleo

Cuando un ataque alcanza el Núcleo a través de una zona colapsada, el daño es `Impacto − 0` — sin Bloqueo. El Narrador aplica el Impacto completo directamente a los PV del Núcleo.

---

## Primordiales y daño físico

Las zonas de los Primordiales son inmunes al daño físico. Cualquier ataque físico produce 0 de daño independientemente del Impacto. El multiplicador de naturaleza × 2 aplica únicamente al daño de Tauma. Para herir a un Primordial, los jugadores necesitan Aspectos y deben identificar qué zonas pueden recibir daño de Tauma dada la lógica estructural del ser.

---

## Colapso de zona

Cuando una zona llega a 0 PV:

- La zona queda destruida.
- Su función estructural desaparece: protección, movilidad, arma o cualquier capacidad que dependiera de esa parte del cuerpo.
- El comportamiento táctico vinculado a ella, si tiene uno, deja de estar disponible.
- Cualquier ciclo autónomo anclado a esa zona se retira del ATB.
- Si la zona declara que expone el Núcleo: los ataques posteriores dirigidos a esa área alcanzan el Núcleo sin Bloqueo.

El colapso de una zona no derrota a la criatura — la cambia. Le quita capacidades. Puede exponerla. Pero sigue viva hasta que el Núcleo llegue a 0.

---

## Ejemplo

Un cuadrúpedo Golpeador Mortal con NR 4:

**Patas** — Piel · PV = (4 × 10) × 2 = **80** · Bloqueo = (4 × 2) × 1 × 1 = **8**
Al colapsar: movimiento reducido a la mitad; no puede usar técnicas de carga. No expone el Núcleo.

**Hocico** — Tejido blando · PV = **80** · Bloqueo = (4 × 2) × 1 × 0,5 = **4**
Al colapsar: pierde la mordida como arma; no puede excavar. No expone el Núcleo.

**Torso** — Escamas · PV = **80** · Bloqueo = (4 × 2) × 1 × 1,5 = **12**
Al colapsar: pierde la protección dorsal. **Expone el Núcleo.**

**Núcleo** (vísceras) · PV = (4 × 15) × 2 = **120** · Bloqueo = 0
Solo accesible a través del Torso colapsado. Al llegar a 0: la criatura muere.

---

## Derrota

Una criatura muere cuando el Núcleo llega a 0 PV.

Para criaturas Elite, el colapso del Núcleo puede activar una fase de Metamorfosis en lugar de muerte inmediata. La Apoteosis y el Golpe Final definen cómo termina el encuentro.
