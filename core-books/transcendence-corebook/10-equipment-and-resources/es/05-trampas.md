---
title: "Trampas"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 10
status: draft
canonical: false
tags: [trampas, fabricación, diagramas, ingeniería, exploración]
related:
  - core-books/transcendence-corebook/10-equipment-and-resources/es/01-materiales.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/02-extraccion-y-conservacion.md
  - core-books/transcendence-corebook/11-ailments/es/03-aflicciones.md
authority_refs:
  - Transcendence-design/docs/system/materials-and-fabrication.md
  - Transcendence-design/data/system/materials-and-fabrication.yaml
---

# Trampas

Una trampa es un mecanismo, disposición o sistema preparado de antemano para activarse ante una condición específica — generalmente la presencia o el movimiento de un objetivo. A diferencia del equipo o los compuestos alquímicos, las trampas no se portan ni se usan activamente: se instalan y esperan.

La especialización que fabrica trampas es **Ingeniería**. La que las detecta o desactiva es también Ingeniería, aunque otras especializaciones pueden ser relevantes según el tipo.

---

## Tipos de trampa

Las trampas se clasifican por el principio que las hace funcionar.

| Tipo | Principio | Costo base adicional |
| --- | --- | --- |
| **Mecanismo** | Dispositivos físicos — resortes, cables, contrapesos, hojas, proyectiles | — |
| **Ilusorio** | Engaños perceptivos naturales — perspectiva, camuflaje, sombra, desalineación visual | +50 S |
| **Ambiental** | Manipulación del entorno — pozos ocultos, superficie inestable, acumulación de peso | +50 S |
| **Vivo** | Organismos vivos incorporados al mecanismo — esporas, insectos, parásitos, lianas | +100 S |
| **Umbral** | Materiales tauma-impregnados con propiedades extranatural fijas — sin control de Tauma | +250 S |

Las trampas ilusorias no requieren materiales de criatura — sus efectos de engaño son puramente físicos: perspectiva distorsionada, camuflaje de superficie, patrones de sombra que ocultan bordes o tensores.

Las trampas umbral son inusualmente difíciles y costosas. Producen efectos extranaturales porque los materiales umbral ya contienen una carga conocida y estable, pero quien las fabrica no controla Tauma — usa el comportamiento fijo del material como se usa cualquier otra herramienta con propiedades extremas. Solo están disponibles a rareza Rara o Excepcional.

---

## Diagramas

Un Diagrama es el documento que define la disposición, materiales y efecto de una trampa. Sin él no es posible fabricarla.

Los Diagramas los crea la especialización Ingeniería. Como los Diseños de equipo, un diagrama no caduca y puede usarse para fabricar múltiples copias de la misma trampa.

---

## Proceso de fabricación

Para fabricar una trampa se necesita:

1. **Un Diagrama** del tipo y rareza de la trampa.
2. **Los materiales** en las cantidades especificadas.
3. **La especialización Ingeniería** al rango suficiente para la rareza.

Cuando el personaje declara una sesión de fabricación:

- Realiza una tirada de **Ingeniería** al inicio. La dificultad la determina la rareza de la trampa.
- Si la tirada **falla**: el tiempo se consume sin producir avance y los materiales de esa sesión se pierden.
- Si la tirada **tiene éxito**: el personaje trabaja durante las horas requeridas y completa la trampa.

A diferencia del equipo, las trampas se fabrican en una sola sesión sin división en semanas — el tiempo listado es el total.

### Parámetros por rareza

| Rareza | Tiempo | Dificultad de fabricación | Detección | Desactivación | Costo de labor | Costo de materiales |
| --- | --- | --- | --- | --- | --- | --- |
| Común | 4 horas | Desafiante | Desafiante | Desafiante | 200 S | 216 S |
| Rara | 10 horas | Exigente | Exigente | Exigente | 500 S | 432 S |
| Excepcional | 24 horas | Extremo | Exigente | Exigente | 1.200 S | 648 S |

El costo total mínimo de cada trampa es la suma de labor + materiales + el costo adicional del tipo. El Diagrama es un costo único de adquisición aparte.

---

## Instalación

Una trampa fabricada debe instalarse en el terreno antes de ser funcional. La instalación es una **acción extendida** que requiere la especialización Ingeniería y toma tiempo proporcional a la rareza — el Narrador determina el tiempo exacto según la complejidad de la disposición.

Una trampa mal instalada puede activarse prematuramente, fallar al activarse, o ser visible sin necesidad de una tirada de detección.

---

## Detección y desactivación

### Detección

Un personaje que pase por una zona donde hay una trampa instalada puede detectarla con una tirada de **Percepción** o **Ingeniería** — la dificultad depende de la rareza (ver tabla de parámetros). La dificultad puede modificarse por condiciones del entorno.

Un personaje puede declarar que avanza con precaución para buscar activamente trampas. En ese caso se considera que realiza la tirada.

### Desactivación

Un personaje que detectó una trampa puede intentar desactivarla con **Ingeniería**. La dificultad depende de la rareza. Si falla, el Narrador determina si la trampa se activa, queda dañada, o simplemente resiste.

---

## Activación

Las trampas se activan ante una **condición de activación** definida en el Diagrama. La condición puede ser:

- cruzar un punto de presión o cable
- entrar en un área delimitada
- interactuar con un objeto trampeado
- una condición temporal (pasado cierto tiempo)

Cuando la trampa se activa, el efecto descrito en el Diagrama se aplica de inmediato sin acción del fabricante.

---

## Catálogo de diagramas

---

### Trampa de Cables

**Tipo:** Mecanismo · **Rareza:** Común

Un sistema de cables tensados a ras del suelo conectado a contrapesos. Al activarse, sujeta los pies del objetivo.

El objetivo que activa la trampa realiza una **T.R. de Alteraciones** — si falla, queda Inmovilizado.

**Disponibilidad:** General

---

### Trampa Afilada

**Tipo:** Mecanismo · **Rareza:** Común

Una serie de hojas o puntas metálicas ocultas bajo una superficie cede al pisar. El objetivo que activa la trampa recibe daño de la impacto — el Narrador determina el T.I. según el grado del material. El objetivo también realiza una **T.R. de Alteraciones** — si falla, sufre Lacerado.

**Disponibilidad:** Limitada

---

### Pozo Oculto

**Tipo:** Ambiental · **Rareza:** Común

Una abertura en el suelo disimulada con una cubierta de baja resistencia. El objetivo que la activa cae y recibe daño por caída.

**Disponibilidad:** General

---

### Trampa Resbaladiza

**Tipo:** Ambiental · **Rareza:** Rara

El área está cubierta de una sustancia resbaladiza preparada. Cualquier movimiento en el área requiere una tirada de **Atletismo** — si falla, el personaje cae.

**Disponibilidad:** Limitada

---

### Espejismo de Abismo

**Tipo:** Ilusorio · **Rareza:** Rara

Una trampa construida con materiales reflectantes y patrones de camuflaje que hace que el suelo sólido aparezca como un precipicio. La trampa permanece activa hasta que alguien la desactive. Un objetivo que la analice activamente puede intentar una tirada de **Percepción** — si tiene éxito, identifica la superficie real.

**Disponibilidad:** Limitada

---

### Trampa de Esporas Fúngicas

**Tipo:** Vivo · **Rareza:** Rara · **Reactivo:** Glándula de criatura

Un contenedor biológico con esporas fúngicas preparadas se rompe al activarse y libera el contenido en un área de 3 metros. Cada criatura en el área realiza una **T.R. de Infección** — si falla, contrae la Afliccción correspondiente al fungo utilizado.

**Disponibilidad:** Limitada
