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
  - core-books/transcendence-corebook/04-skills-and-proficiencies/en/specializations.md
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

Las especializaciones son dominios entrenables. No representan poderes que el personaje simplemente posee, sino disciplinas que ha practicado: cosas que pueden intentarse, fallarse y refinarse con el tiempo. Una característica mide lo que el personaje es capaz de hacer por naturaleza. Una especialización mide lo que ha elegido practicar.

En creación de personaje, las especializaciones ayudan a definir qué sabe hacer el personaje, cómo aborda problemas y por qué se diferencia de otros con características similares.

---

## Para qué sirven

Sin clases que asignen roles, la diferenciación entre personajes depende de lo que cada uno elige desarrollar. Dos personajes con Sabiduría similar pueden comportarse de manera radicalmente distinta si uno ha practicado Medicina y el otro ha practicado Supervivencia. El dominio no los define; define cómo afrontan los mismos problemas.

Las especializaciones habilitan el acceso a Técnicas. Una Técnica no surge de una competencia genérica: nace de un dominio específico que el personaje ya ha trabajado. Sin la especialización de base, la Técnica no existe.

Cada vez que un personaje alcanza un nuevo rango en una especialización, gana +1 a la característica asociada a ese dominio. A esto se le llama **Sinapsis**. Las características no aumentan por asignación libre; aumentan como consecuencia directa del uso practicado.

---

## Especializaciones de inicio

Todo personaje comienza con cuatro especializaciones en Nivel 1 / Novato. Tres provienen del trasfondo, según sus restricciones de categoría. La cuarta es universal: **Vigor**.

Vigor está vinculada a Tenacidad. Todo personaje parte con ella independientemente del trasfondo elegido. Representa el mínimo de resistencia física y tolerancia al esfuerzo necesario para operar en este mundo. No reemplaza los bonificadores de especie a Tenacidad; ambos se acumulan.

La misma especialización no puede escogerse dos veces en la creación. Las demás comienzan en Nivel 0, No entrenado.

---

## Categorías

Las especializaciones se agrupan en cinco categorías según el tipo de dominio que representan. Estas categorías no son compartimentos estancos: una especialización pertenece a una categoría por lo que abarca, no por la característica a la que está vinculada.

| Categoría | Tipo de dominio |
| --- | --- |
| Física | Técnica corporal, movimiento, esfuerzo, control físico practicado |
| Mental | Interpretación, astucia, atención, lectura situacional, razonamiento adaptativo |
| Social | Influencia, expresión, proyección, engaño, control interpersonal |
| Artes y Oficios | Fabricar, reparar, preparar, extraer, trabajo práctico aplicado |
| Conocimiento | Estudio formal, interpretación académica, saber estructurado, comprensión técnica |

Una especialización Física puede estar vinculada a Fuerza, Agilidad o Tenacidad según lo que abarca. Una especialización Social puede estar vinculada a Astucia, Compostura, Aura o Presencia. La categoría organiza; la característica determina la fórmula de tirada.

---

## Tirada de Especialización

Cuando un personaje actúa a partir de una especialización, el resultado se determina mediante una **Tirada de Especialización (T.E.)**.

```
T.E. = 1d10 + Nivel + Rango + Característica + Bonificaciones
```

| Componente | Qué representa |
| --- | --- |
| **Nivel** | Número de niveles de competencia alcanzados en esa especialización |
| **Rango** | Número de rango actual (Novato = 1, Adepto = 2, Experto = 3, Maestro = 4, Consumado = 5, Trascendente = 6) |
| **Característica** | Valor de la característica vinculada a esa especialización |
| **Bonificaciones** | Situacionales, de equipo o de Técnicas activas |

### Sin entrenamiento

Cualquier personaje puede intentar una tirada en cualquier especialización, incluso si nunca la ha practicado. Un personaje **No entrenado** usa solo el dado y la característica:

```
T.E. (sin entrenamiento) = 1d10 + Característica
```

El nivel y el rango son cero. El umbral de dificultad hace el resto: pruebas de nivel avanzado son inalcanzables sin entrenamiento. Desarrollar competencia no habilita el intento, sino que hace alcanzables ciertos resultados.

---

## Cómo se adquieren

Las especializaciones se desarrollan mediante uso. Cada vez que un personaje utiliza la **Ventaja de Aprendizaje** en una T.E., acumula **Progresos** hacia el siguiente nivel de competencia. No es el resultado de la tirada lo que genera progreso, sino la elección deliberada de aprender de ella.

| Afinidad | Progresos necesarios por nivel |
| --- | --- |
| Sin afinidad mayor | 10 |
| Con afinidad mayor | 5 |

La afinidad mayor la determina el trasfondo. Un personaje con trasfondo marcial tiene afinidad mayor en especializaciones Físicas; uno con trasfondo artesano, en Artes y Oficios. Esto no bloquea el acceso a otras especializaciones: reduce el costo de progresar en las propias.

El Narrador valida si la especialización usada se sustenta narrativamente antes de que genere Progresos. La intención del personaje debe ser coherente con el dominio que declara. Un personaje no puede declarar Trampas para analizar el comportamiento de una criatura si no hay una razón narrativa que lo sostenga. El dominio que se practica debe reflejar la acción real.

No hay límite en cuántas especializaciones puede desarrollar un personaje. El límite es práctico: cada especialización exige tiempo, tiradas y decisiones. Priorizar una ralentiza las demás.

---

## Rangos y Sinapsis

La competencia en una especialización se mide en rangos. Cada rango agrupa dos niveles y tiene un nombre que refleja el dominio alcanzado.

| Rango | Nombre | Niveles | Sinapsis al entrar |
| --- | --- | --- | --- |
| 0 | No entrenado | — | — |
| 1 | Novato | 1–2 | +1 a característica |
| 2 | Adepto | 3–4 | +1 a característica |
| 3 | Experto | 5–6 | +1 a característica |
| 4 | Maestro | 7–8 | +1 a característica |
| 5 | Consumado | 9–10 | +1 a característica |
| 6 | Trascendente | 11+ | +1 a característica |

Alcanzar el nivel umbral de un nuevo rango otorga automáticamente +1 a la característica asociada a esa especialización. Esto es la Sinapsis: el incremento de una característica como consecuencia directa de practicar dominios vinculados a ella.

La tensión es estructural. Alcanzar el Rango 1 en muchas especializaciones distintas genera Sinapsis en múltiples características. Profundizar en una sola genera bonificadores de T.E. mayores y acceso a Técnicas más avanzadas. Ninguna de las dos rutas es superior por defecto; cada una prioriza una forma distinta de crecimiento.

---

## Uso directo y Técnicas

Usar una especialización produce un efecto narrativo. El personaje observa, interpreta, actúa — pero el estado mecánico de la escena no cambia de forma automática. Cambiar ese estado requiere acciones adicionales que partan de lo aprendido.

Una **Técnica** es diferente. Es una aplicación específica que el personaje desbloquea al alcanzar cierto nivel de competencia en una o más especializaciones. A diferencia del uso directo, una Técnica produce una consecuencia mecánica definida en el momento de activarse. Su detalle completo aparece en el capítulo correspondiente.

Esta distinción es estructural. El uso directo de una especialización abre posibilidades. La Técnica convierte una de esas posibilidades en consecuencia mecánica inmediata.

---

## Ejemplo

Un personaje usa Supervivencia para leer huellas rotas al borde de un camino inundado. Ese uso puede revelar por dónde pasó un grupo y qué ruta sigue siendo viable, pero no daña a un enemigo, no cambia la iniciativa ni impone una condición por sí mismo. Si más adelante el personaje desbloquea una Técnica vinculada al rastreo o a la lectura de campo, esa Técnica sí puede añadir una consecuencia mecánica definida a ese mismo tipo de acción entrenada.
