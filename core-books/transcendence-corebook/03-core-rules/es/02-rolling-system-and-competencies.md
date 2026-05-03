---
title: "Sistema de Tiradas y Competencias"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 3
status: review
canonical: false
tags: [rolling-system, competencies, attack, defense, impact, resistance, specialization, nr, reference-level, evolutionary-advantage]
related:
  - core-books/transcendence-corebook/03-core-rules/en/02-rolling-system-and-competencies.md
  - core-books/transcendence-corebook/03-core-rules/es/01-general-rules.md
  - core-books/transcendence-corebook/12-gm-toolkit/es/01-condiciones-del-entorno.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/es/01-especializaciones.md
authority_refs:
  - Transcendence-design/docs/system/roll-types.md
  - Transcendence-design/docs/system/competencies.md
  - Transcendence-design/docs/system/difficulty-thresholds.md
  - Transcendence-design/docs/system/characteristics.md
  - Transcendence-design/data/system/roll-types.yaml
  - Transcendence-design/data/system/competencies.yaml
  - Transcendence-design/data/system/difficulty-thresholds.yaml
  - Transcendence-design/data/system/characteristics.yaml
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
---

# Sistema de Tiradas y Competencias

## Resolver una tirada

Las tiradas resuelven acciones cuando el resultado no está asegurado y existe una consecuencia relevante. Pueden aparecer en combate, exploración, interacción social o cualquier escena donde la presión haga que fallar importe.

La base de una tirada es un `d10`. A ese resultado se suman características, competencias, equipo, rasgos, condiciones y otros modificadores según el tipo de acción.

Los personajes jugadores pueden arriesgar ciertas tiradas mediante **Ventaja Evolutiva**. Los PNJ y otras criaturas usan una capa más directa, basada en Rasgos, capacidades especiales y la función que cumplen dentro de la escena.

---

## Ventaja Evolutiva

La Ventaja Evolutiva representa la forma en que un personaje afronta una acción entrenada bajo presión. Antes de tirar, el jugador elige si prioriza la ejecución inmediata o la posibilidad de aprendizaje.

Esta elección solo aplica a tiradas que usan competencias: **Tirada de Ataque**, **Tirada de Defensa**, **Tirada de Resistencia** y **Tirada de Especialización**. No aplica a Tiradas de Característica ni a Tiradas de Rasgo de Personalidad.

### Ventaja en la Ejecución

El jugador lanza dos dados y usa el resultado mayor para resolver la tirada.

La acción tiene más probabilidad de éxito, pero no puede generar progreso. El personaje se concentra en ejecutar bien, no en exponerse al error necesario para aprender.

### Ventaja en el Aprendizaje

El jugador lanza dos dados y usa el resultado menor para resolver la tirada. El dado mayor queda reservado como dado de aprendizaje.

Después de resolver la acción, se compara el dado de aprendizaje contra el resultado usado en la tirada y el rango de la competencia que puede progresar.

```text
Dado de aprendizaje > dado usado + rango de competencia
```

Si el dado de aprendizaje supera esa suma, el personaje marca 1 punto de progreso en la competencia correspondiente, siempre que la acción cumpla las condiciones de progresión de su tipo.

La tirada puede fallar y aun así enseñar. También puede tener éxito sin generar progreso. La competencia que progresa depende del tipo de acción y de lo que ocurrió en la escena.

---

## PNJ y otras criaturas

Los PNJ, adversarios y criaturas del Narrador no siguen las mismas reglas de progresión que los personajes jugadores. No eligen Ventaja Evolutiva ni acumulan progreso de competencia durante la partida.

En su lugar, usan **Rasgos**: ventajas, desventajas, resistencias, capacidades especiales o comportamientos ligados a su naturaleza, entorno, estado emocional o rol de combate.

---

## Tipos de tirada

Las fórmulas de este capítulo usan características como Agilidad, Fuerza, Tenacidad, Compostura y Resiliencia. Estos valores se asignan durante la creación del personaje. Aquí aparecen solo como partes de cada tirada.

---

### Tirada de Ataque (T.A.)

La Tirada de Ataque mide si una ofensiva conecta. Puede venir de un arma, una maniobra, una habilidad o un objeto usado bajo presión. Se compara contra la defensa, la resistencia u otra tirada opuesta que corresponda.

**Fórmula:**

```text
T.A. = 1d10 + nivel de competencia + rango de competencia + característica asociada + bonificadores adicionales
```

El nivel de competencia aporta práctica acumulada. El rango de competencia representa el grado de dominio alcanzado. La característica asociada aporta la aptitud física, mental o sensorial que sostiene la ejecución.

---

### Tirada de Defensa (T.D.)

La Tirada de Defensa mide si una criatura evita un ataque entrante. Combina reflejos, movilidad, entrenamiento evasivo, armadura en la zona amenazada y protección adicional de escudos u otros efectos defensivos.

**Fórmula:**

```text
T.D. = 1d10 + Evasión aplicable + Agilidad aplicable + bonificadores defensivos
```

La **Evasión aplicable** incluye el nivel y el rango de Evasión que pueden usarse según la armadura que protege la zona impactada.

```text
Evasión aplicable = nivel de Evasión aplicable + rango de Evasión aplicable
```

Tanto la Evasión como la Agilidad dependen del tipo de armadura que proteja la zona impactada:

| Armadura en la zona | Evasión aplicable | Agilidad aplicable |
| --- | --- | --- |
| Sin armadura | Evasión completa | Agilidad completa |
| Ligera | Evasión completa | Agilidad completa |
| Intermedia | Mitad de Evasión, mínimo 1 | Mitad de Agilidad, mínimo 1 |
| Pesada | 0 | 0 |

Para armadura intermedia, calcula por separado la mitad de la Evasión y la mitad de la Agilidad. Cada resultado se redondea hacia arriba, salvo que una regla específica indique lo contrario.

El escudo aporta un bonificador general a la T.D. como parte del equipo defensivo. Su competencia no progresa por esta tirada genérica; progresa mediante Técnicas y maniobras de escudo.

La T.D. debe igualar o superar la tirada ofensiva del oponente para evitar daño o efectos adicionales. Si falla, la armadura de la zona todavía puede absorber parte del impacto. El detalle completo de zonas, piezas y bloqueo se describe en el capítulo de Equipo.

---

### Tirada de Impacto (T.I.)

La Tirada de Impacto se resuelve después de que un ataque supera la defensa o la tirada opuesta correspondiente. Define cuánto daño llega al objetivo.

La T.I. no usa un `d10` base. Usa el dado de daño del arma, multiplicado por el rango de competencia del personaje con esa arma. La característica asociada y el grado del arma añaden ejecución y potencia del equipo.

**Fórmula:**

```text
T.I. = (rango de competencia × daño del arma) + (característica asociada × grado del arma)
```

#### Daño de arma

El daño base del arma usa el dado indicado por su categoría: `d4`, `d6`, `d8`, `d10` o `d12`.

Si un personaje tiene rango 3 con un arma de daño `d8`, tira `3d8` como base de impacto antes de sumar la característica asociada por grado del arma.

#### Impacto con armas sin competencia

Un personaje puede atacar con un arma en la que no posee competencia. El golpe puede conectar, pero el impacto se reduce.

**Fórmula:**

```text
T.I. sin competencia = ((1 × daño del arma) + (característica asociada × grado del arma)) / 2
```

Esta fórmula mantiene la posibilidad de usar el arma, pero limita cuánto puede extraer de ella un personaje sin entrenamiento.

---

### Tirada de Característica (T.C.)

La Tirada de Característica se usa cuando la acción depende de una aptitud general: Fuerza, Agilidad, Tenacidad, Sabiduría o cualquier otra característica relevante.

No usa entrenamiento específico. Toma la aptitud del personaje y la aplica a una situación concreta.

**Fórmula:**

```text
T.C. = 1d10 + característica + Nivel de Referencia + bonificadores adicionales
```

La T.C. entra en juego cuando no hay una competencia específica que resuelva mejor la acción. No genera progreso por sí sola.

---

### Tirada de Resistencia (T.R.)

La Tirada de Resistencia resuelve si una criatura soporta, evita o reduce un efecto perjudicial: veneno, infección, aflicción, maldición o alteración.

La característica base depende del tipo de efecto. La resistencia correspondiente añade experiencia acumulada frente a ese peligro.

**Fórmulas:**

| Efecto | Fórmula |
| --- | --- |
| Venenos o infecciones | `1d10 + Tenacidad + resistencia correspondiente + bonificadores adicionales` |
| Aflicciones o maldiciones | `1d10 + Compostura + resistencia correspondiente + bonificadores adicionales` |
| Alteraciones | `1d10 + Resiliencia + resistencia correspondiente + bonificadores adicionales` |

El objetivo es igualar o superar la dificultad del efecto para evitarlo, mitigarlo o reducir sus consecuencias.

---

### Tirada de Especialización (T.E.)

La Tirada de Especialización se usa para habilidades entrenadas: escalar, nadar, desactivar trampas, escapar de ataduras o cualquier práctica definida como especialización.

**Fórmula:**

```text
T.E. = 1d10 + nivel de competencia en la especialización + rango de competencia + característica asociada + bonificadores adicionales
```

El nivel aporta práctica acumulada. El rango aporta el grado de dominio alcanzado en esa especialización.

---

### Tirada de Rasgo de Personalidad (T.P.)

Durante la exploración o el conflicto, un jugador puede proponer que uno de sus Rasgos de Personalidad influya sobre la situación. Si el Narrador acepta la justificación, el personaje puede realizar una Tirada de Rasgo de Personalidad en lugar de una Tirada de Característica o de Especialización.

**Fórmula:**

```text
T.P. = 2d10
```

Esta tirada no depende de competencias y no genera progreso. Depende del rasgo invocado, de su peso en la escena y de la aprobación del Narrador.

---

## Umbrales de dificultad

Toda tirada se compara contra un número. Ese número puede provenir de la tirada de otro participante o de un umbral fijo establecido por el sistema o el Narrador.

Cuando el desafío proviene de un oponente activo, ambas partes tiran y comparan resultados directamente. Cuando proviene del entorno, de la complejidad de una tarea o de otro sistema, el Narrador fija un umbral usando uno de los cinco niveles de dificultad.

```text
Umbral = base + NR
```

**Base** es el valor fijo del nivel de dificultad elegido. **NR** es el Nivel de Referencia del contexto: el de la criatura o entidad que plantea el reto, o el equivalente que el Narrador asigna al entorno, obstáculo o tarea.

| Nivel | Base | Fórmula |
| --- | --- | --- |
| **Fundamentos** | 5 | 5 + NR |
| **Desafiante** | 8 | 8 + NR |
| **Rigurosa** | 11 | 11 + NR |
| **Exigente** | 14 | 14 + NR |
| **Extrema** | 17 | 17 + NR |

Estos cinco niveles aplican a todos los sistemas que requieran superar un umbral fijo: T.E., T.C., T.R., fabricación, Agravios y otras pruebas equivalentes.

El Narrador anuncia el nivel de dificultad antes de pedir la tirada, salvo cuando revelar esa información contradiga la naturaleza de la escena. Si la tirada puede generar progreso mediante Ventaja en el Aprendizaje, el jugador debe conocer el umbral antes de elegir cómo tirar.

---

## Competencias

Las competencias indican qué ha practicado un personaje y qué tan lejos ha llevado esa práctica. Algunas pertenecen al combate. Otras pertenecen a supervivencia, conocimiento, oficios, movimiento o destrezas concretas.

Las competencias cumplen dos funciones:

- modifican tiradas
- permiten progresar cuando el personaje las pone a prueba en situaciones relevantes

Las competencias no sustituyen a las características. Las características dan base. Las competencias muestran cuánto ha entrenado, practicado o refinado el personaje esa base.

---

### Niveles y rangos de competencia

Cada competencia posee un nivel y un rango.

- El **nivel de competencia** registra el progreso numérico acumulado.
- El **rango de competencia** resume el grado de dominio alcanzado.

| Rango | Nombre | Niveles |
| --- | --- | --- |
| 0 | No Entrenado | 0 |
| 1 | Novato | 1–2 |
| 2 | Adepto | 3–4 |
| 3 | Experto | 5–6 |
| 4 | Maestro | 7–8 |
| 5 | Consumado | 9–10 |
| 6 | Trascendente | 11+ |

Se obtiene un nuevo rango cada 2 niveles de competencia. Las especializaciones otorgan Sinapsis al entrar en cada nuevo rango, como se describe en el capítulo de Especializaciones.

---

### Competencias iniciales

El trasfondo del personaje determina con qué competencias comienza entrenado. Las competencias otorgadas por el trasfondo empiezan en nivel 1, lo que equivale al rango Novato.

Todas las demás competencias comienzan en nivel 0. El personaje se considera No Entrenado en ellas.

---

### Progresión de competencias

Las competencias aumentan cuando el personaje las pone en riesgo y elige aprender de la acción.

Cada vez que usa Ventaja en el Aprendizaje, la tirada puede generar progreso en una competencia distinta según el tipo de acción y el resultado obtenido.

Para subir un nivel de competencia se requieren:

- 5 puntos de progreso en especializaciones de afinidad mayor
- 10 puntos de progreso en el resto de competencias

La afinidad de una especialización se define en el capítulo de Especializaciones.

---

### Pruebas adecuadas para progresar

No toda acción enseña. Para que exista progreso, la situación debe exigir algo real para el rango actual del personaje.

#### Competencias marciales

Las competencias marciales progresan cuando el personaje enfrenta adversarios de dificultad adecuada y pone su entrenamiento en práctica.

En el caso de armas, el personaje debe atacar, impactar y causar daño efectivo a una criatura cuyo nivel sea al menos igual al NR del personaje -1.

#### Competencias de evasión, armadura, escudo y resistencias

Estas competencias progresan cuando el personaje queda expuesto a peligros relevantes y responde de una forma que deja aprendizaje: evitar, absorber, sobrevivir o soportar la exposición correspondiente.

#### Competencias de especialización

Las especializaciones progresan solo cuando la dificultad de la prueba es coherente con el rango del personaje.

| Rango actual | Puede progresar con pruebas de... |
| --- | --- |
| Novato | Cualquier nivel |
| Adepto | Fundamentos o superior |
| Experto | Desafiante o superior |
| Maestro | Rigurosa o superior |
| Consumado | Exigente o superior |
| Trascendente | Extrema |

---

## Tipos de competencias y sus efectos

### Armas

La competencia en armas mide el dominio de un tipo de arma concreto.

**Bonificadores**

- Cada nivel de competencia con un arma otorga `+1` a la T.A.
- Cada rango de competencia otorga `+1` adicional a la T.A.
- Cada rango de competencia añade un dado de daño a la T.I.

**Progresión**

La competencia en armas aumenta cuando el personaje usa Ventaja en el Aprendizaje, impacta con esa arma u objeto y causa daño efectivo en un enfrentamiento relevante.

---

### Armaduras

La competencia en armaduras cubre el uso eficiente de piezas defensivas. Se separa por tipo: ligera, intermedia y pesada.

**Bonificadores**

- Cada nivel de competencia aumenta en `1` el bloqueo de una armadura de ese tipo cuando esa pieza resuelve el impacto en su zona.

**Progresión**

La competencia en armaduras aumenta con una T.D. fallida bajo Ventaja en el Aprendizaje, siempre que el impacto se resuelva en una zona protegida y la armadura absorba efectivamente parte del daño.

El progreso se aplica al tipo de armadura que protegía esa zona.

---

### Escudos

La competencia en escudos mide el dominio técnico del escudo en combate.

**Bonificadores**

- Cada rango de competencia otorga acceso a Técnicas adicionales según el tipo de escudo.
- Alcanzar Maestro reduce en `grado` la penalización de movimiento del escudo equipado, con mínimo `0`.

**Progresión**

La competencia en escudos aumenta cuando el personaje emplea Técnicas o maniobras de escudo con éxito. No progresa por la T.D. genérica.

---

### Evasión

La competencia en evasión mide la habilidad del personaje para anticipar y evitar ataques.

**Bonificadores**

- Cada nivel de competencia otorga `+1` a la T.D.
- Cada rango de competencia otorga `+1` adicional a la T.D.
- La Evasión se suma a la T.D. según el tipo de armadura que proteja la zona impactada.

**Progresión**

La evasión aumenta con una T.D. exitosa bajo Ventaja en el Aprendizaje, siempre que el personaje evite un ataque o peligro relevante mediante movilidad, anticipación o reflejos.

---

### Especialización

La competencia en una especialización mide el dominio técnico de una habilidad concreta.

**Bonificadores**

- Cada nivel de competencia otorga `+1` a la T.E.
- Cada rango de competencia otorga `+1` adicional a la T.E.

**Progresión**

La especialización aumenta al superar pruebas apropiadas para el rango actual del personaje y al cumplir la condición de aprendizaje de Ventaja Evolutiva.

---

### Resistencias

Las resistencias cubren peligros concretos que buscan intoxicar, infectar, alterar, afligir o maldecir a una criatura. No se entrenan solo por repetición controlada. Suelen crecer por exposición, supervivencia y adaptación.

Las resistencias no reducen Impacto, daño elemental ni Heridas. El daño se resuelve por la relación entre Impacto, Bloqueo y las reglas de Heridas o PV. Si un ataque de fuego, agua, luz u otro origen elemental causa daño, ese daño sigue el flujo normal salvo que una regla específica diga lo contrario.

#### Veneno

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R. contra venenos.

#### Infección

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R. contra infecciones.

#### Aflicción

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R. contra aflicciones.
- Cada rango de competencia otorga `+1` a las T.R. de Aflicción realizadas durante meditación.

#### Alteración

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R. contra alteraciones.

#### Maldiciones

**Bonificador**

- Cada nivel de competencia otorga `+1` a tiradas para detectar o resistir maldiciones.

**Progresión general de resistencias**

Las resistencias aumentan con una T.R. fallida bajo Ventaja en el Aprendizaje, siempre que el personaje sufra y sobreviva al efecto correspondiente.

Resistir por completo un peligro no enseña lo mismo que soportarlo.

#### Sobre resistencia elemental

La **Resistencia Elemental** y la **Vulnerabilidad Elemental** no son competencias. No progresan mediante Ventaja Evolutiva y no forman parte de las resistencias entrenables del personaje.

Cuando una criatura, material, objeto, Técnica o efecto tenga resistencia o vulnerabilidad frente a un origen elemental, se resuelve mediante las reglas de **Daño Elemental y Afinidades**.


---

## Nivel de Referencia

El **Nivel de Referencia** (**NR**) resume la competencia global de un personaje. No se elige ni se asigna directamente. Sale del conjunto de competencias que el personaje ha desarrollado.

---

### NR de personaje

El NR de un personaje se calcula como el promedio redondeado hacia arriba de todas sus competencias base.

```text
NRₚ = ⌈promedio de todas las competencias base del personaje⌉
```

Se incluyen todas las competencias listadas en la hoja del personaje con valor numérico. Las competencias marcadas como `—` no se incluyen en el cálculo.

---

### NR de grupo

Cuando el encuentro involucra a varios personajes jugadores, el NR del grupo se calcula como el promedio redondeado hacia arriba de los NR individuales de todos los PJ activos en el encuentro.

```text
NRg = ⌈promedio de los NRₚ de todos los PJ activos en el encuentro⌉
```

El Narrador usa el NR de grupo para escalar criaturas, fijar dificultades base y comparar fuerzas entre bandos sin revisar cada competencia individual.

---

### Actualización del NR

El NRₚ puede revisarse cuando:

- el personaje gana nuevas competencias
- varias competencias relevantes suben de rango
- comienza un nuevo arco o episodio

No es necesario recalcularlo en cada sesión.

---

### NR en la Tirada de Característica

El NR entra directamente en la Tirada de Característica. A medida que el personaje se vuelve más competente en general, responde mejor incluso cuando la acción no depende de un entrenamiento específico.

El NR no reemplaza una competencia entrenada. Evita que la experiencia global del personaje desaparezca en pruebas básicas.

---

## Relación entre tiradas y competencias

| Tirada | Competencia utilizada | Progresión con Ventaja en el Aprendizaje |
| --- | --- | --- |
| T.A. | Competencia del arma u objeto empleado | Si el ataque tiene éxito y causa daño efectivo, progresa el arma u objeto usado. |
| T.D. | Evasión aplicable según armadura | Si la tirada tiene éxito, progresa Evasión. Si falla y la armadura absorbe impacto, progresa el tipo de armadura de la zona resuelta. |
| T.I. | Rango de competencia del arma | No progresa por sí sola. |
| T.C. | Ninguna por defecto | No progresa por sí sola. |
| T.R. | Resistencia correspondiente al tipo de efecto | Si falla y el efecto se sufre, progresa la resistencia correspondiente. |
| T.E. | Competencia de la especialización implicada | Si la tirada tiene éxito y la dificultad es adecuada, progresa la especialización usada. |
| T.P. | Ninguna | No progresa por sí sola. |

La competencia de escudo progresa aparte, mediante Técnicas y maniobras de escudo exitosas.

---

## Ejemplo

Un personaje intenta esquivar el golpe de una criatura pesada mientras usa Ventaja en el Aprendizaje. Lanza dos dados y resuelve la T.D. con el dado menor. El dado mayor queda reservado como dado de aprendizaje.

Si evita el ataque y el dado de aprendizaje supera la condición de progreso, la situación puede generar progreso en Evasión.

Si falla la T.D., pero la armadura de la zona resuelta absorbe parte del impacto, la situación puede generar progreso en el tipo de armadura correspondiente.

La competencia que progresa depende del resultado de la escena, no solo del tipo de tirada.
