---
title: "Fabricación de Equipo"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 10
status: draft
canonical: false
tags: [fabricación, equipo, armas, armaduras, escudos, joyería, herrería, sastrería, joyería]
related:
  - core-books/transcendence-corebook/10-equipment-and-resources/es/01-materiales.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/02-extraccion-y-conservacion.md
authority_refs:
  - Transcendence-design/docs/system/materials-and-fabrication.md
  - Transcendence-design/data/system/materials-and-fabrication.yaml
---

# Fabricación de Equipo

La fabricación de equipo produce armas, armaduras, escudos y joyas a través de un proceso controlado de trabajo manual. No existe una tirada genérica de "hacer un objeto" — cada pieza de equipo pertenece a la especialización que la ejecuta, requiere un documento de diseño, y consume horas de trabajo real.

---

## Proceso de fabricación

Para fabricar cualquier pieza de equipo se necesita:

1. **Un Diseño** — el documento de instrucciones del objeto. Sin él, no es posible comenzar.
2. **Los materiales** en las cantidades y tipos requeridos para el objeto.
3. **La especialización relevante** al rango suficiente para el material.

El personaje declara cuántas horas va a trabajar en esa sesión. Por cada hora declarada, realiza una tirada de la **especialización relevante**. La dificultad la determina la accesibilidad del material principal del objeto.

- Si la tirada **tiene éxito**: esa hora cuenta como progreso real hacia el total requerido.
- Si la tirada **falla**: esa hora se consume sin avance. Los materiales no se ven afectados.

El trabajo continúa en sesiones hasta completar el total de horas de progreso requeridas para el material.

### Dificultad por accesibilidad del material

| Accesibilidad del material | Dificultad de fabricación |
| --- | --- |
| General | Desafiante |
| Limitada | Exigente |
| Singular | Extremo |

---

## Diseños

Un Diseño es el documento que define la apariencia, configuración y atributos de un objeto de equipo. Sin diseño no hay producción posible.

Los Diseños los crean las mismas especializaciones que fabrican el objeto: Herrería, Sastrería o Joyería. Un diseño no caduca y puede usarse para fabricar múltiples copias del mismo objeto.

### Tipos de diseño y costo de adquisición

| Tipo de objeto | Tipo de diseño | Costo de adquisición | Disponibilidad |
| --- | --- | --- | --- |
| Armas arrojadizas y a distancia | Diseño de arma | 50 S | General |
| Armas con mango (astas, lanzas, hachas, mazas, hojas) | Diseño de arma | 80 S | General |
| Armas flexibles | Diseño de arma | 100 S | Limitada |
| Armadura ligera | Diseño de armadura | 50 S | General |
| Armadura intermedia | Diseño de armadura | 80 S | General |
| Armadura pesada | Diseño de armadura | 100 S | Limitada |
| Escudo ligero | Diseño de escudo | 50 S | General |
| Escudo intermedio | Diseño de escudo | 80 S | General |
| Escudo pesado | Diseño de escudo | 100 S | Limitada |
| Colgante | Diseño de joya | 50 S | Limitada |
| Amuleto | Diseño de joya | 80 S | Limitada |
| Insignia | Diseño de joya | 100 S | Limitada |

---

## Especialización por tipo de objeto

La especialización que fabrica el objeto depende de su material principal.

| Tipo de objeto | Especialización |
| --- | --- |
| Armas de metal (hojas, mazas, hachas de metal) | Herrería |
| Armas con mango compuesto (astas, lanzas, hachas, mazas con mango) | Herrería |
| Armas de madera pura (arcos, cerbatanas) | Sastrería |
| Armas de fibra (hondas, látigos) | Sastrería |
| Armas flexibles de metal (cadenas, nekode) | Herrería |
| Armadura ligera (cuero, tela) | Sastrería |
| Armadura intermedia y pesada (metal) | Herrería |
| Escudo ligero (madera, cuero) | Sastrería |
| Escudo intermedio y pesado (metal) | Herrería |
| Joyas (colgantes, amuletos, insignias) | Joyería |

---

## Materiales requeridos por tipo de arma

Cada arma tiene componentes con requisitos de material y peso específicos. Un componente clasificado como **metal** puede ser cualquier material metálico válido. Un componente clasificado como **madera** puede ser cualquier madera válida. Un componente clasificado como **fibra** puede ser cualquier fibra o cuero válido.

| Tipo de arma | Componente | Material | Kg requeridos |
| --- | --- | --- | --- |
| **Arma de asta** | Asta | Madera | 5 |
| | Hoja | Metal | 2 |
| **Lanza (dos manos)** | Asta | Madera | 4 |
| | Punta | Metal | 2 |
| **Lanza (una mano)** | Asta | Madera | 2 |
| | Punta | Metal | 1 |
| **Hacha (dos manos)** | Mango | Madera | 3 |
| | Hoja | Metal | 2 |
| **Hacha (una mano)** | Mango | Madera | 2 |
| | Hoja | Metal | 1 |
| **Maza (dos manos)** | Mango | Madera o metal | 3 |
| | Cabeza | Metal | 3 |
| **Maza (una mano)** | Mango | Madera o metal | 1 |
| | Cabeza | Metal | 1 |
| **Hoja larga (dos manos)** | — | Metal | 3 |
| **Hoja larga (una mano)** | — | Metal | 2 |
| **Hoja corta** | — | Metal | 1 |
| **Daga** | — | Metal | 1 |
| **Kunai / Shuriken (x3)** | — | Metal | 1 |
| **Pilum / Francisca** | Mango | Madera | 1 |
| | Hoja | Metal | 2 |
| **Arco / Cerbatana** | Cuerpo | Madera | 1 |
| **Honda (balearic)** | Cuerpo | Fibra | 1 |
| **Kusarigama / Kusari Fundo** | — | Metal | 2 |
| **Nekode (x2)** | — | Metal | 1 |
| **Látigo (scourge)** | — | Fibra | 3 |

---

## Materiales para armaduras

Las armaduras se fabrican pieza a pieza. El total de material depende de cuántas piezas se producen y a qué clase pertenecen.

### Kg de material por pieza y clase

| Pieza | Ligera | Intermedia | Pesada |
| --- | --- | --- | --- |
| Casco | 1 kg | 2 kg | 3 kg |
| Peto | 3 kg | 6 kg | 9 kg |
| Pantalón | 2 kg | 4 kg | 6 kg |
| Brazales | 2 kg | 3 kg | 4 kg |
| Botas | 1 kg | 2 kg | 3 kg |
| **Total (juego completo)** | **9 kg** | **17 kg** | **25 kg** |

### Materiales válidos por clase de armadura

| Clase | Materiales válidos |
| --- | --- |
| **Ligera** | Cuero, tela, cuero de criatura, titanio |
| **Intermedia** | Hierro, cobre, bronce, peltre, obsidiana, cuero escamado |
| **Pesada** | Acero, plomo, plata, oro, platino |

Los materiales tauma-impregnados de cualquier categoría pueden ser válidos según su equivalente estructural — el Narrador evalúa caso a caso.

---

## Materiales para escudos

| Clase | Kg de material | Materiales válidos |
| --- | --- | --- |
| **Ligero** | 3 kg | Cuero, roble, pino, caoba, arce, titanio |
| **Intermedio** | 7 kg | Hierro, cobre, bronce, peltre, cuero escamado |
| **Pesado** | 11 kg | Acero, plomo, plata, oro, platino |

---

## Costo de fabricación

El costo total de un objeto fabricado tiene dos componentes: el costo de materiales (variable) y el costo de mano de obra (calculado por fórmula). El costo del Diseño es una inversión única — no se paga de nuevo al fabricar más copias con el mismo diseño.

### Mano de obra

El costo de mano de obra depende de la accesibilidad del material, el grado y el peso total del objeto.

| Accesibilidad del material | Mano de obra por kg |
| --- | --- |
| General | 15 S × Grado × kg |
| Limitada | 45 S × Grado × kg |
| Singular | 150 S × Grado × kg |

**Ejemplo:** Una hoja larga (una mano) de acero (material de accesibilidad limitada, grado 2) pesa 2 kg. Mano de obra = 45 × 2 × 2 = **180 S**. Material: 30 S × 2 × 2 kg = 120 S. Total: **300 S**. Ver el _Catálogo de Materiales_ para precios de materiales.

Para objetos con componentes de materiales distintos (asta de madera + punta de metal), se calcula la mano de obra por separado para cada componente si difieren en accesibilidad o grado.

---

## Tiempo de trabajo

El tiempo de fabricación lo fija la accesibilidad del material principal del objeto.

| Accesibilidad del material | Tiempo total | Desglose |
| --- | --- | --- |
| General | 1 semana (30 horas) | 5 días × 6 horas/día |
| Limitada | 2 semanas (60 horas) | 10 días × 6 horas/día |
| Singular | 3 semanas (90 horas) | 15 días × 6 horas/día |

Las sesiones de trabajo se pueden distribuir libremente en el tiempo. En cada sesión, el personaje declara cuántas horas trabaja y realiza una tirada de especialización por hora.
