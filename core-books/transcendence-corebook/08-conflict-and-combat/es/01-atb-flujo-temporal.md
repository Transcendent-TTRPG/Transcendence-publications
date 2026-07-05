---
title: "ATB: Flujo Temporal de Combate"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [atb, combat, flow, rhythm, initiative, opening]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/01-atb-combat-flow.md
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

El combate en Transcendence no es un intercambio ordenado de turnos fijos. Es un caos hiperactivo de adrenalina, pánico y reflejos de supervivencia. El **ATB (Línea de Tiempo Activa)** no divide el tiempo en rondas estáticas; representa el avance inexorable de una masacre y los preciosos segundos que tardan tus músculos en volver a reaccionar tras un esfuerzo táctico.

El ATB responde dos preguntas:

> ¿Quién actúa ahora?  
> ¿Cuánto tardará tu cuerpo en volver a responder?

---

## El Flujo Temporal

El ATB se representa físicamente en la mesa como un **track circular continuo**.

Cada participante ocupa una posición numerada. En el track hay un **marcador de flujo** que registra el presente absoluto del combate.

Cuando una criatura se activa, el marcador se empareja con su ficha. La criatura declara su acción y mueve su ficha hacia adelante (alejándose del marcador) pagando el *costo de ritmo*. Este desplazamiento físico de la ficha representa el tiempo de recuperación táctica que necesita antes de volver a ser una amenaza. Una vez resuelta la acción, el marcador avanza inexorablemente en el sentido de las manecillas del reloj hasta la siguiente ficha más próxima; esa criatura se activa y el ciclo continúa.

El track permite ver:

- quién actúa primero
- quién vuelve a actuar antes
- quién se sobrecompromete
- quién gana tempo mediante acciones más ligeras

El orden de combate no queda fijo al inicio. Cambia con cada activación.

---

## Apertura del combate

Cuando la violencia estalla, no todos reaccionan igual. El Valor de Apertura determina quién tiene los nervios más templados frente al horror para asegurar el primer impacto.

Para establecer el orden inicial, cada participante calcula su **Valor de Apertura**.

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

## Resolución del flujo

El flujo del ATB sigue este procedimiento en bucle:

1. El marcador se coloca en la posición de la ficha activa.
2. La criatura activa declara su acción. Puede usar cualquier acción disponible según las reglas de Acciones, Técnicas, condiciones activas y estado de la escena.
3. La ficha de la criatura activa avanza según el costo de ritmo de la acción declarada.
4. La acción se resuelve.
5. El marcador avanza en el sentido de las manecillas del reloj hasta la siguiente ficha más próxima.
6. Esa criatura se activa y el proceso se repite.

```text
Nueva posición = posición actual + costo de ritmo de la acción
```

El combate continúa repitiendo este procedimiento hasta que la escena termine.

---

## Desempates

Si dos o más fichas quedan a la misma distancia del marcador, actúa primero quien tenga mayor Preparación.

Si también empatan en Preparación, el resultado depende de quiénes están empatados:

- **PNJ y PJ empatados:** el Narrador decide quién actúa primero.
- **PJ entre sí:** los jugadores deciden el orden por sí mismos.

---

## Costo de ritmo

Cada acción significativa tiene un **costo de ritmo**.

Ese costo indica cuánto avanza la ficha en el track después de actuar.

El costo de ritmo no es lo mismo que el Desgaste.

| Concepto | Qué mide |
| --- | --- |
| Ritmo | Cuánto tarda la criatura en volver a actuar |
| Desgaste | Cuánta presión acumulada deja la acción sobre cuerpo, mente o compostura |

Una técnica marcial puede resolverse en un parpadeo (bajo costo de Ritmo), pero desgarrar tus tendones en el proceso (alto costo de Desgaste). Por el contrario, recargar y preparar un arma pesada puede tomar tiempo (alto Ritmo), pero no exigirte físicamente.

El Ritmo organiza el tiempo continuo del combate. El Desgaste registra el sufrimiento fisiológico del cuerpo para sostener ese ritmo.

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

## Ciclos autónomos

Algunas criaturas y efectos del entorno generan **ciclos autónomos**: fichas adicionales que entran al ATB con su propio costo de Ritmo e independientes del turno principal de la criatura.

Un ciclo autónomo no es una acción del Narrador durante el turno de la criatura. Es una ficha propia en el track, visible para todos en la mesa, que se activa cuando el marcador de flujo la alcanza.

Su siguiente costo de Ritmo no se declara por defecto. Es información oculta hasta que el ciclo se dispara o hasta que una Técnica lo revela.

Los ciclos autónomos pueden representar:

- procesos biológicos de la criatura (carga elemental, regeneración, postura defensiva recurrente)
- capacidades de coordinación de campeones que modifican el comportamiento de criaturas cercanas
- efectos ambientales generados por criaturas élite que modifican el campo de batalla

Cuando la zona que impulsa un ciclo autónomo biológico colapsa, el ciclo se retira del ATB. Los efectos ya activos pueden persistir según el diseño de la criatura.

---

## Reacciones y ATB

Las Reacciones también tienen costo de ritmo. Cuando una criatura ejecuta una Reacción, su ficha avanza desde su posición actual según el costo de ritmo de esa Reacción.

La definición completa de Reacciones se encuentra en el capítulo de Acciones.

---

## Ejemplo

Dos personajes comienzan próximos al marcador de flujo.

El primero usa Movimiento para ganar cobertura. Su acción tiene costo de ritmo `5`, así que su ficha avanza 5 posiciones en el track.

El segundo usa un ataque con arma a dos manos. Su acción tiene costo de ritmo `7`, así que su ficha avanza 7 posiciones.

El primer personaje vuelve a estar activo antes porque pagó un costo de ritmo menor. El segundo generó más presión inmediata, pero tardará más en volver a actuar.

El track circular registra esas elecciones directamente, sin convertirlas en rondas fijas.
