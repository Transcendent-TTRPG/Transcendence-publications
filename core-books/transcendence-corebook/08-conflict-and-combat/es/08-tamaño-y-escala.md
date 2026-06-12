---
title: "Tamaño y Escala"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [size, scale, endurance, physical-modifiers, combat, creatures]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/02-desgaste-aguante-fatiga.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/07-cobertura-visibilidad-y-ocultacion.md
  - core-books/transcendence-corebook/11-ailments/es/02-alteraciones.md
  - core-books/transcendence-corebook/17-appendices/es/01-catalogo-de-especializaciones.md
authority_refs:
  - Transcendence-design/data/system/size-modifiers.yaml
---

# Tamaño y Escala

El tamaño de una criatura afecta directamente varios cálculos del sistema. Una criatura más grande tiene más Aguante, puede cargar más peso y tiene mayor rango visual. Una más pequeña puede maniobrar, trepar y pasar desapercibida con más facilidad, pero resiste peor las condiciones físicas adversas.

Las categorías de tamaño son:

| Tamaño | Criterio |
| --- | --- |
| Diminuto | La más pequeña. Insectos, animales de bolsillo, formas menores. |
| Pequeño | Por debajo del rango humanoide estándar. |
| Mediano | El rango humanoide estándar. Referencia del sistema. |
| Grande | Significativamente más grandes que un humanoide. |
| Enorme | Criaturas masivas. Ocupan varias casillas en tablero. |
| Gigantesco | La más grande. Bestias colosales, entidades. |

---

## Modificadores por tamaño

Todas las categorías reciben modificadores derivados de su posición en la escala. Los valores toman a Mediano como referencia `0` y escalan en pasos de `±2` por categoría.

La relación es **inversamente proporcional**: las criaturas pequeñas son más ágiles en maniobras corporales, pero más difíciles de sostener bajo condiciones de estabilidad física. Las criaturas grandes resisten mejor esas condiciones, pero son menos precisas en acciones que exigen control corporal fino.

| Tamaño | T.E. físicas propias | T.R. físicas |
| --- | ---: | ---: |
| Diminuto | `+4` | `−4` |
| Pequeño | `+2` | `−2` |
| Mediano | — | — |
| Grande | `−2` | `+2` |
| Enorme | `−4` | `+4` |
| Gigantesco | `−6` | `+6` |

---

### T.E. físicas propias

Las **T.E. físicas propias** son T.E. que representan el movimiento del propio cuerpo de la criatura como agente.

El modificador de tamaño aplica cuando la criatura realiza:

- **Acrobacias** — equilibrio dinámico, rotaciones, amortiguación de caídas
- **Equilibrio** — estabilidad bajo condiciones que amenazan la postura
- **Trepar** — ascenso o descenso de superficies verticales
- **Sigilo** — reducir la señal del propio cuerpo para pasar desapercibido

Una criatura Pequeña con Sigilo no es necesariamente más hábil — su firma física (visual, sonora, térmica) es simplemente más difícil de captar. Una criatura Grande carga con esa misma dificultad multiplicada al intentar moverse en silencio.

---

### T.R. físicas

Las **T.R. físicas** son T.R. contra alteraciones que actúan sobre la estabilidad corporal.

El modificador de tamaño aplica cuando la criatura resiste:

- **Derribado** — perder el contacto con el suelo o caer de forma no controlada
- **Desequilibrado** — perder temporalmente la estabilidad corporal
- **Atrapado** — quedar inmovilizado o restringido en movimiento

Una criatura de mayor tamaño tiene más masa, más base de contacto y más inercia. Es más difícil hacerla caer o atraparla. Una criatura pequeña puede ser volteada con menos esfuerzo, aunque sea igualmente ágil.

---

## Aguante por tamaño

El **Aguante** usa una base que depende del tamaño. Ver el capítulo **Desgaste, Aguante y Fatiga** para la fórmula completa.

```text
Aguante = base de tamaño + (Tenacidad × 2)
```

| Tamaño | Base de Aguante |
| --- | ---: |
| Pequeño | 2 |
| Mediano | 4 |
| Grande | 6 |

Esta base aplica a especies jugables. Los valores de Aguante para criaturas no jugables pueden diferir según la regla del narrador.

---

## Capacidad de Carga por tamaño

La Capacidad de Carga también escala con el tamaño mediante un multiplicador por categoría. Ver el capítulo **Desgaste, Aguante y Fatiga** para la fórmula y la tabla completa.

---

## Rango visual por tamaño

Una criatura más grande detecta detalles a mayor distancia; una más pequeña tiene un campo visual efectivo menor. Ver el capítulo **Cobertura, Visibilidad y Ocultación** para los valores por tamaño.

---

## Modificadores de especie

Algunos rasgos de especie alteran cómo aplican estos modificadores para cálculos específicos. Cuando un rasgo indica que una criatura se trata como un tamaño distinto al real, ese tratamiento aplica solo a los valores indicados. El tamaño real no cambia y los demás modificadores no se ven afectados.
