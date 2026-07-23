---
title: "El Ancestro Despierta"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, innate, species, luphran, active, utility, fury, instinct, counter, permanent]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
  - core-books/transcendence-corebook/06-species/es/12-luphran.md
---

# El Ancestro Despierta

### Activo - Utilidad

**Rango Novato**

*Lo que queda cuando el pensamiento se retira no es vacío. Es el lobo.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Personal | Tú | Permanente | — |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | `2` | `1` |

## Requisitos

- Especie: Luphran.

## Keywords

- `Luphran`
- `Furia Instintiva`

## Efecto

Al activar esta técnica, entras en el estado **Furia Instintiva** y mantienes un **contador de Furia** que comienza en 0.

Mientras el estado esté activo, cada vez que realices una T.E.:

- **Instintiva** (Saltar, Trepar, Acrobacias, Supervivencia, Intuición, Rastreo): el contador aumenta en 1 antes de resolverse. Esa tirada recibe un modificador igual al nuevo valor del contador.
- **Cognitiva** (Identificación, Interpretación, Percepción, Saberes): el contador disminuye en 1 antes de resolverse. Esa tirada recibe un modificador igual al valor del contador negado (si el contador es +3, recibes −3 en esa tirada; si el contador es −1, recibes +1).

El contador sube hasta un máximo igual a tu Tenacidad y puede bajar hasta ese mismo valor en negativo. Una vez en cualquiera de los dos extremos, las tiradas del tipo que lo llevaría más allá ya no lo modifican.

El estado es permanente. Termina de forma natural cuando dejas de percibir amenazas, o prematuramente cuando realizas una T.C. de Enfoque contra una dificultad que el Narrador fija según las condiciones del entorno. Si tienes éxito, el estado termina y el contador se reinicia.