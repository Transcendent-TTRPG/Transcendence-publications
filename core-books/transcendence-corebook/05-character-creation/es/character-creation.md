---
title: "Creación de Personaje"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 5
status: review
canonical: false
tags: [character-creation, species, background, specializations, synapsis, attributes, personality-traits, derived-attributes]
related:
  - core-books/transcendence-corebook/05-character-creation/en/character-creation.md
  - core-books/transcendence-corebook/03-core-rules/es/02-rolling-system-and-competencies.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/es/01-especializaciones.md
authority_refs:
  - Transcendence-design/docs/system/backgrounds.md
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/docs/system/characteristics.md
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/docs/adr/system-abilities-and-specializations.md
  - Transcendence-design/docs/adr/system-specialization-rank-restructure.md
  - Transcendence-design/data/system/backgrounds.yaml
  - Transcendence-design/data/system/attrition-fatigue.yaml
  - Transcendence-design/data/system/specializations.yaml
  - Transcendence-design/data/system/specializations-catalog.yaml
  - Transcendence-design/data/system/competencies.yaml
section_modes:
  - heading: "Ejemplo breve"
    writing_mode: example
  - heading: "Ejemplo"
    writing_mode: example
---

# Creación de Personaje

La creación de personaje define quién eres al inicio de la aventura, de dónde vienes y qué capacidades has desarrollado antes de entrar en juego.

Para crear un personaje, sigue estos pasos en orden:

1. Define el concepto.
2. Anota las características base.
3. Elige especie.
4. Elige trasfondo.
5. Escoge especializaciones iniciales.
6. Aplica Sinapsis.
7. Calcula atributos derivados.
8. Elige Rasgos de Personalidad.
9. Registra atributos adicionales de especie.

El orden importa. Algunos pasos modifican valores que se usan más adelante.

---

## 1. Define el concepto

Antes de elegir números, define una idea breve del personaje.

No necesitas escribir una historia completa. Basta con responder tres preguntas:

| Pregunta | Respuesta esperada |
| --- | --- |
| ¿Qué tipo de persona o criatura es? | Su identidad general |
| ¿Qué lo mueve? | Su motivación principal |
| ¿Cómo enfrenta el mundo? | Su actitud ante peligro, conflicto, otros personajes o incertidumbre |

Un concepto no debe ser solo una función mecánica.

No escribas solo:

- “un personaje fuerte”
- “alguien sigiloso”
- “un personaje inteligente”

Conviene formularlo como una persona concreta:

- una cazadora paciente que aprendió a sobrevivir sola
- un antiguo custodio que teme olvidar lo que juró proteger
- una noble insegura que intenta mantener autoridad en un mundo que ya no la respeta
- un combatiente criado para resistir dolor antes que para entenderlo

Usa este concepto como guía para elegir especie, trasfondo, especializaciones y Rasgos de Personalidad.

Al terminar este paso, anota una frase breve de concepto en tu hoja.

---

## 2. Anota las características base

Todas las características comienzan en `0`.

Este valor no significa que el personaje sea incompetente. Es una base neutra. La especie y la Sinapsis aumentarán estos valores durante la creación.

| Grupo | Característica | Qué representa |
| --- | --- | --- |
| Física | Fuerza | Potencia física, empuje, carga, golpes y esfuerzo bruto |
| Física | Agilidad | Coordinación, movilidad, equilibrio y reacción corporal |
| Física | Tenacidad | Resistencia física, tolerancia al dolor, fatiga y exigencia prolongada |
| Mental | Intelecto | Razonamiento, memoria, estudio y comprensión formal |
| Mental | Astucia | Improvisación, engaño, creatividad práctica y lectura de oportunidades |
| Mental | Sabiduría | Percepción, intuición, criterio y experiencia aplicada |
| Social | Compostura | Autocontrol, estabilidad emocional y calma bajo presión |
| Social | Aura | Impresión natural e involuntaria que el personaje proyecta |
| Social | Presencia | Proyección activa, autoridad, influencia e impacto social |

Al terminar este paso, tu hoja debe tener todas las características en `0`.

---

## 3. Elige especie

La especie define la base biológica y cultural del personaje.

Al elegir especie, registra todo lo que indique su perfil.

| Elemento | Qué debes anotar |
| --- | --- |
| Longevidad | Expectativa de vida habitual |
| Tamaño | Categoría de tamaño |
| Estatura y peso | Rango físico de referencia |
| Idiomas | Lenguas conocidas al inicio |
| Velocidad | Distancia recorrida con una acción de movimiento |
| Bonificaciones de características | Aumentos iniciales otorgados por especie |
| Otros valores iniciales equivalentes | Competencias, sentidos, rasgos innatos u otros valores especiales |
| Herencia | Vulnerabilidad, limitación o marca ancestral |
| Legado | Ventajas innatas o adaptaciones compartidas |
| Ataques corporales o armas naturales | Garras, colmillos, cuernos, cola, pinzas, aguijones u otras formas naturales de combate |
| Variante | Adaptación interna de la especie, si existe |

### Aplica bonificaciones de especie

Después de elegir especie, aumenta las características indicadas por su perfil.

```text
Característica actual = 0 + bonificación de especie
```

La descripción completa de cada especie aparece en el capítulo **Especies**.

Al terminar este paso, tu hoja debe tener:

- especie elegida
- atributos de especie anotados
- bonificaciones de características aplicadas

---

## 4. Elige trasfondo

El trasfondo representa la vida del personaje antes de la aventura.

Cada trasfondo otorga dos cosas:

| Beneficio | Función |
| --- | --- |
| Afinidad mayor | Reduce el progreso necesario en una categoría de especializaciones |
| Especializaciones iniciales | Define tres prácticas que el personaje ya desarrolló antes de empezar |

Una especialización con afinidad mayor necesita `5` puntos de progreso para subir de nivel.

Las demás especializaciones necesitan `10` puntos de progreso.

---

## Trasfondos disponibles

### Artista Marcial

El Artista Marcial ha dedicado su vida al perfeccionamiento del cuerpo, el combate o la resistencia física.

| Rasgo | Valor |
| --- | --- |
| Afinidad mayor | Física |
| Especializaciones iniciales | 2 Físicas + 1 de Mental, Social o Conocimiento |
| Regla adicional | Puede sustituir cualquier cantidad de competencias iniciales en armas naturales de su especie por armas fabricadas. |

---

### Artesano

El Artesano transforma materia, herramientas y recursos en objetos útiles, bellos o peligrosos.

| Rasgo | Valor |
| --- | --- |
| Afinidad mayor | Artes y Oficios |
| Especializaciones iniciales | 2 de Artes y Oficios + 1 de cualquier categoría |

---

### Errante

El Errante fue formado por el camino, la adaptación, la observación y la supervivencia lejos de un lugar estable.

| Rasgo | Valor |
| --- | --- |
| Afinidad mayor | Mental |
| Especializaciones iniciales | 2 Mentales + 1 de Física, Social o Conocimiento |

---

### Custodio

El Custodio proviene de tradiciones, instituciones o deberes ligados a proteger conocimiento, memoria o reliquias.

| Rasgo | Valor |
| --- | --- |
| Afinidad mayor | Conocimiento |
| Especializaciones iniciales | 2 de Conocimiento + 1 de Física, Mental o Social |

---

### Noble

El Noble fue criado entre jerarquía, educación, influencia, deber o vínculos sociales.

| Rasgo | Valor |
| --- | --- |
| Afinidad mayor | Social |
| Especializaciones iniciales | 1 Social + 2 de cualquier otra categoría |

---

Al terminar este paso, anota:

- tu trasfondo
- tu afinidad mayor
- las categorías permitidas para tus tres especializaciones iniciales

---

## 5. Escoge especializaciones iniciales

Cada personaje comienza con tres especializaciones otorgadas por su trasfondo.

Estas especializaciones deben cumplir las restricciones del trasfondo elegido.

Cada especialización inicial:

- comienza en nivel `1`
- comienza en rango `Novato`
- activa Sinapsis
- no puede repetirse durante la creación

```text
Especialización inicial = nivel 1 / rango Novato
```

Todo personaje recibe una especialización universal inicial de Tenacidad.

Elige una:

- **Marcha**
- **Aclimatación**
- **Tolerancia**

Esta especialización también comienza en nivel `1`, rango `Novato`, y activa Sinapsis.

No puedes escoger la misma especialización dos veces. Si una especialización ya fue elegida por trasfondo, no puede repetirse como elección universal.

Al terminar este paso, tu personaje debe tener cuatro especializaciones iniciales:

| Fuente | Cantidad |
| --- | --- |
| Trasfondo | 3 especializaciones |
| Universal de Tenacidad | 1 especialización |
| Total | 4 especializaciones iniciales |

La lista completa de especializaciones aparece en el **Catálogo de Especializaciones**.

---

## 6. Aplica Sinapsis

La Sinapsis representa cómo la práctica modifica las características del personaje.

Cada especialización está asociada a una característica. Cuando una especialización alcanza un nuevo rango, aumenta esa característica en `+1`.

Durante la creación, todas tus especializaciones iniciales comienzan en rango `Novato`. Por eso cada una otorga `+1` a su característica asociada.

```text
Sinapsis por especialización inicial = +1 a la característica asociada
```

Esto incluye:

- las tres especializaciones del trasfondo
- la especialización universal de Tenacidad

### Cómo aplicar Sinapsis

Para cada especialización inicial:

1. Revisa su característica asociada.
2. Suma `+1` a esa característica.
3. Repite el proceso con las cuatro especializaciones iniciales.

Si varias especializaciones están asociadas a la misma característica, sus aumentos se acumulan.

```text
Característica final = bonificación de especie + suma de Sinapsis aplicadas
```

Al terminar este paso, todas tus características finales deben estar calculadas.

---

## 7. Calcula atributos derivados

Los atributos derivados se calculan después de aplicar especie y Sinapsis.

Durante la creación, calcula estos atributos derivados:

- **Preparación**
- **Resiliencia**
- **Aguante**
- **Cordura**

Estos valores usan las características finales del personaje.

---

### Preparación

La Preparación mide qué tan bien el personaje anticipa, reacciona y actúa bajo presión.

```text
Preparación = (Agilidad + Astucia + Compostura) / 3
```

Valor mínimo: `1`.

---

### Resiliencia

La Resiliencia mide la capacidad del personaje para resistir y recuperarse de alteraciones adversas.

```text
Resiliencia = (Tenacidad + Sabiduría + Compostura) / 3
```

Valor mínimo: `1`.

---

### Aguante

El Aguante mide cuánta carga acumulada puede sostener el personaje antes de entrar en Fatiga.

```text
Aguante = base de tamaño + (Tenacidad × 2)
```

La base de tamaño depende de la especie: `2` para Pequeño, `4` para Mediano, `6` para Grande. La mayoría de las especies jugables son Mediano.

La especialización universal inicial de Tenacidad ya está incluida indirectamente, porque aplica Sinapsis y aumenta Tenacidad durante la creación.

---

### Cordura

La Cordura mide la estabilidad mental y anímica del personaje frente a presión extrema, horror, corrupción o efectos que ataquen su equilibrio interno.

```text
Cordura = 3 + (Compostura × 2)
```

La interacción completa de Cordura con horror cósmico, corrupción y equipo se desarrolla en sus secciones correspondientes. Durante la creación, anota el valor base para que la hoja quede completa.

---

### Redondeo

Si Preparación o Resiliencia producen fracciones o decimales, redondea hacia arriba.

```text
1.1 → 2
1.6 → 2
2.0 → 2
```

Aguante y Cordura no requieren redondeo con sus fórmulas actuales.

Si más adelante una característica permanente aumenta, recalcula cualquier atributo derivado que dependa de ella.

---

## Ejemplo breve

Después de aplicar especie y Sinapsis, un personaje tiene:

| Característica | Valor |
| --- | --- |
| Agilidad | 2 |
| Astucia | 1 |
| Compostura | 1 |
| Tenacidad | 2 |
| Sabiduría | 1 |

Calcula Preparación:

```text
Preparación = (2 + 1 + 1) / 3
Preparación = 4 / 3
Preparación = 2
```

Calcula Resiliencia:

```text
Resiliencia = (2 + 1 + 1) / 3
Resiliencia = 4 / 3
Resiliencia = 2
```

Calcula Aguante (especie Mediana):

```text
Aguante = 4 + (2 × 2)
Aguante = 8
```

Calcula Cordura:

```text
Cordura = 3 + (1 × 2)
Cordura = 5
```

Preparación y Resiliencia se redondean hacia arriba.

---

## 8. Elige Rasgos de Personalidad

Los Rasgos de Personalidad describen cómo el personaje piensa, siente y responde ante el mundo.

También pueden usarse en juego. Si un rasgo influye de forma clara en una escena, el jugador puede proponer una **Tirada de Rasgo de Personalidad** en lugar de una Tirada de Característica o de Especialización. El Narrador decide si la justificación es válida.

Puedes elegir rasgos de dos formas.

---

### Opción estructurada

Elige un rasgo para cada factor:

| Factor | Qué describe |
| --- | --- |
| Apertura a la experiencia | Relación con lo nuevo, incierto, abstracto o imaginativo |
| Conciencia | Disciplina, orden, constancia y responsabilidad |
| Extraversión | Forma de ocupar el espacio social |
| Amabilidad | Empatía, cooperación, confianza o reserva frente a otros |
| Neuroticismo | Estabilidad emocional y respuesta ante ansiedad, presión o conflicto interno |

Cada rasgo debe tener intensidad:

- alta
- baja

La intensidad no significa “mejor” o “peor”. Define cómo se expresa ese factor en el personaje.

---

### Opción libre

Elige cinco rasgos sin asignarlos a factores.

Pueden ser palabras o frases cortas:

- inquieto
- analítico
- leal
- impulsivo
- sombrío
- desconfiado
- protector
- curioso

Esta opción funciona igual en juego. Cualquier rasgo puede invocarse si el jugador explica cómo afecta la escena y el Narrador acepta la justificación.

---

Al terminar este paso, tu personaje debe tener:

- cinco Rasgos de Personalidad, o
- un rasgo por cada factor con intensidad alta o baja

La lista completa de rasgos sugeridos aparece en la sección **Rasgos de Personalidad**.

---

## 9. Registra atributos adicionales de especie

Antes de terminar, revisa el perfil completo de tu especie y anota cualquier elemento que aún no esté en la hoja.

Esto puede incluir:

- tamaño
- estatura y peso
- idiomas
- velocidad
- herencia
- legado
- otros valores iniciales equivalentes
- ataques corporales o armas naturales
- variante
- capacidades especiales adicionales
- restricciones de uso
- bonificadores situacionales

No necesitas copiar toda la información cultural de la especie. Sí debes registrar todos los efectos mecánicos y rasgos funcionales que puedan usarse durante el juego.

---

## Cierre de la creación de personaje

Al terminar la creación, tu personaje debe tener:

| Elemento | Estado |
| --- | --- |
| Concepto | Definido |
| Especie | Elegida |
| Trasfondo | Elegido |
| Afinidad mayor | Anotada |
| Características | Calculadas con especie y Sinapsis |
| Especializaciones iniciales | 3 por trasfondo + 1 universal de Tenacidad |
| Preparación | Calculada |
| Resiliencia | Calculada |
| Aguante | Calculado |
| Cordura | Calculada |
| Rasgos de Personalidad | Elegidos |
| Atributos adicionales de especie | Registrados |

Con esto, el personaje está listo para entrar en juego.

---

## Ejemplo

Una jugadora crea una exploradora de una especie con bonificador a Agilidad.

Primero anota todas las características en `0`. Luego elige especie y aplica el bonificador a Agilidad junto con las demás características indicadas por la especie.

Después elige un trasfondo que le concede tres especializaciones iniciales. También escoge **Aclimatación** como especialización universal de Tenacidad.

Ahora tiene cuatro especializaciones iniciales. Cada una está en nivel `1`, rango `Novato`, así que cada una activa Sinapsis y aumenta en `+1` su característica asociada.

Solo después de aplicar especie y Sinapsis calcula Preparación, Resiliencia, Aguante y Cordura.

El orden importa porque cada paso modifica el siguiente.
