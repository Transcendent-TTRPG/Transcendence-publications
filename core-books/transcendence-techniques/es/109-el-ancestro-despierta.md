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

Al activar esta técnica, tu mente analítica retrocede y cede el control. Entras en el estado **Furia Instintiva** y pasas a llevar un **Contador de Furia** que inicia en 0.

Mientras este estado se mantenga activo, tu comportamiento se altera y cada vez que realices una prueba de habilidad (`T.E.`) se aplica lo siguiente:

- **Tirada Instintiva** (Saltar, Trepar, Acrobacias, Supervivencia, Intuición, Rastreo): El contador **aumenta en 1** antes de resolverse. Sumas el nuevo valor del contador como modificador positivo a esa tirada.
- **Tirada Cognitiva** (Identificación, Interpretación, Percepción, Saberes): El contador **disminuye en 1** antes de resolverse. Aplicas el valor del contador invertido a esta tirada (por ejemplo, si tu contador está en +3 de Furia, recibes un -3 a tu tirada cognitiva; si lograste llevar el contador a -1 de Furia, recibes un +1).

El contador puede subir hasta un máximo igual a tu **Tenacidad**, y puede bajar hasta ese mismo valor en negativo. Una vez alcances cualquiera de los dos extremos, las tiradas que seguirían empujándolo más allá simplemente no lo modifican.

Este estado es permanente. Terminará de forma natural y pacífica cuando dejes de percibir amenazas tangibles, o puedes forzar un fin prematuro realizando una `T.C.` (Enfoque) contra una dificultad fijada por el Narrador basada en la tensión del entorno. Con éxito, recuperas la lucidez, el estado termina y el contador se reinicia.