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
  - core-books/transcendence-corebook/03-core-rules/es/03-environmental-conditions.md
  - core-books/transcendence-corebook/08-skills-and-proficiencies/es/especializaciones.md
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

## Sistema de Tiradas

El Sistema de Tiradas determina el resultado de una acción, ya sea en combate, exploración o interacción social. Las tiradas utilizan un `d10` modificado por características, competencias, equipo y circunstancias.

Los jugadores eligen cómo afrontar ciertas acciones mediante la Ventaja Evolutiva. Los PNJs y criaturas emplean un sistema simplificado acorde con su función narrativa.

## Ventaja Evolutiva

Para las tiradas de Ataque, Defensa, Resistencia y Especialización, los jugadores pueden elegir una de dos aproximaciones antes de tirar.

### Ventaja en la Ejecución

El jugador lanza dos dados y escoge el resultado mayor. La posibilidad de aprendizaje derivada de esa tirada se pierde.

### Ventaja en el Aprendizaje

El jugador lanza dos dados y utiliza el resultado menor para resolver la acción.

El dado mayor se reserva para la tirada de aprendizaje.

Si ese dado mayor supera la suma del dado menor y el rango de la competencia que la regla de progresión de esa tirada designe, el personaje marca un punto de progreso en esa competencia.

## PNJs y otras criaturas

Los PNJs y monstruos no siguen necesariamente las mismas reglas de progresión que los personajes jugadores. En su lugar, usan Rasgos: ventajas, desventajas o capacidades especiales ligadas a su naturaleza, comportamiento, entorno, estado emocional o rol de combate.

## Tipos de Tirada

Las fórmulas de este capítulo incluyen **características** como Agilidad, Fuerza, Tenacidad, Compostura y Resiliencia. Estos valores se definen y se asignan durante la creación del personaje, en el capítulo correspondiente. Aquí aparecen como componentes de las fórmulas de tirada.

### Tirada de Ataque (T.A.)

La Tirada de Ataque representa la capacidad del personaje para asestar un golpe efectivo con un arma, maniobra, habilidad u objeto. Se utiliza para impactar a un objetivo y superar su defensa, resistencia u otra tirada opuesta, según corresponda.

**Fórmula:**

`Tirada de Ataque = 1d10 + Nivel de Competencia con arma/objeto + Característica asociada`

La competencia refleja el dominio técnico del personaje con el medio que emplea, mientras que la característica asociada representa la aptitud física, mental o marcial con la que ejecuta la acción.

### Tirada de Defensa (T.D.)

La Tirada de Defensa representa la capacidad del personaje para evitar un ataque entrante. Combina reflejos, movilidad, entrenamiento evasivo, el tipo de armadura en la zona amenazada y la protección adicional que aporte un escudo u otros efectos defensivos.

**Fórmula:**

`Tirada de Defensa = 1d10 + Nivel de Competencia Evasiva + Agilidad aplicable + Bonificadores defensivos`

La Agilidad aplicable depende del tipo de armadura que proteja la zona impactada:

- armadura ligera: usa toda la Agilidad
- armadura intermedia: usa la mitad de la Agilidad, mínimo 1
- armadura pesada: no usa Agilidad

El escudo aporta un bonificador general a la T.D. como parte del equipo defensivo, pero su competencia progresa por Técnicas y maniobras propias, no por la tirada defensiva genérica.

Su objetivo es igualar o superar la tirada ofensiva del oponente para evitar el daño o los efectos adicionales del ataque. Si no lo logra, la armadura de la zona todavía puede absorber parte del impacto. El detalle completo de zonas, piezas y bloqueo pertenece al capítulo de Equipo.

### Tirada de Impacto (T.I.)

La Tirada de Impacto determina el daño real que se inflige al objetivo una vez que el ataque ha superado la defensa o la tirada opuesta correspondiente.

En esta tirada, el rango de competencia define cuántos dados de daño puede aprovechar el personaje, mientras que la característica asociada y el grado del arma representan la calidad de la ejecución y la potencia del equipo utilizado.

**Fórmula:**

`Impacto = (Rango de Competencia × Daño del arma) + (Característica asociada × Grado del arma)`

#### Daño de arma

El daño base del arma se expresa mediante su dado correspondiente: `d4`, `d6`, `d8`, `d10` o `d12`. Ese valor se multiplica por el rango de competencia del personaje con el arma empleada.

#### Impacto con armas sin competencia

Cuando un personaje utiliza un arma en la que no posee competencia, puede atacar, pero su capacidad de causar daño efectivo se reduce de forma considerable.

**Fórmula:**

`Tirada de Impacto = ((1 × Daño del arma) + (Característica asociada × Grado)) / 2`

Esto representa una ejecución ineficiente y una menor capacidad para aprovechar correctamente el arma.

### Tirada de Característica (T.C.)

La Tirada de Característica se utiliza cuando una acción depende principalmente de una aptitud general del personaje, como Fuerza, Agilidad, Tenacidad, Sabiduría o cualquier otra característica relevante.

No representa entrenamiento específico, sino capacidad general aplicada a una situación concreta.

**Fórmula:**

`Tirada de Característica = 1d10 + Característica + Nivel de Referencia + Bonificadores adicionales`

Se usa para resolver acciones que dependen de cualidades innatas o desarrolladas del personaje, especialmente cuando no interviene una competencia específica.

### Tirada de Resistencia (T.R.)

La Tirada de Resistencia representa la capacidad del personaje para soportar o superar efectos perjudiciales como venenos, infecciones, aflicciones, maldiciones o alteraciones.

La característica base depende del tipo de efecto enfrentado, mientras que la competencia en la resistencia correspondiente refleja la experiencia acumulada del personaje frente a ese peligro.

**Fórmulas:**

- Resistencia a venenos o infecciones: `1d10 + Tenacidad + Resistencias + Bonificadores adicionales`
- Resistencia a aflicciones o maldiciones: `1d10 + Compostura + Resistencias + Bonificadores adicionales`
- Resistencia a alteraciones: `1d10 + Resiliencia + Resistencias + Bonificadores adicionales`

El objetivo es igualar o superar la dificultad del efecto para evitarlo, mitigarlo o reducir sus consecuencias.

### Tirada de Especialización (T.E.)

La Tirada de Especialización refleja el dominio del personaje en una habilidad concreta, como escalar, nadar, desactivar trampas o escapar de ataduras. A diferencia de una Tirada de Característica, aquí sí existe entrenamiento específico.

**Fórmula:**

`Tirada de Especialización = 1d10 + Nivel de Competencia en la Especialización + Rango de Competencia + Característica asociada + Bonificadores adicionales`

El nivel de competencia representa la experiencia acumulada, mientras que el rango resume el grado general de dominio alcanzado en esa especialización.

### Tirada de Rasgo de Personalidad (T.P.)

Durante la exploración o el conflicto, un jugador puede proponer que uno de sus Rasgos de Personalidad influya de manera decisiva en la situación. Si el Narrador acepta la justificación, el personaje puede realizar una Tirada de Rasgo de Personalidad en lugar de una Tirada de Característica o de Especialización.

**Fórmula:**

`Tirada de Rasgo de Personalidad = 2d10`

Esta tirada no depende de competencias, sino de la fuerza narrativa y psicológica del rasgo invocado.

## Umbrales de Dificultad

Toda tirada se compara contra un número. Ese número puede provenir de la tirada de otro participante o de un umbral fijo establecido por el sistema o el Narrador.

Cuando el desafío proviene de un oponente activo, ambas partes tiran y se comparan resultados directamente. Cuando proviene del entorno, de la complejidad de una tarea o de otro sistema, el Narrador fija un umbral usando uno de los cinco niveles de dificultad.

```text
Umbral = Base + NR
```

**Base** es el valor fijo del nivel de dificultad elegido. **NR** es el Nivel de Referencia del contexto: el de la criatura o entidad que plantea el reto, o el equivalente que el Narrador asigna al entorno o a la tarea.

| Nivel | Base | Fórmula |
| --- | --- | --- |
| **Fundamentos** | 5 | 5 + NR |
| **Desafiante** | 8 | 8 + NR |
| **Rigurosa** | 11 | 11 + NR |
| **Exigente** | 14 | 14 + NR |
| **Extrema** | 17 | 17 + NR |

Estos cinco niveles aplican a todos los sistemas del juego: T.E., T.C., T.R., fabricación, Agravios y cualquier otra prueba que requiera superar un umbral fijo. El Narrador anuncia el nivel antes de pedir la tirada. El jugador conoce el umbral antes de decidir entre Ventaja en la Ejecución o Ventaja en el Aprendizaje.

---

## Competencias

Las competencias representan el grado de dominio que un personaje posee en un campo específico. Algunas están orientadas al combate, otras a la supervivencia, otras al conocimiento o a destrezas concretas.

Las competencias cumplen dos funciones:

- modifican tiradas
- permiten progresar a medida que el personaje las pone a prueba en situaciones relevantes

Las competencias no sustituyen a las características: ambas operan juntas. Las características expresan el potencial del personaje; las competencias expresan cuánto ha entrenado, practicado o refinado ese potencial.

### Niveles y rangos de competencia

Cada competencia posee un nivel y un rango.

- El nivel de competencia representa el progreso numérico acumulado.
- El rango de competencia representa el grado general de dominio alcanzado.

| Rango | Nombre | Niveles |
| --- | --- | --- |
| 0 | No Entrenado | — |
| 1 | Novato | 1–2 |
| 2 | Adepto | 3–4 |
| 3 | Experto | 5–6 |
| 4 | Maestro | 7–8 |
| 5 | Consumado | 9–10 |
| 6 | Trascendente | 11+ |

Se obtiene un nuevo rango cada 2 niveles de competencia. Las especializaciones otorgan Sinapsis al entrar en cada nuevo rango — ver el capítulo de Especializaciones.

### Competencias iniciales

El trasfondo del personaje determina con qué competencias comienza entrenado. Las competencias otorgadas por el trasfondo empiezan en nivel 1, lo que equivale al rango Novato.

Todas las demás competencias comienzan en nivel 0, por lo que el personaje se considera No Entrenado en ellas.

### Progresión de competencias

Las competencias aumentan cuando el personaje las pone en juego de forma significativa y opta por una aproximación orientada al aprendizaje.

Cada vez que un personaje utiliza Ventaja en el Aprendizaje, la tirada puede generar progreso en una competencia distinta según el tipo de acción y el resultado obtenido.

Para subir un nivel de competencia se requieren:

- 5 puntos de progreso en especializaciones de afinidad mayor.
- 10 puntos de progreso en el resto de competencias.

### Pruebas adecuadas para progresar

No toda acción sirve para mejorar una competencia. Para que exista progreso, la situación debe representar un desafío apropiado.

#### Competencias marciales

Las competencias marciales progresan cuando el personaje se enfrenta a adversarios de dificultad adecuada y pone realmente en práctica su entrenamiento.

En el caso de armas, el personaje debe atacar y golpear a criaturas cuyo nivel sea, al menos, igual a su nivel de referencia -1.
Además, para que la competencia progrese, ese ataque debe causar daño efectivo.

#### Competencias de evasión, armadura, escudo y resistencias

Estas competencias progresan cuando el personaje se convierte en objetivo de peligros relevantes y responde a ellos de una forma que produzca aprendizaje real: evitar, absorber, sobrevivir o soportar la exposición correspondiente.

#### Competencias de especialización

Las especializaciones progresan solo cuando la dificultad de la prueba es coherente con el rango del personaje.

- Novato: puede progresar con pruebas de cualquier nivel.
- Adepto: progresa con pruebas de Fundamentos o superiores.
- Experto: progresa con pruebas Desafiantes o superiores.
- Maestro: progresa con pruebas Rigurosas o superiores.
- Consumado: progresa con pruebas Exigentes o superiores.
- Trascendente: progresa con pruebas Extremas.

## Tipos de competencias y sus efectos

### Armas

Representan el dominio de un tipo de arma concreto.

**Bonificadores**

- Cada nivel de competencia con un arma otorga `+1` a la T.A.
- Cada rango de competencia otorga `+1` adicional a la T.A. y un dado adicional a la T.I.

**Progresión**

La competencia en armas aumenta cuando el personaje usa Ventaja en el Aprendizaje, impacta con esa arma u objeto y causa daño efectivo en un enfrentamiento relevante.

### Armaduras

Reflejan la capacidad del personaje para usar armaduras de forma eficiente. Se separan por tipo: ligera, intermedia y pesada.

**Bonificadores**

- Cada nivel de competencia aumenta en 1 el bloqueo de la armadura del tipo correspondiente cuando esa pieza resuelve el impacto en su zona.
- Alcanzar Maestro reduce la penalización de movimiento de ese tipo de armadura cuando corresponda.

**Progresión**

La competencia en armaduras aumenta con una T.D. fallida bajo Ventaja en el Aprendizaje, siempre que el impacto se resuelva en una zona protegida y la armadura absorba efectivamente parte del daño. El progreso se aplica al tipo de armadura que protegía esa zona.

### Escudos

Representan el dominio técnico del uso de escudos en combate.

**Bonificadores**

- El escudo aporta un bonificador general a la T.D. según el equipo usado.
- Cada rango de competencia otorga acceso a Técnicas adicionales según el tipo de escudo.

**Progresión**

La competencia en escudos aumenta cuando el personaje emplea Técnicas de escudo de forma efectiva. No progresa por la T.D. genérica.

### Evasión

La evasión representa la habilidad del personaje para anticipar y evitar ataques.

**Bonificadores**

- Cada nivel de competencia otorga `+1` a la T.D.
- Cada rango de competencia otorga `+1` a la T.D.

**Progresión**

La evasión aumenta con una T.D. exitosa bajo Ventaja en el Aprendizaje, cuando el personaje evita con éxito ataques o peligros relevantes mediante su movilidad y reflejos.

### Especialización

La competencia en especialización refleja el dominio técnico en una habilidad concreta.

**Bonificadores**

- Cada nivel de competencia otorga `+1` a la T.E.
- Cada rango de competencia otorga `+1` adicional a la T.E.

**Progresión**

La especialización aumenta al superar pruebas apropiadas para el rango actual del personaje.

### Resistencias

Las resistencias representan la capacidad del personaje para soportar tipos concretos de peligro. A diferencia de otras competencias, suelen desarrollarse a través de la exposición, la supervivencia y la adaptación.

#### Daño elemental

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R contra efectos producidos por daño elemental.

#### Física

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R en casos generales de resistencia física.

#### Veneno

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R contra venenos.

#### Infección

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R contra infecciones.

#### Aflicción

**Bonificador**

- Cada nivel de competencia otorga `+1` a la tirada correspondiente contra aflicciones.
- Cada rango de competencia otorga `+1` a las T.R de Aflicciones durante la meditación.

#### Alteración

**Bonificador**

- Cada nivel de competencia otorga `+1` a la T.R contra alteraciones.

#### Maldiciones

**Bonificador**

- Cada nivel de competencia otorga `+1` a la tirada correspondiente para detectar o resistir maldiciones.

**Progresión general de resistencias**

Las resistencias aumentan con una T.R. fallida bajo Ventaja en el Aprendizaje, siempre que el personaje realmente sufra y sobreviva al efecto correspondiente. Resistir por completo un peligro no genera por sí mismo el mismo aprendizaje que soportarlo.

## Nivel de Referencia

El Nivel de Referencia (NR) es un valor derivado que resume la competencia global de un personaje. No se elige ni se asigna directamente — emerge del conjunto de competencias que el personaje ha desarrollado.

### NR de Personaje

El NR de un personaje se calcula como el promedio redondeado hacia arriba de todas sus competencias base:

`NRₚ = ⌈promedio de todas las competencias iniciales del personaje⌉`

Se incluyen todas las competencias listadas en la hoja del personaje con un valor inicial distinto de "—".

### NR de Grupo

Cuando el encuentro involucra a varios personajes jugadores, el NR del grupo es:

`NRg = ⌈promedio de los NRₚ de todos los PJ activos en el encuentro⌉`

El Narrador usa el NR de grupo para escalar criaturas, fijar dificultades base y comparar fuerzas entre bandos sin tener que consultar cada competencia individual.

### Actualización del NR

El NRₚ puede revisarse cuando:

- el personaje gana nuevas competencias
- suben varios rangos en competencias relevantes
- al inicio de un arco o episodio

No es necesario recalcularlo en cada sesión.

### NR en la Tirada de Característica

El NR entra directamente en la Tirada de Característica. Representa que, a medida que el personaje se vuelve más competente en general, también mejora su capacidad de respuesta en situaciones que dependen de aptitudes generales y no de entrenamiento específico. Un personaje más capaz globalmente es también más capaz en lo que no ha entrenado a fondo.

---

## Relación entre tiradas y competencias

| Tirada | Competencia utilizada | Progresión con Ventaja en el Aprendizaje |
| --- | --- | --- |
| T.A. | competencia del arma u objeto empleado | si el ataque tiene éxito y causa daño, progresa el arma u objeto usado |
| T.D. | Evasión | si la tirada tiene éxito, progresa Evasión; si falla y la armadura absorbe impacto, progresa el tipo de armadura de la zona resuelta |
| T.I. | rango de competencia del arma (factor principal) | no progresa por sí sola |
| T.C. | ninguna por defecto | no progresa por sí sola |
| T.R. | resistencia correspondiente al tipo de efecto | si falla y el efecto se sufre, progresa la resistencia correspondiente |
| T.E. | competencia de la especialización implicada | si la tirada tiene éxito, progresa la especialización usada |
| T.P. | ninguna | no progresa por sí sola |

La competencia de escudo progresa aparte, mediante Técnicas y maniobras de escudo exitosas.

---

## Ejemplo

Un personaje intenta esquivar el golpe de una criatura pesada mientras lleva Ventaja en el Aprendizaje. Resuelve la T.D. con el dado menor. Si evita el ataque, la tirada puede generar progreso en Evasión. Si falla, pero la armadura de la zona resuelta absorbe parte del impacto, la misma situación puede generar progreso en el tipo de armadura correspondiente. La competencia que progresa depende del resultado de la tirada, no solo del tipo de acción.
