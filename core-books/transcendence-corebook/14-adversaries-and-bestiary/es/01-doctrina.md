---
title: "Doctrina, Naturaleza, Categoría y Rol"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 14
status: draft
canonical: false
tags: [criaturas, adversarios, naturaleza, categoría, rol, doctrina, mortal, anomalía, primordial]
related:
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/02-zonas.md
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/03-rasgos.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/
authority_refs:
  - Transcendence-design/docs/system/creatures.md
---

# Doctrina, Naturaleza, Categoría y Rol

Cada criatura es un sistema con comportamientos, y cada comportamiento tiene un cuerpo que lo hace posible.

---

## El cuerpo explica el comportamiento

Una criatura que respira hielo tiene un órgano que produce ese frío. Una que regenera tejido tiene una glándula que lo impulsa. Una que barre con la cola tiene una cola que existe porque ese barrido existe.

El punto de partida siempre son los comportamientos: qué hace la criatura, cómo ataca, cómo responde, cómo presiona el campo de batalla. Las zonas — las partes del cuerpo que el sistema registra — son consecuencia de esos comportamientos, no su origen.

**Si un comportamiento no tiene zona, no es un comportamiento: es una abstracción. Las abstracciones no pertenecen al diseño de criaturas.**

Cuando una zona colapsa, el comportamiento vinculado a ella se detiene. Los jugadores que apuntan a zonas desmantelan la criatura parte a parte: cuando una zona colapsa, el comportamiento que sostenía desaparece. La pregunta táctica es cuál desactivar primero, y qué hace la criatura cuando lo pierde.

---

## Naturaleza

La naturaleza describe la composición biológica de la criatura y su relación con el Tauma. El peligro viene del NR — una Mortal puede ser tan letal como una Anomalía; la naturaleza describe qué es la criatura, no cuánto daña.

### Mortal

Puramente biológica. Sin Tauma en su composición ni en sus procesos internos. La resistencia a daño elemental es natural — pieles, conchas, densidad, masa — y se expresa a través de los valores de Bloqueo en las zonas relevantes.

### Anomalía

Base biológica con Tauma presente en sus procesos internos. El Tauma es parte de su metabolismo, no una habilidad que activa o controla.

- **Afinidad elemental:** 50% de reducción de daño del elemento afiliado.
- **Vulnerabilidad elemental:** +50% de daño del elemento opuesto.

### Primordial

Entidades compuestas enteramente de Tauma. Sin estructura biológica convencional.

- **Afinidad elemental:** 100% de reducción de daño del elemento afiliado.
- **Vulnerabilidad elemental:** +100% de daño del elemento opuesto.

Para los Primordiales, los ataques que alcanzan zonas sin relación con su lógica estructural causan 0 de daño. El daño significativo requiere que los jugadores comprendan la composición de la criatura lo suficiente como para identificar qué atacar.

---

## Categoría

La categoría define el tipo de presencia que tiene la criatura en el mundo y en un encuentro: su rol en el ecosistema y el alcance de sus ciclos autónomos. El poder lo determina el NR.

### Común

Representa la población general de una especie. Sin rol organizativo especial. Sus ciclos autónomos son estrictamente biológicos: expresan la propia fisiología de la criatura — cómo carga una habilidad elemental, cómo recupera su cuerpo, cómo cambia de postura entre ataques.

### Campeón

Un individuo poderoso que comanda o coordina a un grupo. Sus ciclos autónomos incluyen ciclos biológicos y ciclos de coordinación de aliados — habilidades que funcionan porque otras criaturas están presentes y que modifican el comportamiento de esas aliadas (Preparación, acceso a tácticas, Bloqueo, posicionamiento).

### Elite

Un individuo excepcional, más allá de cualquier otro miembro de su especie. Sus ciclos autónomos incluyen ciclos biológicos y ciclos ambientales — procesos que cambian el propio campo de batalla: visibilidad, terreno, condiciones elementales, estabilidad espacial.

Una criatura Elite no es un Común o un Campeón con más potencia — es un encuentro que modifica el espacio mismo donde están los jugadores.

Las criaturas Elite tienen además:

**Metamorfosis** — Fases que se activan cuando colapsan zonas específicas. Cada fase modifica los comportamientos disponibles, los ciclos activos y las condiciones ambientales. Las fases no están telegrafidas a los jugadores; los aprenden a través del encuentro.

**Apoteosis** — Fase final que se activa después de completar todas las fases de Metamorfosis. Concede a la criatura +3 a todas las tiradas de ataque. Reduce en 1 el rango de amenaza crítica para los jugadores que la atacan.

**Golpe Final** — La acción coordinada específica que pone fin a la criatura durante la Apoteosis. Se define por criatura. Requiere daño umbral entregado a través de un ataque coordinado declarado. Hasta que se ejecute el Golpe Final, la criatura en Apoteosis no puede reducirse por debajo de 1 PV en ninguna zona.

---

## Rol

El rol define la función de combate de la criatura y modifica sus PV en todas las zonas.

| Rol | Multiplicador de PV | Función |
| --- | --- | --- |
| Protector | × 3 | Absorbe ataques; protege a Comunes; prioriza Bloqueo |
| Golpeador | × 2 | Fuente de daño principal; ataques que apuntan a zonas |
| Soporte | × 1,5 | Coordina aliados; aplica condiciones; habilita a otros |
| Lanzador | × 1 | Ataques a distancia o elementales; zonas con menos PV |
