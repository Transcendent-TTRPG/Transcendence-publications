---
title: "Catálogo de Materiales"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 10
status: draft
canonical: false
tags: [materiales, precios, catálogo, fabricación, economía, recursos, durabilidad, potencia]
related:
  - core-books/transcendence-corebook/10-equipment-and-resources/es/01-materiales.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/03-economia-y-shekels.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/04-fabricacion-equipo.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/05-alquimia.md
authority_refs:
  - Transcendence-design/docs/system/materials-and-fabrication.md
  - Transcendence-design/data/system/materials-and-fabrication.yaml
---

# Catálogo de Materiales

Los valores corresponden a **Grado 1**. Para Grado 2, multiplica por 2; para Grado 3, por 3.

Los materiales de Accesibilidad **Limitada** o **Singular** pueden no estar disponibles en todos los asentamientos — su presencia depende de las rutas comerciales y la región.

---

## Cómo leer el catálogo

| Campo | Significado |
| --- | --- |
| **D base** | Durabilidad del material en Grado 1. D real = D base × grado |
| **P base** | Potencia base del material en Grado 1. P real = P base × grado |
| **S/kg** | Precio por kilogramo, Grado 1. Precio real = precio × grado |
| **S/u** | Precio por unidad (partes sensibles) |
| **S/L** | Precio por litro (fluidos) |

La **Durabilidad** refleja qué tan resistente es la estructura del material a ser rota bajo impacto. La **Potencia** refleja con qué efectividad el material transmite o genera fuerza estructural sobre otro objeto — capacidad de corte, masa, densidad de impacto. Estos valores se usan en el sistema de Ruptura durante los Impactos Críticos.

---

## Metales

| Material | Acc. | S/kg | D base | P base | Notas |
| --- | --- | ---: | ---: | ---: | --- |
| Estaño | General | 20 | 5 | 5 | Muy blando; componente de aleaciones |
| Plomo | General | 15 | 6 | 14 | Blando pero extremadamente denso — golpea duro, no aguanta filo |
| Oro | General | 100 | 6 | 10 | Muy blando y denso; se deforma al impacto |
| Cobre | General | 10 | 8 | 8 | Maleable; ni gran corte ni gran resistencia |
| Peltre | General | 12 | 8 | 7 | Aleación blanda de estaño; funcional, sin excelencia |
| Bronce | General | 15 | 12 | 11 | Más duro que cobre; histórica arma de combate |
| Hierro | General | 10 | 14 | 12 | Metal estructural base; equilibrio correcto |
| Plata | Limitada | 40 | 10 | 9 | Preciosa pero blanda; sirve, no lidera |
| Platino | Limitada | 120 | 12 | 14 | Denso; más duro que oro pero aún relativamente suave |
| Acero | Limitada | 30 | 20 | 18 | Refinado del hierro; mejor estructura y filo |
| Cromo | Limitada | 60 | 22 | 12 | Durísimo superficialmente; no transmite bien la fuerza solo |
| Titanio | Singular | 200 | 32 | 18 | Resistencia excepcional a la fractura; ligero, sin filo natural |

---

## Rocas y minerales

| Material | Acc. | S/kg | D base | P base | Notas |
| --- | --- | ---: | ---: | ---: | --- |
| Piedra | General | 5 | 10 | 10 | Masa bruta; decente en ambos por volumen puro |
| Roca | General | 5 | 10 | 10 | Bloques sin trabajar; mismo perfil que piedra |
| Vidrio | General | 8 | 3 | 8 | Extremadamente frágil; corta bien hasta que se rompe |
| Obsidiana | Singular | 40 | 6 | 22 | El mayor filo conocido; se astilla con cualquier torsión |

La obsidiana no es rara en zonas volcánicas, pero su fragilidad extrema y la precisión que exige su trabajo la sitúan en Accesibilidad Singular. Corta casi cualquier cosa; también se destruye rápido.

---

## Maderas

| Material | Acc. | S/kg | D base | P base | Notas |
| --- | --- | ---: | ---: | ---: | --- |
| Pino | General | 5 | 7 | 4 | Blanda y ligera; mango funcional básico |
| Caoba | General | 15 | 9 | 6 | Resistente con grano fino |
| Arce | General | 12 | 10 | 6 | Dura y densa; buena para mangos de arma |
| Roble | General | 10 | 12 | 7 | Mejor madera común para estructuras y escudos |
| Ébano | Limitada | 20 | 16 | 8 | Extraordinariamente denso para ser madera |
| Secoya | Singular | 60 | 22 | 7 | Resistencia estructural excepcional; crece solo en zonas específicas |

---

## Fibras, cuero y textiles

| Material | Acc. | S/kg | D base | P base | Notas |
| --- | --- | ---: | ---: | ---: | --- |
| Algodón | General | 8 | 2 | 1 | Textil suave |
| Lana | General | 12 | 3 | 1 | Algo más denso; aún textil |
| Lino | General | 10 | 4 | 2 | Resistente para su peso |
| Yute | General | 6 | 4 | 2 | Fibra robusta; cuerdas, no protección real |
| Seda | General | 20 | 6 | 2 | Sorprendentemente resistente a tracción; sin filo |
| Tela | General | 8 | 4 | 1 | Textil procesado a partir de fibras naturales |
| Cuero | Limitada | 18 | 10 | 3 | Piel procesada; protección flexible, no corta |
| Cuero escamado | Limitada | 30 | 14 | 4 | Escamas integradas sobre cuero; protección adicional |
| Seda de Arakhel | Singular | 120 | 18 | 5 | Fibra de criatura tratada; resistencia comparable a metales ligeros. Precio de mercado para seda procesada — producción cruda: ver entrada de especie Arakhel |

El cuero y el cuero escamado son materiales **procesados** — se obtienen a partir de pelaje y escamas mediante trabajo de Sastrería.

---

## Partes de criatura — estructurales

| Material | Acc. | S/kg | D base | P base | Notas |
| --- | --- | ---: | ---: | ---: | --- |
| Plumaje | General | 10 | 3 | 1 | Frágil; aislante y decorativo |
| Pelaje | General | 10 | 4 | 2 | Algo más robusto; aún textil |
| Garras | General | 16 | 8 | 16 | Muy afiladas; Potencia alta, Durabilidad moderada |
| Cuernos | General | 16 | 12 | 14 | Queratina densa; excelente material de arma natural |
| Huesos | Limitada | 16 | 10 | 8 | Estructura calcárea; equilibrado en ambos |
| Colmillos | Limitada | 16 | 10 | 18 | Diseñados para penetrar; la mayor Potencia de materiales comunes de criatura |
| Escamas | Limitada | 20 | 16 | 4 | Protección estructural flexible; prácticamente sin potencia ofensiva |
| Caparazón | Limitada | 30 | 22 | 5 | La mayor Durabilidad de materiales de criatura; protección estructural pura |

---

## Partes de criatura — sensibles

Materiales de precisión para uso alquímico. No tienen valor estructural — su D y P indican únicamente que se destruyen ante el menor intento de ruptura.

| Material | Acc. | Precio | D base | P base | Unidad |
| --- | --- | --- | ---: | ---: | --- |
| Fluidos | General | 20 S | 2 | 0 | por litro |
| Glándulas | Limitada | 30 S | 2 | 0 | por unidad |
| Órganos | Limitada | 40 S | 2 | 0 | por unidad |
| Sistema nervioso | Singular | 150 S | 1 | 0 | por unidad |

---

## Gemas y piedras preciosas

Las gemas se usan en cantidades pequeñas en joyería. Los precios por kilogramo son para referencia de extracción y comercio mayorista — una pieza de joyería consume entre 0,02 y 0,1 kg de material.

**Dureza** y **Potencia** no son lo mismo. El diamante raya todo — y se parte ante un impacto directo. El jade es menos duro pero casi imposible de fracturar.

| Material | Acc. | S/kg | D base | P base | Notas |
| --- | --- | ---: | ---: | ---: | --- |
| Lapislázuli | Limitada | 30 | 8 | 7 | Semiprecioso moderado |
| Cuarzo | Limitada | 20 | 10 | 10 | 7 Mohs; rasca metales blandos |
| Cristales | Limitada | 30 | 10 | 9 | Similar a cuarzo; variados en color |
| Topacio | Singular | 120 | 13 | 13 | 8 Mohs; duro y algo tenaz |
| Esmeralda | Singular | 170 | 13 | 12 | Similar a topacio; algo más frágil |
| Corindón | Singular | 140 | 16 | 16 | 9 Mohs, duro y tenaz — se presenta como zafiro (azul) o rubí (rojo) |
| Jade | Singular | 150 | 20 | 8 | El mineral más tenaz conocido; no es para corte |
| Diamante | Singular | 250 | 12 | 26 | Más duro que todo (10 Mohs) pero frágil bajo impacto directo |

---

## Reactivos botánicos

Las plantas y hongos se cotizan por **unidad colectada**. Su precio varía con la accesibilidad en zona de recolección.

| Accesibilidad | Precio orientativo | Ejemplos de uso |
| --- | --- | --- |
| Alta (zona segura, planta común) | 3–8 S/u | Reactivos alquímicos básicos, medicamentos simples |
| Media (zona moderada o planta menos común) | 8–15 S/u | Fórmulas intermedias, tratamientos específicos |
| Baja (zona peligrosa o planta rara) | 15–20 S/u | Reactivos excepcionales, venenos complejos |

Los reactivos botánicos no tienen D/P útiles — son materiales consumibles de proceso, no estructurales.

---

## Ejemplos de costo total de fabricación

**Daga de hierro, Grado 1** (1 kg hierro, General)

- Material: 10 S × 1 × 1 kg = **10 S**
- Mano de obra: 15 × 1 × 1 kg = **15 S**
- Total: **25 S** — D del arma: 14, P del arma: 12

**Hoja larga (una mano) de acero, Grado 2** (2 kg acero, Limitada)

- Material: 30 S × 2 × 2 kg = **120 S**
- Mano de obra: 45 × 2 × 2 kg = **180 S**
- Total: **300 S** — D del arma: 40, P del arma: 36

**Armadura intermedia completa de hierro, Grado 1** (17 kg, General)

- Material: 10 S × 1 × 17 kg = **170 S**
- Mano de obra: 15 × 1 × 17 kg = **255 S**
- Total: **425 S** — D de cada pieza: 14

**Armadura pesada completa de acero, Grado 2** (25 kg, Limitada)

- Material: 30 S × 2 × 25 kg = **1.500 S**
- Mano de obra: 45 × 2 × 25 kg = **2.250 S**
- Total: **3.750 S** — D de cada pieza: 40

Estos son precios de **mercado en asentamiento**. Una comisión directa a un especialista libre suma el jornal completo por cada día de trabajo, resultando en costos significativamente mayores.
