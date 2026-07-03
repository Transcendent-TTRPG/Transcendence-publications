---
title: "Alquimia"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 10
status: draft
canonical: false
tags: [alquimia, fórmulas, elixires, venenos, fabricación, plantas]
related:
  - core-books/transcendence-corebook/10-equipment-and-resources/es/01-materiales.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/02-extraccion-y-conservacion.md
  - core-books/transcendence-corebook/11-ailments/es/03-aflicciones.md
authority_refs:
  - Transcendence-design/docs/system/materials-and-fabrication.md
  - Transcendence-design/data/system/materials-and-fabrication.yaml
---

# Alquimia

En Transcendence, la alquimia no es magia embotellada; es farmacología de supervivencia y toxinas armadas. Extraes fluidos, neurotoxinas y glándulas de los cadáveres y los obligas a reaccionar, inyectando los peores mecanismos del mundo salvaje en el torrente sanguíneo de tu presa... o en el tuyo propio.

---

## Preparación e índices alquímicos

La fabricación tiene dos etapas con requisitos distintos. La primera — moler glándulas, aislar toxinas y estabilizar sangre negra antes de que se pudra en tu mochila — se llama preparación de **índices alquímicos** y puede hacerse en el fango del campo con un Kit Alquímico. La segunda — sintetizar el elixir o veneno terminado — siempre necesita alambique u horno en instalación fija.

Un personaje puede preparar sus índices durante la expedición. El producto se completa al regresar.

---

## Proceso de fabricación alquímica

Para fabricar un compuesto alquímico se necesita:

1. **Una Fórmula** — el documento de instrucciones del compuesto. Sin ella, no es posible comenzar.
2. **Los reactivos** en los tipos y cantidades indicados por la fórmula.
3. **La especialización Alquimia** al rango suficiente para la rareza de la fórmula.

El personaje declara cuántas horas va a trabajar en esa sesión. Por cada hora declarada, realiza una tirada de **Alquimia**. La dificultad la determina el tipo de reactivo principal de la fórmula.

- Éxito: esa hora suma progreso.
- Fallo: la hora se pierde, los reactivos quedan intactos.

El proceso se extiende en sesiones hasta completar el total de horas requeridas. Al completar ese total, el personaje produce el compuesto y tira las dosis.

### Dificultad por tipo de reactivo

| Reactivo principal | Accesibilidad | Dificultad de fabricación |
| --- | --- | --- |
| Fluidos | General | Desafiante |
| Glándulas | Limitada | Exigente |
| Órganos | Limitada | Exigente |
| Sistema nervioso | Singular | Extremo |

---

## Fórmulas

Una Fórmula es el documento que define reactivos, procedimiento y efecto de un compuesto. Sin fórmula no hay producción posible.

Las fórmulas pertenecen exclusivamente a la especialización Alquimia. A diferencia de los Diseños de equipo, las fórmulas se consumen con el uso: cada vez que se produce el compuesto, el personaje puede trabajar de la misma fórmula sin restricción adicional mientras la posea.

Las fórmulas tienen tres niveles de rareza que determinan el tiempo de producción y las dosis obtenidas.

### Rareza y parámetros de producción

| Rareza | Horas de trabajo | Dosis obtenidas | Dificultad base |
| --- | --- | --- | --- |
| Común | 12 horas | 1d4 | Desafiante |
| Rara | 24 horas | 1d3 | Exigente |
| Excepcional | 36 horas | 1d2 | Extremo |

El rendimiento de cada lote varía — los reactivos orgánicos y las condiciones del entorno nunca son exactamente los mismos.

---

## Vías de administración

Cada compuesto tiene una vía de administración que determina cómo entra al organismo.

| Vía | Descripción |
| --- | --- |
| **Ingestión** | Se consume por vía oral. Requiere que el objetivo trague voluntariamente o sea forzado a hacerlo. |
| **Inhalación** | Se inhala como gas, polvo o vapor. Puede afectar a múltiples criaturas en un área. |
| **Contacto** | Basta con que entre en contacto con piel o mucosas. Puede aplicarse a un objeto o superficie. |
| **Inoculación** | Debe introducirse directamente al flujo sanguíneo — mediante una hoja, una aguja o una garra recubierta. |

---

## Reactivos

Los compuestos alquímicos requieren dos categorías de insumo: un **reactivo de criatura** y un número de unidades de **plantas o reactivos botánicos**.

| Reactivo de criatura | Tipo | Accesibilidad |
| --- | --- | --- |
| Fluidos | Parte sensible de criatura | General |
| Glándulas | Parte sensible de criatura | Limitada |
| Órganos | Parte sensible de criatura | Limitada |
| Sistema nervioso | Parte sensible de criatura | Singular |

Cada fórmula especifica cuántas unidades del reactivo y cuántas plantas o reactivos vegetales requiere.

---

## Catálogo de fórmulas

A continuación se presentan fórmulas representativas. Las cantidades de reactivos aparecen en la entrada de cada fórmula; la rareza de la fórmula determina el tiempo de fabricación y el número de dosis del lote.

---

### Elixir Curativo

**Rareza:** Común · **Vía:** Ingestión · **Reactivo:** Glándula (1) · **Plantas:** 1

Fuerza al metabolismo a estabilizar tejido rasgado y cerrar hemorragias por pura sobremarcha biológica. Al consumirlo, el personaje reduce 2 puntos de Desgaste. No tiene efecto mientras el personaje esté Inconsciente o en Agonía.

**Disponibilidad:** General

---

### Elixir de Aguante

**Rareza:** Común · **Vía:** Contacto · **Reactivo:** Órgano (1) · **Plantas:** 2 · **Duración:** 3 horas

Inyecta una densa capa de estimulantes bioquímicos para adormecer el dolor y estabilizar la fatiga estructural. Mientras dura el efecto, el personaje incrementa su Aguante en 1. Los beneficios de múltiples dosis no se acumulan — aplica el valor más alto.

**Disponibilidad:** General

---

### Elixir de Agudeza Sensorial

**Rareza:** Común · **Vía:** Inhalación · **Reactivo:** Fluido (1) · **Plantas:** 3 · **Duración:** 2 horas

Agudiza la percepción sensorial de forma temporal. Mientras dura el efecto, el personaje obtiene +1 a las tiradas de Percepción. Los beneficios de múltiples dosis no se acumulan.

**Disponibilidad:** General

---

### Veneno Paralizante

**Rareza:** Raro · **Vía:** Inoculación · **Reactivo:** Fluido (1) · **Plantas:** 3

Al entrar en el flujo sanguíneo, el compuesto compromete el control neuromuscular. El objetivo realiza una T.R. de Veneno — si falla, sufre Ralentizado. Si falla por 3 rangos o más, queda Inmovilizado.

**Disponibilidad:** Limitada

---

### Veneno de Confusión

**Rareza:** Común · **Vía:** Inoculación · **Reactivo:** Glándula (1) · **Plantas:** 2

Interfiere con los procesos de orientación y toma de decisiones del objetivo. El objetivo realiza una T.R. de Veneno — si falla, sufre Desorientado.

**Disponibilidad:** Limitada

---

### Veneno de Letargo

**Rareza:** Raro · **Vía:** Ingestión · **Reactivo:** Fluido (1) · **Plantas:** 2

Suprime la reactividad muscular y la velocidad de respuesta. El objetivo realiza una T.R. de Veneno — si falla, sufre −1 a todas las T.A. y no puede realizar reacciones hasta que el efecto cese.

**Disponibilidad:** Limitada

---

### Veneno de Inercia

**Rareza:** Excepcional · **Vía:** Inoculación · **Reactivo:** Sistema nervioso (1) · **Plantas:** 2

Un colapso neurológico total. Ataca directamente el puente espinal de la bestia, ahogando sus señales nerviosas. El objetivo realiza una T.R. de Veneno — si falla, queda Inmovilizado. Mientras persiste el efecto, no puede tomar ninguna acción voluntaria. La T.R. puede repetirse al inicio de cada turno del objetivo.

**Disponibilidad:** Singular
