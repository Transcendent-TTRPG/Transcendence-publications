---
title: "Especializaciones"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 4
section: especializaciones
status: review
canonical: false
tags: [specializations, progression, synapsis, competencies, character-development]
related:
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/01-specializations.md
  - core-books/transcendence-corebook/16-appendices/es/01-catalogo-de-especializaciones.md
  - core-books/transcendence-corebook/05-character-creation/es/character-creation.md
  - core-books/transcendence-corebook/03-core-rules/es/02-rolling-system-and-competencies.md
authority_refs:
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/docs/system/competencies.md
  - Transcendence-design/docs/system/backgrounds.md
  - Transcendence-design/docs/system/characteristics.md
  - Transcendence-design/docs/adr/system-abilities-and-specializations.md
  - Transcendence-design/docs/adr/system-specialization-rank-restructure.md
  - Transcendence-design/data/system/specializations.yaml
  - Transcendence-design/data/system/specializations-catalog.yaml
  - Transcendence-design/data/system/competencies.yaml
  - Transcendence-design/data/system/backgrounds.yaml
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
---

# Especializaciones

Las especializaciones son dominios entrenables. Representan prácticas que el personaje ha desarrollado: acciones, oficios, saberes o disciplinas que puede intentar, fallar y refinar con el tiempo.

Una característica mide una aptitud base. Una especialización mide lo que el personaje ha practicado con esa aptitud.

En juego, las especializaciones cumplen tres funciones:

- modifican Tiradas de Especialización
- permiten progresar mediante Ventaja en el Aprendizaje
- activan Sinapsis al alcanzar nuevos rangos

---

## Qué representan

Una especialización no es un poder que el personaje posee por sí mismo. Es una práctica.

Dos personajes con la misma característica pueden actuar de formas distintas si han entrenado dominios diferentes. Un personaje con Sabiduría alta y Medicina interpreta heridas, síntomas y tratamientos. Otro con Sabiduría alta y Supervivencia lee rastros, clima, rutas y señales del entorno.

La característica da la base. La especialización define cómo se convierte esa base en acción.

---

## Especializaciones de inicio

Durante la creación de personaje, todo personaje comienza con cuatro especializaciones iniciales:

| Fuente | Cantidad | Nivel inicial | Rango inicial |
| --- | --- | --- | --- |
| Trasfondo | 3 | 1 | Novato |
| Universal de Tenacidad | 1 | 1 | Novato |

La especialización universal de Tenacidad debe ser una de estas tres:

- **Marcha**
- **Aclimatación**
- **Tolerancia**

La misma especialización no puede escogerse dos veces durante la creación de personaje.

Todas las especializaciones que no fueron escogidas comienzan en nivel `0`, rango **No Entrenado**.

Las especializaciones iniciales ya otorgan la Sinapsis correspondiente al rango Novato durante la creación.

---

## Categorías

Las especializaciones se agrupan en cinco categorías. La categoría indica qué tipo de dominio representa la especialización; no determina por sí sola qué característica usa.

| Categoría | Tipo de dominio |
| --- | --- |
| Física | Técnica corporal, movimiento, esfuerzo y control físico practicado |
| Mental | Interpretación, astucia, atención, lectura situacional y razonamiento adaptativo |
| Social | Influencia, expresión, proyección, engaño y control interpersonal |
| Artes y Oficios | Oficios prácticos y disciplinas artísticas concretas, como música, danza, malabarismo, títeres o actuación escénica |
| Conocimiento | Estudio formal, interpretación académica, saber estructurado y comprensión técnica |

Una especialización Física puede estar vinculada a Fuerza, Agilidad o Tenacidad, según lo que abarque. Una especialización Social puede estar vinculada a Astucia, Compostura, Aura o Presencia.

La categoría organiza el dominio. La característica determina qué valor se suma a la tirada.

La lista completa de especializaciones, sus características asociadas y sus usos comunes se encuentra en el **Catálogo de Especializaciones**, ubicado en los apéndices.

---

## Tirada de Especialización

Cuando un personaje actúa mediante una especialización, realiza una **Tirada de Especialización** (**T.E.**).

```text
T.E. = 1d10 + nivel de competencia + rango de competencia + característica asociada + bonificadores adicionales
```

| Componente | Qué representa |
| --- | --- |
| **Nivel de competencia** | Progreso numérico alcanzado en esa especialización |
| **Rango de competencia** | Grado de dominio actual |
| **Característica asociada** | Característica vinculada a la especialización usada |
| **Bonificadores adicionales** | Modificadores situacionales, equipo, Técnicas activas u otros efectos aplicables |

Usa una T.E. cuando la acción depende de una práctica concreta: escalar, nadar, rastrear, curar, convencer, fabricar, desactivar trampas, interpretar símbolos o cualquier otro dominio definido como especialización.

---

## Sin entrenamiento

Cualquier personaje puede intentar una tirada en una especialización que no posee entrenada.

Un personaje **No Entrenado** usa solo el dado y la característica asociada.

```text
T.E. sin entrenamiento = 1d10 + característica asociada
```

El nivel y el rango son `0`.

La falta de entrenamiento no impide intentar la acción. Limita lo que el personaje puede alcanzar. Una prueba avanzada puede existir en la ficción, pero quedar fuera del alcance mecánico de alguien sin práctica.

Desarrollar una especialización no habilita la acción. La vuelve sostenible.

---

## Niveles y rangos

Cada especialización tiene un nivel y un rango.

| Rango | Nombre | Niveles |
| --- | --- | --- |
| 0 | No Entrenado | 0 |
| 1 | Novato | 1–2 |
| 2 | Adepto | 3–4 |
| 3 | Experto | 5–6 |
| 4 | Maestro | 7–8 |
| 5 | Consumado | 9–10 |
| 6 | Trascendente | 11+ |

El nivel mide avance numérico. El rango resume el grado de dominio alcanzado.

Cada nuevo rango puede desbloquear nuevas posibilidades, activar Sinapsis y servir como requisito para Técnicas.

---

## Progresión

Las especializaciones progresan mediante uso bajo presión.

Para que una T.E. pueda generar progreso, deben cumplirse tres condiciones:

- el personaje usa **Ventaja en el Aprendizaje**
- la dificultad de la prueba es adecuada para su rango actual
- el dado de aprendizaje supera la condición de progreso

```text
Dado de aprendizaje > dado usado + rango de competencia
```

Si estas condiciones se cumplen, el personaje marca `1` punto de progreso en esa especialización.

El progreso no aparece solo por elegir aprender. La acción debe exigir algo real y la especialización declarada debe coincidir con lo que el personaje está haciendo.

---

## Progreso necesario por nivel

La cantidad de progreso necesaria depende de la afinidad del personaje.

| Afinidad | Progreso necesario para subir 1 nivel |
| --- | --- |
| Sin afinidad mayor | 10 puntos |
| Con afinidad mayor | 5 puntos |

La afinidad mayor proviene del trasfondo.

Un personaje con trasfondo marcial puede tener afinidad mayor en especializaciones Físicas. Uno con trasfondo artesano puede tenerla en Artes y Oficios.

La afinidad mayor no bloquea otras especializaciones. Solo reduce el costo de progresar en las que pertenecen a esa categoría.

---

## Pruebas adecuadas para progresar

No toda acción enseña. Para que una especialización pueda progresar, la dificultad debe ser coherente con el rango actual del personaje.

| Rango actual | Puede progresar con pruebas de... |
| --- | --- |
| Novato | Cualquier nivel |
| Adepto | Fundamentos o superior |
| Experto | Desafiante o superior |
| Maestro | Rigurosa o superior |
| Consumado | Exigente o superior |
| Trascendente | Extrema |

Una prueba demasiado simple no genera progreso para alguien que ya domina ese tipo de acción.

---

## Validación del Narrador

El Narrador valida si la especialización declarada corresponde a la acción real.

El jugador debe explicar cómo usa esa especialización en la escena. Si la justificación no coincide con el dominio declarado, la tirada puede resolverse con otra especialización, con una Tirada de Característica o sin posibilidad de progreso.

Un personaje no puede usar Trampas para analizar el comportamiento de una criatura solo porque quiere progresar Trampas. Debe haber una relación concreta entre la acción y el dominio usado.

El dominio practicado debe reflejar la acción real.

---

## Sinapsis

La Sinapsis representa el modo en que la práctica modifica al personaje.

Cada especialización está asociada a una característica. Cuando la especialización alcanza un nuevo rango, el personaje gana `+1` permanente a esa característica.

| Rango | Nombre | Sinapsis al entrar |
| --- | --- | --- |
| 0 | No Entrenado | — |
| 1 | Novato | +1 a característica |
| 2 | Adepto | +1 a característica |
| 3 | Experto | +1 a característica |
| 4 | Maestro | +1 a característica |
| 5 | Consumado | +1 a característica |
| 6 | Trascendente | +1 a característica |

La Sinapsis se aplica al entrar en un nuevo rango, no cada vez que se gana un nivel.

Durante la creación de personaje, las especializaciones iniciales comienzan en rango Novato. Por eso cada una otorga de inmediato `+1` a su característica asociada.

---

## Crecimiento amplio o profundo

El jugador puede desarrollar muchas especializaciones o concentrarse en pocas.

Desarrollar muchas especializaciones permite activar Sinapsis en varias características y ampliar las opciones del personaje.

Profundizar en una especialización aumenta sus bonificadores de T.E. y puede dar acceso a Técnicas más avanzadas.

Ninguna ruta es superior por defecto. Cada una prioriza una forma distinta de crecimiento.

---

## Uso directo y Técnicas

Usar una especialización produce un resultado narrativo dentro de la escena.

El personaje puede observar, interpretar, construir, reparar, convencer, recordar, desplazarse o actuar según el dominio usado. Ese uso puede abrir información, rutas, ventajas narrativas o nuevas posibilidades de acción.

Por sí solo, el uso directo de una especialización no cambia automáticamente el estado mecánico de la escena, salvo que una regla, consecuencia o decisión del Narrador lo indique.

Una **Técnica** es diferente. Es una aplicación específica que el personaje desbloquea al alcanzar cierto nivel de competencia en una o más especializaciones.

A diferencia del uso directo, una Técnica produce una consecuencia mecánica definida cuando se activa.

Esta distinción es estructural:

| Uso | Resultado |
| --- | --- |
| Especialización directa | Abre posibilidades narrativas o prácticas |
| Técnica | Produce una consecuencia mecánica definida |

---

## Resumen rápido

| Elemento | Regla |
| --- | --- |
| Especialización inicial | Nivel 1 / rango Novato |
| No Entrenado | Nivel 0 / rango 0 |
| T.E. entrenada | `1d10 + nivel + rango + característica + bonificadores` |
| T.E. sin entrenamiento | `1d10 + característica` |
| Progreso con afinidad mayor | 5 puntos por nivel |
| Progreso sin afinidad mayor | 10 puntos por nivel |
| Sinapsis | +1 a característica al entrar en cada nuevo rango |
| Técnica | Requiere dominio específico y produce consecuencia mecánica definida |

---

## Ejemplo

Un personaje usa Supervivencia para leer huellas rotas al borde de un camino inundado.

La tirada puede revelar por dónde pasó un grupo, qué ruta sigue siendo viable y qué señales del terreno conviene evitar. Ese resultado abre información y opciones.

Por sí mismo, ese uso no daña a un enemigo, no cambia la iniciativa ni impone una condición mecánica.

Si más adelante el personaje desbloquea una Técnica vinculada al rastreo o a la lectura de campo, esa Técnica sí puede añadir una consecuencia mecánica definida a ese mismo tipo de acción entrenada.
