---
title: "ATB: Flujo Temporal de Combate"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [atb, combat, timeline, rhythm, initiative, opening]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-atb-combat-timeline.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-acciones.md
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

# ATB: Flujo Temporal de Combate

El combate no se divide en rondas fijas. Cada criatura actúa según su posición en el flujo temporal, su Preparación y el costo de ritmo de sus acciones.

El **ATB** — Flujo Temporal de Combate — representa cuándo una criatura está lista para actuar y cuánto tarda en volver a estarlo.

El ATB responde dos preguntas:

> ¿Quién actúa ahora?  
> ¿Cuánto tarda en volver a actuar?

---

## El Flujo Temporal

El ATB se representa como un **track circular**.

Cada participante ocupa una posición en ese track. En el centro del track hay un **marcador de flujo** que indica el momento presente del combate. La ficha más próxima al marcador es la siguiente en actuar.

Cuando una criatura actúa, su ficha avanza en el track según el costo de ritmo de la acción elegida. El marcador se desplaza hasta la siguiente ficha activa. El flujo continúa sin reiniciar.

El track circular resuelve el problema práctico de la línea infinita: las fichas no se reposicionan. Simplemente avanzan alrededor del track, y el marcador sigue a la ficha más próxima.

El track permite ver:

- quién actúa primero
- quién vuelve a actuar antes
- quién se sobrecompromete
- quién gana tempo mediante acciones más ligeras

El orden de combate no queda fijo al inicio. Cambia con cada activación.

---

## Apertura del combate

Cuando comienza una escena hostil, cada participante recibe una posición inicial en el ATB.

Para hacerlo, cada participante calcula su **Valor de Apertura**.

```text
Valor de Apertura = Preparación + modificadores de situación
```

El Valor de Apertura más alto entre todos los participantes establece el **Punto de Referencia** del encuentro.

```text
Punto de Referencia = Valor de Apertura más alto del encuentro
```

La posición inicial de cada participante se calcula con esta fórmula:

```text
Posición inicial = Punto de Referencia − Valor de Apertura del participante
```

El participante con el Valor de Apertura más alto queda en posición `0`, el punto más próximo al marcador de flujo. Ese participante actúa primero.

Los demás quedan más lejos del marcador, a una distancia igual a la diferencia entre el Punto de Referencia y su propio Valor de Apertura.

La apertura no es un sistema separado del ATB. Solo define el estado inicial del track. Desde la primera activación, los costos de ritmo se aplican normalmente.

---

## Modificadores de situación

Los modificadores de situación representan ventajas o desventajas al inicio del combate.

Pueden incluir:

- estar alerta
- emboscar
- estar sorprendido
- tener el arma preparada
- estar distraído
- estar herido
- estar mal posicionado
- estar reorganizándose
- iniciar desde una posición ventajosa

El Narrador asigna estos modificadores según la ficción de la escena.

---

## Ejemplo de apertura

Tres criaturas comienzan un encuentro.

| Participante | Preparación | Modificador | Valor de Apertura |
| --- | ---: | ---: | ---: |
| Exploradora | 4 | +1 | 5 |
| Bestia | 3 | 0 | 3 |
| Custodio | 2 | -1 | 1 |

El Valor de Apertura más alto es `5`, por lo que el Punto de Referencia es `5`.

| Participante | Cálculo | Posición inicial |
| --- | --- | ---: |
| Exploradora | 5 − 5 | 0 |
| Bestia | 5 − 3 | 2 |
| Custodio | 5 − 1 | 4 |

La Exploradora actúa primero porque su ficha es la más próxima al marcador. La Bestia queda a distancia `2`. El Custodio queda a distancia `4`.

---

## Activación

Una criatura se activa cuando su ficha es la más próxima al marcador de flujo.

Durante su activación puede realizar una acción disponible según las reglas de Acciones, Técnicas, condiciones activas y estado de la escena.

Después de resolver la acción, su ficha avanza en el track.

```text
Nueva posición = posición actual + costo de ritmo de la acción
```

Una acción rápida desplaza poco la ficha. Una acción pesada la desplaza más.

---

## Resolución del flujo

El flujo del ATB sigue este procedimiento en bucle:

1. El marcador señala la ficha más próxima a él.
2. Esa criatura actúa.
3. Resuelve su acción.
4. Su ficha avanza según el costo de ritmo de la acción elegida.
5. El marcador se desplaza hasta la siguiente ficha más próxima.

El combate continúa repitiendo este procedimiento hasta que la escena termine.

---

## Desempates

Si dos o más fichas quedan a la misma distancia del marcador, actúa primero quien tenga mayor Preparación.

Si también empatan en Preparación, cada participante empatado realiza una Tirada de Característica de Agilidad enfrentada.

El resultado más alto actúa primero.

Si el empate persiste, el Narrador decide según la posición, la ficción de la escena o cualquier ventaja situacional clara.

---

## Costo de ritmo

Cada acción significativa tiene un **costo de ritmo**.

Ese costo indica cuánto avanza la ficha en el track después de actuar.

El costo de ritmo no es lo mismo que el Desgaste.

| Concepto | Qué mide |
| --- | --- |
| Ritmo | Cuánto tarda la criatura en volver a actuar |
| Desgaste | Cuánta presión acumulada deja la acción sobre cuerpo, mente o compostura |

Una acción puede ser rápida pero agotadora. También puede ser lenta sin generar mucho Desgaste.

El ritmo organiza el tiempo. El Desgaste registra el costo interno de sostener la acción.

---

## Bandas de acción

Cada acción tiene un costo de ritmo. Ese número indica cuántas posiciones avanza la ficha al resolverse.

| Banda | Costo de ritmo |
| --- | ---: |
| Acción gratuita | 0 |
| Acción rápida | 3 |
| Acción estándar | 5 |
| Acción pesada | 7 |
| Acción extrema | 9 |
| Variable | Definido por la regla, Técnica o efecto |

Las acciones extremas no están disponibles como acciones base. Aparecen mediante Técnicas, efectos especiales o reglas específicas.

Una acción de costo `0` no desplaza la ficha. Las Acciones Gratuitas siguen sujetas a los límites definidos en el capítulo de Acciones.

Los costos específicos de cada acción base se encuentran en el capítulo de Acciones.

---

## Reacciones y ATB

Las Reacciones existen dentro de la misma economía temporal que cualquier otra acción.

Aunque ocurran fuera de la activación normal de una criatura, pueden tener:

- costo de ritmo
- costo de Desgaste
- efectos sobre la posición futura de la ficha

Si una Reacción tiene costo de ritmo, la ficha de la criatura avanza desde su posición actual.

```text
Nueva posición = posición actual + costo de ritmo de la Reacción
```

La ventaja de una Reacción no es que sea gratuita. Su ventaja es que permite intervenir antes de la siguiente activación natural.

Una criatura solo puede usar una Reacción cuando una regla, Técnica, maniobra, rasgo o situación específica lo permita.

La definición completa de Reacciones se encuentra en el capítulo de Acciones.

---

## Ejemplo

Dos personajes comienzan próximos al marcador de flujo.

El primero usa Movimiento para ganar cobertura. Su acción tiene costo de ritmo `5`, así que su ficha avanza 5 posiciones en el track.

El segundo usa un ataque con arma a dos manos. Su acción tiene costo de ritmo `7`, así que su ficha avanza 7 posiciones.

El primer personaje vuelve a estar activo antes porque pagó un costo de ritmo menor. El segundo generó más presión inmediata, pero tardará más en volver a actuar.

El track circular registra esas elecciones directamente, sin convertirlas en rondas fijas.
