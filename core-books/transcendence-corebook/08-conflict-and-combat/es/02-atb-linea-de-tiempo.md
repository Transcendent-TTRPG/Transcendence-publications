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
  - core-books/transcendence-corebook/08-conflict-and-combat/en/02-atb-combat-timeline.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-acciones.md
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

El combate no se divide en rondas fijas. Cada criatura actúa según su posición en la línea de tiempo, su Preparación y el costo de ritmo de sus acciones.

La línea de tiempo de combate, o **ATB**, representa cuándo una criatura está lista para actuar y cuánto tarda en volver a estarlo.

Cada participante ocupa una posición en un track. La ficha más a la izquierda actúa primero. Después de actuar, esa ficha avanza hacia la derecha según el costo de ritmo de la acción elegida.

El ATB responde dos preguntas:

> ¿Quién actúa ahora?  
> ¿Cuánto tarda en volver a actuar?

---

## Qué representa el ATB

La posición de una ficha en el track no representa solo iniciativa. Representa el tiempo que una criatura necesita para recuperarse, reorganizarse y generar una nueva acción significativa.

Una acción rápida deja a la criatura disponible antes. Una acción pesada la retrasa más.

El track permite ver:

- quién actúa primero
- quién vuelve a actuar antes
- quién se sobrecompromete
- quién retrasa su siguiente oportunidad por una acción pesada
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
Posición inicial = Punto de Referencia - Valor de Apertura del participante
```

El participante con el Valor de Apertura más alto queda en posición `0`, el extremo izquierdo del track. Ese participante actúa primero.

Los demás quedan a la derecha, a una distancia igual a la diferencia entre el Punto de Referencia y su propio Valor de Apertura.

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

La apertura no es un sistema separado del ATB. Solo define el estado inicial del track. Desde la primera activación, los costos de ritmo se aplican normalmente.

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
| Exploradora | 5 - 5 | 0 |
| Bestia | 5 - 3 | 2 |
| Custodio | 5 - 1 | 4 |

La Exploradora actúa primero porque está en posición `0`. La Bestia queda en posición `2`. El Custodio queda en posición `4`.

---

## Flujo del ATB

Una vez resuelta la apertura, el combate sigue el flujo normal del ATB.

Para resolver el orden:

1. Actúa la ficha más a la izquierda.
2. La criatura resuelve su acción.
3. La ficha avanza hacia la derecha según el costo de ritmo de la acción.
4. Se revisa de nuevo cuál ficha queda más a la izquierda.
5. Esa ficha actúa a continuación.

El combate continúa repitiendo este procedimiento hasta que la escena termine.

---

## Activación

Una criatura se activa cuando su ficha es la más a la izquierda del track.

Durante su activación, puede realizar una acción disponible según las reglas de Acciones, Técnicas, condiciones activas y estado de la escena.

Después de resolver la acción, su ficha avanza hacia la derecha.

```text
Nueva posición = posición actual + costo de ritmo de la acción
```

Una acción rápida desplaza poco la ficha. Una acción pesada la desplaza más.

---

## Desempates

Si dos o más fichas ocupan la misma posición más a la izquierda, actúa primero quien tenga mayor Preparación.

Si también empatan en Preparación, cada participante empatado realiza una Tirada de Característica de Agilidad enfrentada.

El resultado más alto actúa primero.

Si el empate persiste, el Narrador decide según la posición, la ficción de la escena o cualquier ventaja situacional clara.

---

## Costo de ritmo

Cada acción significativa tiene un **costo de ritmo**.

Ese costo indica cuánto se retrasa la próxima oportunidad de actuar.

El costo de ritmo no es lo mismo que el Desgaste.

| Concepto | Qué mide |
| --- | --- |
| Ritmo | Cuánto tarda la criatura en volver a actuar |
| Desgaste | Cuánta presión acumulada deja la acción sobre cuerpo, mente o compostura |

Una acción puede ser rápida pero agotadora. También puede ser lenta sin generar mucho Desgaste.

El ritmo organiza el tiempo. El Desgaste registra el costo interno de sostener la acción.

---

## Bandas de acción

Cada acción tiene un costo de ritmo. Ese número indica cuántas posiciones avanza la ficha hacia la derecha al resolverse.

| Banda | Costo de ritmo |
| --- | ---: |
| Acción gratuita | 0 |
| Acción rápida | 3 |
| Acción estándar | 5 |
| Acción pesada | 7 |
| Acción extrema | 9 |
| Variable | Definido por la regla, Técnica o efecto |

Las acciones extremas no están disponibles como acciones base. Aparecen mediante Técnicas, efectos especiales o reglas específicas.

Una acción de costo `0` no desplaza la ficha. Esto no significa que pueda usarse sin límite. Las Acciones Gratuitas siguen sujetas a los límites definidos en el capítulo de Acciones.

---

## Acciones base y ritmo

Estos costos aplican cuando ninguna Técnica, regla específica, condición o bonificador los modifica.

| Acción | Costo de ritmo | Desgaste base |
| --- | ---: | ---: |
| Acción gratuita: soltar, hablar brevemente | 0 | 0 |
| Interactuar | 3 | 0 o 1 |
| Moverse | 5 | 1 |
| Ocultarse | 5 | 1 |
| Usar Especialización | 5 | 1 |
| Atacar con arma natural | 5 | 1 |
| Atacar con arma a una mano | 5 | 1 |
| Atacar con arma a dos manos | 7 | 1 |
| Atacar con dos armas | 7 | 1 |
| Usar Técnica | Variable | Variable |

El Desgaste de Interactuar solo se aplica cuando la interacción ocurre bajo presión real de la escena. Una interacción trivial o sin riesgo inmediato genera `0` Desgaste.

---

## Acciones de costo 0

Una acción con costo de ritmo `0` no mueve la ficha en el ATB.

Esto aplica a acciones breves como soltar un objeto o decir una frase corta, dentro de los límites definidos en el capítulo de Acciones.

El costo `0` no convierte una acción en ilimitada. Si una acción gratuita cambia la escena de forma importante, sustituye una Acción Activa o se repite para generar ventajas sin costo, el Narrador puede asignarle costo de ritmo, Desgaste o ambos.

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

La ventaja de una Reacción no es que sea gratuita. Su ventaja es que permite intervenir ahora, antes de la siguiente activación normal.

Una criatura solo puede usar una Reacción cuando una regla, Técnica, maniobra, rasgo o situación específica lo permita.

La definición completa de Reacciones se encuentra en el capítulo de Acciones.

---

## Movimiento y ATB

El Movimiento no es una capa separada del combate. Forma parte del ritmo de la escena y tiene su propio costo.

Moverse siempre ocupa la banda Estándar del ATB.

```text
Movimiento = costo de ritmo 5
```

Moverse para salir de un aliento, alcanzar cobertura, cerrar distancia o interceptar una carga cuesta lo mismo en el track. Lo que cambia es lo que ese movimiento logra.

El terreno no modifica el costo de ritmo. El terreno puede modificar:

- la distancia recorrida
- las tiradas requeridas
- las consecuencias del trayecto
- los peligros atravesados

La posición determina lo que es posible. Ese es el valor táctico del Movimiento dentro del ATB.

---

## Ocultarse y ATB

Ocultarse usa ritmo estándar porque exige una oportunidad real dentro de la escena.

```text
Ocultarse = costo de ritmo 5
```

Para ocultarse, el personaje debe crear o aprovechar una situación que permita romper la localización precisa de los enemigos.

No puede declararse sin cobertura, visibilidad reducida, distracción, preparación o una regla específica que lo permita.

Las reglas completas de Ocultación, posición aproximada y detección se encuentran en **Cobertura, Visibilidad y Ocultación**.

---

## Técnicas y costos variables

Las Técnicas pueden modificar el flujo normal del ATB.

Una Técnica puede:

- usar un costo de ritmo distinto
- reducir o aumentar Desgaste
- funcionar como Reacción
- crear una excepción al orden normal
- desplazar fichas
- alterar la posición de una criatura en el track

Cuando una Técnica contradice una regla general del ATB, se aplica la regla específica de la Técnica.

---

## Ejemplo

Dos personajes comienzan cerca del mismo punto en la línea de tiempo.

El primero usa Movimiento para ganar cobertura. Su acción tiene costo de ritmo `5`, así que su ficha avanza 5 posiciones.

El segundo usa un ataque con arma a dos manos. Su acción tiene costo de ritmo `7`, así que su ficha avanza 7 posiciones.

El primer personaje vuelve a estar disponible antes porque pagó un costo de ritmo menor. El segundo generó más presión inmediata, pero tardará más en volver a actuar.

La línea de tiempo registra esas elecciones directamente, sin convertirlas en rondas fijas.

