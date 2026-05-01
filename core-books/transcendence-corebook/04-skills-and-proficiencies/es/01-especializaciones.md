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

Las especializaciones son dominios entrenables. No representan poderes que el personaje posee por sí mismo, sino prácticas que ha desarrollado: acciones que pueden intentarse, fallarse y refinarse con el tiempo.

Una característica mide una aptitud base. Una especialización mide lo que el personaje ha elegido practicar con esa aptitud.

Durante la creación de personaje, las especializaciones ayudan a definir qué sabe hacer el personaje, cómo aborda los problemas y por qué se diferencia de otros con características similares.

---

## Para qué sirven

Transcendence no usa clases para asignar roles cerrados. La diferenciación entre personajes depende de lo que cada uno desarrolla.

Dos personajes con Sabiduría similar pueden actuar de forma distinta si uno ha practicado Medicina y el otro ha practicado Supervivencia. La característica les da una base comparable. La especialización define cómo convierten esa base en acción.

Las especializaciones también habilitan el acceso a Técnicas. Una Técnica no nace de una competencia genérica: requiere un dominio específico que el personaje ya ha trabajado. Sin la especialización de base, la Técnica no existe.

Cada vez que un personaje alcanza un nuevo rango en una especialización, gana `+1` a la característica asociada a ese dominio. A este incremento se le llama **Sinapsis**. Las características no aumentan por asignación libre; aumentan como consecuencia directa del uso practicado.

---

## Especializaciones de inicio

Todo personaje comienza con cuatro especializaciones en nivel 1, rango Novato.

Tres provienen del trasfondo, según sus restricciones de categoría. La cuarta es una elección universal vinculada a **Tenacidad**: **Marcha**, **Aclimatación** o **Tolerancia**.

Todo personaje elige una de estas tres opciones, independientemente de su trasfondo. Esta elección no reemplaza los bonificadores de especie a Tenacidad; ambos se acumulan.

La misma especialización no puede escogerse dos veces durante la creación de personaje. Todas las demás comienzan en nivel 0, rango No Entrenado.

Las especializaciones iniciales ya otorgan la Sinapsis correspondiente al rango Novato durante la creación.

---

## Categorías

Las especializaciones se agrupan en cinco categorías según el tipo de dominio que representan. Estas categorías no son compartimentos cerrados. Una especialización pertenece a una categoría por lo que abarca, no por la característica a la que está vinculada.

| Categoría | Tipo de dominio |
| --- | --- |
| Física | Técnica corporal, movimiento, esfuerzo y control físico practicado |
| Mental | Interpretación, astucia, atención, lectura situacional y razonamiento adaptativo |
| Social | Influencia, expresión, proyección, engaño y control interpersonal |
| Artes y Oficios | Oficios prácticos y disciplinas artísticas concretas, como música, danza, malabarismo, títeres o actuación escénica |
| Conocimiento | Estudio formal, interpretación académica, saber estructurado y comprensión técnica |

Una especialización Física puede estar vinculada a Fuerza, Agilidad o Tenacidad según lo que abarque. Una especialización Social puede estar vinculada a Astucia, Compostura, Aura o Presencia.

La categoría organiza el dominio. La característica determina qué valor se suma a la Tirada de Especialización.

Las disciplinas artísticas pertenecen a **Artes y Oficios**. Su desarrollo y uso práctico se describen en el **Catálogo de Especializaciones**, ubicado en los apéndices.

---

## Tirada de Especialización

Cuando un personaje actúa a partir de una especialización, el resultado se determina mediante una **Tirada de Especialización** (**T.E.**).

```text
T.E. = 1d10 + nivel de competencia + rango de competencia + característica asociada + bonificadores adicionales
```

| Componente | Qué representa |
| --- | --- |
| **Nivel de competencia** | Progreso numérico alcanzado en esa especialización |
| **Rango de competencia** | Grado de dominio actual: Novato, Adepto, Experto, Maestro, Consumado o Trascendente |
| **Característica asociada** | Característica vinculada a la especialización usada |
| **Bonificadores adicionales** | Modificadores situacionales, de equipo, Técnicas activas u otros efectos aplicables |

### Sin entrenamiento

Cualquier personaje puede intentar una tirada en cualquier especialización, incluso si nunca la ha practicado. Un personaje **No Entrenado** usa solo el dado y la característica asociada.

```text
T.E. sin entrenamiento = 1d10 + característica asociada
```

El nivel y el rango son 0. La falta de entrenamiento no impide el intento, pero limita los resultados alcanzables. Pruebas avanzadas siguen siendo posibles en la ficción, pero suelen quedar fuera del alcance mecánico de un personaje sin práctica.

Desarrollar una especialización no habilita la acción. La vuelve sostenible.

---

## Cómo se adquieren

Las especializaciones se desarrollan mediante uso bajo presión. Cada vez que un personaje utiliza **Ventaja en el Aprendizaje** en una T.E., la tirada puede generar progreso hacia el siguiente nivel de competencia.

El progreso no aparece solo por elegir aprender. La acción debe cumplir tres condiciones:

- la tirada usa la especialización declarada
- la dificultad es adecuada para el rango actual del personaje
- el dado de aprendizaje supera la condición de progreso de Ventaja Evolutiva

```text
Dado de aprendizaje > dado usado + rango de competencia
```

Si estas condiciones se cumplen, el personaje marca 1 punto de progreso en esa especialización.

| Afinidad | Progreso necesario por nivel |
| --- | --- |
| Sin afinidad mayor | 10 puntos |
| Con afinidad mayor | 5 puntos |

La afinidad mayor la determina el trasfondo. Un personaje con trasfondo marcial puede tener afinidad mayor en especializaciones Físicas. Uno con trasfondo artesano puede tenerla en Artes y Oficios.

La afinidad mayor no bloquea el acceso a otras especializaciones. Solo reduce el costo de progresar en las que corresponden al trasfondo.

El Narrador valida si la especialización usada se sostiene en la ficción antes de que pueda generar progreso. La intención del personaje debe coincidir con el dominio declarado. Un personaje no puede usar Trampas para analizar el comportamiento de una criatura si no hay una razón concreta que lo justifique.

El dominio practicado debe reflejar la acción real.

No hay límite en cuántas especializaciones puede desarrollar un personaje. El límite es práctico: cada especialización exige tiempo, tiradas y decisiones. Priorizar una ralentiza las demás.

---

## Rangos y Sinapsis

La competencia en una especialización se mide en niveles y rangos. Cada rango agrupa dos niveles y representa un grado de dominio.

| Rango | Nombre | Niveles | Sinapsis al entrar |
| --- | --- | --- | --- |
| 0 | No Entrenado | 0 | — |
| 1 | Novato | 1–2 | +1 a característica |
| 2 | Adepto | 3–4 | +1 a característica |
| 3 | Experto | 5–6 | +1 a característica |
| 4 | Maestro | 7–8 | +1 a característica |
| 5 | Consumado | 9–10 | +1 a característica |
| 6 | Trascendente | 11+ | +1 a característica |

Al alcanzar el nivel umbral de un nuevo rango, el personaje gana automáticamente `+1` a la característica asociada a esa especialización.

Esto es la **Sinapsis**: el incremento de una característica como consecuencia directa de practicar dominios vinculados a ella.

La tensión es estructural. Alcanzar el rango Novato en muchas especializaciones distintas genera Sinapsis en varias características. Profundizar en una sola especialización genera bonificadores de T.E. mayores y acceso a Técnicas más avanzadas.

Ninguna ruta es superior por defecto. Cada una prioriza una forma distinta de crecimiento.

---

## Uso directo y Técnicas

Usar una especialización produce un resultado narrativo dentro de la escena. El personaje observa, interpreta, construye, repara, convence, recuerda, se desplaza o actúa según el dominio usado.

Ese uso puede abrir información, rutas, ventajas narrativas o posibilidades de acción. No cambia el estado mecánico de la escena de forma automática, salvo que una regla, consecuencia o decisión del Narrador lo indique.

Una **Técnica** es diferente. Es una aplicación específica que el personaje desbloquea al alcanzar cierto nivel de competencia en una o más especializaciones.

A diferencia del uso directo, una Técnica produce una consecuencia mecánica definida en el momento de activarse. Su detalle completo aparece en el capítulo correspondiente.

Esta distinción es estructural. El uso directo de una especialización abre posibilidades. La Técnica convierte una de esas posibilidades en consecuencia mecánica inmediata.

---

## Ejemplo

Un personaje usa Supervivencia para leer huellas rotas al borde de un camino inundado. Ese uso puede revelar por dónde pasó un grupo, qué ruta sigue siendo viable y qué señales del terreno conviene evitar.

Por sí mismo, ese uso no daña a un enemigo, no cambia la iniciativa ni impone una condición mecánica.

Si más adelante el personaje desbloquea una Técnica vinculada al rastreo o a la lectura de campo, esa Técnica sí puede añadir una consecuencia mecánica definida a ese mismo tipo de acción entrenada.
