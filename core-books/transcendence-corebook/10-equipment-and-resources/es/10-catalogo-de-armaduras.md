---
title: "Catálogo de Armaduras y Escudos"
type: corebook
content_kind: reference
writing_mode: reference
language: es
chapter: 10
status: draft
canonical: false
tags: [armaduras, escudos, equipo, catálogo, combate, defensa, bloqueo]
related:
  - core-books/transcendence-corebook/10-equipment-and-resources/es/04-fabricacion-equipo.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/08-catalogo-de-materiales.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/05-heridas-y-dano.md
authority_refs:
  - Transcendence-design/data/system/combat-equipment-catalog.yaml
  - Transcendence-design/docs/system/combat-equipment-catalog.md
  - Transcendence-design/data/system/wounds-and-damage.yaml
---

# Catálogo de Armaduras y Escudos

La armadura en Transcendence no es un ítem único sino un conjunto de piezas intercambiables. Cada pieza pertenece a una de cinco zonas del cuerpo y puede ser de una categoría distinta — no es obligatorio llevar un juego completo de la misma clase. Un personaje puede combinar un peto pesado con brazales ligeros según la situación táctica.

---

## Piezas de Armadura

| Pieza | Zona que cubre |
| --- | --- |
| Casco | Cabeza |
| Peto | Torso |
| Brazales | Brazos |
| Pantalón | Piernas |
| Botas | Pies |

Una zona sin pieza de armadura no recibe Bloqueo de armadura si es golpeada.

---

## Categorías de Armadura

La categoría de una pieza determina su Bloqueo base (BC) y cómo afecta la Tirada de Defensa de esa zona.

| Categoría | BC | Competencia evasiva | Agilidad en T.D. |
| --- | :---: | --- | --- |
| Ligera | 2 | Completa | Completa |
| Intermedia | 4 | Completa | La mitad |
| Pesada | 6 | La mitad | No aplica |

La armadura pesada reduce la capacidad de esquivar, pero su mayor BC y los materiales densos que requiere compensan con absorción directa del impacto.

El Bloqueo total de una zona se calcula sumando BC + BM del material + nivel de competencia en ese tipo de armadura. La fórmula completa está en el capítulo _Heridas y Daño_.

---

## Bonificadores por Pieza

Cada pieza de armadura otorga un bonificador pasivo permanente que depende de la zona que cubre y de la categoría de la pieza. Todos los valores escalan con el **grado** de la pieza (1, 2 o 3).

| Pieza | Ligera | Intermedia | Pesada |
| --- | --- | --- | --- |
| **Casco** | +grado a Preparación | +grado a T.E. de Compostura | +grado a T.R. contra conmoción, ceguera y aturdimiento |
| **Peto** | +grado ×3 a Aguante | +grado ×2 a Aguante | +grado a Aguante |
| **Brazales** | +grado a T.A. en Técnicas Reactivas | +grado a T.A. en Técnicas Activas | +grado a T.I. en Técnicas Activas |
| **Pantalón** | +grado a T.E. de Agilidad | +grado a T.E. de Fuerza | +grado a T.E. de Tenacidad |
| **Botas** | +grado al movimiento | +grado a tiradas reactivas (Equilibrio, esquivar efectos de área) | +grado a T.R. contra desplazamiento forzado, derribo y desestabilización |

Estos bonificadores se aplican solo mientras la pieza está equipada. La zona sin pieza no recibe el bonificador correspondiente.

---

## Materiales por Categoría

El **Bono de Material (BM)** depende de la Durabilidad del material y del grado de la pieza.

> **BM = D base × grado ÷ 6** (redondeado hacia abajo)

Las tablas muestran el BM resultante para cada grado. Para el Bloqueo final de una pieza, suma BC + BM al nivel de competencia del portador.

---

### Ligera

| Material | Acc. | D base | BM G1 | BM G2 | BM G3 |
| --- | --- | :---: | :---: | :---: | :---: |
| Tela | General | 4 | 0 | 1 | 2 |
| Cuero | Limitada | 10 | 1 | 3 | 5 |
| Titanio | Singular | 32 | 5 | 10 | 16 |
| Tela de criatura (pelaje) | Variable | — | — | — | — |
| Cuero de criatura (pelaje) | Variable | — | — | — | — |

Las piezas de criatura usan la Durabilidad del pelaje de la especie fuente. El valor de referencia en el catálogo es D=4 para pelaje estándar — criaturas más robustas pueden tener D más alto. Consulta el stat block de la criatura para el valor exacto.

---

### Intermedia

| Material | Acc. | D base | BM G1 | BM G2 | BM G3 |
| --- | --- | :---: | :---: | :---: | :---: |
| Peltre | General | 8 | 1 | 2 | 4 |
| Cobre | General | 8 | 1 | 2 | 4 |
| Bronce | General | 12 | 2 | 4 | 6 |
| Hierro | General | 14 | 2 | 4 | 7 |
| Cuero escamado | Limitada | 14 | 2 | 4 | 7 |
| Obsidiana | Singular | 6 | 1 | 2 | 3 |
| Escamas de criatura | Variable | — | — | — | — |

La obsidiana tiene Durabilidad muy baja — su valor como material de armadura está en su filo excepcional (P=22), no en la absorción de impacto. En piezas de armadura, su BM es bajo pero sus propiedades de ruptura sobre quienes la impactan pueden justificar su uso situacional.

Las escamas usan la Durabilidad de la especie fuente. El valor de referencia en el catálogo es D=16 — criaturas con escamas especialmente duras pueden superar ese valor. Consulta el stat block de la criatura para el valor exacto.

---

### Pesada

| Material | Acc. | D base | BM G1 | BM G2 | BM G3 |
| --- | --- | :---: | :---: | :---: | :---: |
| Plomo | General | 6 | 1 | 2 | 3 |
| Oro | General | 6 | 1 | 2 | 3 |
| Plata | Limitada | 10 | 1 | 3 | 5 |
| Platino | Limitada | 12 | 2 | 4 | 6 |
| Acero | Limitada | 20 | 3 | 6 | 10 |
| Coraza de criatura | Variable | — | — | — | — |

El plomo y el oro tienen Durabilidad baja para ser metales pesados — su peso confiere el acceso a la categoría Pesada y sus propiedades de masa, pero el BM resultante es inferior al de acero o platino. El plomo es la opción de armadura pesada de menor costo por accesibilidad; el acero es el estándar práctico.

La coraza usa la Durabilidad del caparazón de la especie fuente. El valor de referencia en el catálogo es D=22 — criaturas con estructuras quitinosas o calcáreas excepcionales pueden superar ese valor. Consulta el stat block de la criatura para el valor exacto.

---

## Escudos

Los escudos son equipo de defensa activa, no piezas de armadura. No ocupan ninguna zona de armadura y se llevan en la mano. Aportan un bonificador a la Tirada de Defensa y los modelos más grandes otorgan Cobertura mientras están activos.

El bonificador y la penalización al movimiento dependen del **grado** del escudo (1, 2 o 3).

| Categoría | Cobertura | Bono a T.D. | Penalización a movimiento | Peso aprox. |
| --- | --- | :---: | :---: | --- |
| Escudo ligero | Ninguna | = grado | Ninguna | 2 kg |
| Escudo intermedio | Cobertura Ligera | = grado | = grado | 5 kg |
| Escudo pesado | Cobertura Intermedia | = grado + 1 | = grado × 2 | 10 kg |

Un escudo roto deja de aportar su bonificador y su Cobertura hasta ser reparado.
