---
title: "ATB: Línea de Tiempo de Combate"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [atb, combat, timeline, rhythm, initiative, actions, rhythm-cost, opening]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/atb-combat-timeline.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/acciones.md
  - core-books/transcendence-corebook/03-core-rules/es/02-rolling-system-and-competencies.md
authority_refs:
  - Transcendence-design/docs/system/atb-reference.md
  - Transcendence-design/docs/system/mechanics-overview.md
  - Transcendence-design/docs/adr/combat-atb-timeline.md
  - Transcendence-design/docs/adr/combat-atb-rhythm-costs.md
  - Transcendence-design/data/system/atb-combat.yaml
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
---

# ATB: Línea de Tiempo de Combate

El combate no se divide en rondas fijas. Cada personaje, criatura o sistema importante del encuentro actúa según su ritmo, su preparación y el costo temporal de sus decisiones.

La línea de tiempo de combate — también llamada ATB — representa esto directamente. Cada participante ocupa una posición en un track. Quien se encuentre más a la izquierda actúa primero.

Cuando una entidad actúa, su ficha se desplaza hacia la derecha según el costo de ritmo de la acción elegida. Actuar antes cuesta más; retrasar una acción preserva el tempo pero cede terreno.

El ATB existe para responder una pregunta simple:

> ¿Quién está listo para actuar ahora, y cuánto tardará en volver a estarlo?

---

## Qué representa el ATB

La posición de una ficha en el track no representa solo "iniciativa". Representa el tiempo que le tomará a una criatura recuperarse, reorganizarse y volver a generar una acción significativa dentro del combate.

Una acción rápida deja a la criatura lista antes. Una acción pesada o exigente la retrasa más.

El track hace esto visible en tiempo real:

- quién reacciona antes
- quién se sobrecompromete
- quién fuerza una acción muy poderosa a costa de perder tempo
- quién consigue actuar dos veces antes que otro porque sus decisiones fueron más ligeras o más eficientes

---

## Apertura del combate

Cuando comienza una escena hostil, cada participante recibe una posición en el track antes de que se resuelva la primera acción.

Cada participante calcula su Valor de Apertura:

Valor de Apertura = Preparación + modificadores de situación

El Valor de Apertura más alto entre todos los participantes establece el Punto de Referencia del encuentro. La posición inicial de cada participante es la diferencia entre ese Punto de Referencia y su propio Valor de Apertura.

Quien tenga el Valor de Apertura más alto queda en la posición 0 — el extremo izquierdo del track — y actúa primero. Los demás quedan a la derecha a una distancia igual a la diferencia entre el Punto de Referencia y su propio Valor de Apertura.

Los modificadores de situación representan circunstancias como:

- estar alerta
- emboscar
- estar sorprendido
- encontrarse mal posicionado
- tener el arma preparada
- estar distraído, herido o reorganizándose

La apertura del combate no es un sistema separado del track. Es el estado inicial desde el que parte. Los costos de ritmo se acumulan sobre esa posición desde la primera activación en adelante.

---

## La línea de tiempo

Una vez resuelta la apertura, el combate entra en el flujo completo del ATB.

Tres principios lo rigen:

- La ficha más a la izquierda actúa primero.
- Después de actuar, esa ficha se mueve a la derecha.
- La distancia que avanza es el costo de ritmo de la acción elegida.

El orden no queda fijo desde el principio. Se ajusta con cada activación.

Un personaje que use acciones rápidas y eficientes puede volver a actuar antes. Otro que se sobreextienda con una maniobra muy pesada tardará más en recuperar su siguiente oportunidad.

---

## Desempates

Si dos o más fichas ocupan la misma posición más a la izquierda, actúa primero quien tenga mayor Preparación.

Si también empatan en Preparación, cada uno realiza una Tirada de Característica de Agilidad enfrentada. El resultado más alto actúa primero.

---

## Costo de ritmo

Cada acción significativa tiene un costo de ritmo. Ese costo indica cuánto retrasa la próxima oportunidad de actuar.

El costo de ritmo no es lo mismo que el Desgaste:

- El ritmo responde a cuánto tiempo tardas en volver a actuar.
- El Desgaste responde a cuánto esfuerzo acumulado deja esa acción sobre tu cuerpo, tu mente y tu compostura.

Una acción más exigente suele comprometer más en ambas dimensiones — pero no siempre en la misma medida.

Una acción puede ser:

- rápida pero exigente
- lenta pero estable
- eficiente para un personaje entrenado
- costosa para quien no ha desarrollado esa habilidad

---

## Bandas de acción

Cada acción tiene un costo de ritmo — el número de posiciones que su ficha avanza a la derecha al resolverse.

| Banda | Costo de ritmo |
| --- | ---: |
| Acción libre | 0 |
| Acción rápida | 3 |
| Acción estándar | 5 |
| Acción pesada | 7 |
| Acción extrema | 9 |

Costo de ritmo 0 significa que la ficha no se mueve. La criatura mantiene su posición y procede la siguiente activación en línea. Las acciones libres están limitadas por alcance: Soltar y Hablar califican dentro de los límites definidos en las reglas de acción.

Las acciones extremas no están disponibles en el nivel base. Aparecen a través de Técnicas.

### Familias de acción base

Estos costos aplican cuando ninguna habilidad, entrenamiento o bonificador por competencia los modifica.

| Acción | Costo de ritmo | Desgaste |
| --- | ---: | ---: |
| Acción libre (soltar, hablar) | 0 | 0 |
| Interactuar | 3 | 1 * |
| Moverse | 5 | 1 |
| Especialización | 5 | 1 |
| Atacar con arma a una mano | 5 | 1 |
| Atacar con arma a dos manos | 7 | 1 |
| Atacar con dos armas a una mano | 7 | 1 |

\* El Desgaste aplica solo bajo presión real de la escena. Las interacciones triviales generan 0.

El terreno no cambia el costo de ritmo. El terreno afecta la distancia recorrida, las tiradas requeridas y las consecuencias del movimiento.

---

## Reacciones

Las Reacciones existen dentro de la misma economía temporal que cualquier otra acción. Aunque ocurran fuera de la activación planificada del personaje, tienen costo de ritmo, costo de Desgaste y desplazan la ficha en el track.

La ventaja de una Reacción no está en que sea gratuita, sino en que permite intervenir en el momento en lugar de esperar la siguiente activación normal.

La definición completa de Reacciones — qué las activa, cuándo se declaran y cómo se usan — se encuentra en el capítulo de Acciones.

---

## Movimiento y ATB

El movimiento no es una capa invisible separada del combate. El desplazamiento forma parte del ritmo de la escena y tiene su propio costo de ritmo.

Ese costo es fijo: el Movimiento siempre ocupa la banda Estándar del ATB. Moverse para salir de un aliento, alcanzar una posición ventajosa o interceptar una carga cuesta lo mismo en el track — lo que varía no es el tiempo de decisión, sino lo que ese movimiento puede lograr.

El terreno no modifica el costo de ritmo. Lo que el terreno cambia es:

- la distancia que el personaje puede recorrer
- si el trayecto requiere una tirada
- las consecuencias o peligros del desplazamiento

La posición determina lo que es posible. Ese es el valor táctico del Movimiento dentro del ATB.

---

## Ejemplo

Dos personajes comienzan el encuentro cerca del mismo punto de la línea de tiempo. Uno elige un reposicionamiento rápido para ganar cobertura; el otro se compromete con una acción más pesada y de mayor impacto. El primero vuelve a actuar antes porque pagó un costo de ritmo menor. El segundo genera más presión inmediata, pero regresa más tarde al track. La línea de tiempo registra esas elecciones de forma directa en lugar de convertirlas en rondas abstractas.
