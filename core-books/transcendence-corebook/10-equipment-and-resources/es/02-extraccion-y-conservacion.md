---
title: "Extracción y Conservación"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 10
status: draft
canonical: false
tags: [materiales, extracción, conservación, partes-de-criatura, medicina, minería, herboristería]
related:
  - core-books/transcendence-corebook/10-equipment-and-resources/es/01-materiales.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/04-fabricacion-equipo.md
  - core-books/transcendence-corebook/11-ailments/es/03-aflicciones.md
authority_refs:
  - Transcendence-design/docs/system/materials-and-fabrication.md
  - Transcendence-design/data/system/materials-and-fabrication.yaml
---

# Extracción y Conservación

## Extracción

Despiezar una presa en el fango no es lo mismo que picar piedra. Cada proceso de extracción exige herramientas precisas y conocimientos específicos.

### Dominios de extracción

| Fuente | Especialización |
| --- | --- |
| Tejidos, pieles, órganos, glándulas, fluidos de criatura | Medicina |
| Filones minerales, mineral bruto, piedra, tierra compactada | Minería |
| Plantas, hongos, reactivos botánicos | Herboristería |

### Requisitos de extracción

Una extracción normalmente requiere todo lo siguiente:

- acceso físico válido a la fuente
- herramienta o kit adecuado
- suficiente integridad restante en la fuente
- la especialización relevante a un rango creíble
- superar un umbral de tarea determinado por la accesibilidad del material, el estado de la fuente o la presión del entorno

### Grados de herramienta

Las herramientas y kits determinan qué se puede extraer de forma segura y eficiente.

| Kit | Puede extraer de forma segura hasta | Reducción de tiempo | Bonificador a la tirada |
| --- | --- | --- | --- |
| Grado 1 | Grado 1 (común) | — | +0 |
| Grado 2 | Grado 2 (raro) | 25% | +1 |
| Grado 3 | Grado 3 (excepcional) | 50% | +2 |

Un kit de Grado 1 no puede extraer material raro o excepcional de forma segura.

### Resultados de la extracción

En caso de fallo, el resultado por defecto es generalmente uno o más de los siguientes:

- tiempo invertido sin rendimiento válido
- muestra desgarrada o inútil
- exposición biológica o derrame tóxico (riesgo de Infección activado)
- riesgo de Veneno activado
- daño a una parte sensible de uso posterior

### Determinar el Grado de la Muestra

Al extraer un material, su calidad (Grado 1, 2 o 3) define qué tan potente o puro es para la fabricación. El grado se determina al momento de la extracción según la fuente:

**Materiales Naturales (Minería y Herboristería):**
La pureza de una veta mineral o la potencia de un espécimen botánico salvaje se define mediante una tirada de **1d100** tras una extracción exitosa:
- **01-60:** Grado 1 (Común)
- **61-85:** Grado 2 (Raro)
- **86-100:** Grado 3 (Excepcional)

**Partes de Criatura (Medicina y Supervivencia):**
El grado de la biomasa está dictado por la letalidad y el desarrollo anatómico de la presa. Depende del Rango de la criatura cazada:
- **Criatura Común:** Produce biomasa de **Grado 1** (Común).
- **Criatura Campeón:** Produce biomasa de **Grado 2** (Raro).
- **Criatura Élite:** Produce biomasa de **Grado 3** (Excepcional).

---

## Partes de criatura

El despiece biológico es una carrera contra la putrefacción. Las partes no sensibles (huesos, placas, escamas) toleran la fuerza bruta. Sin embargo, las partes sensibles (glándulas, nervios, órganos) exigen cortes quirúrgicos; un fallo en el tejido blando no solo arruina la muestra, sino que a menudo perfora sacos de toxinas o libera esporas directo a la cara del extractor.

### Grupos de extracción

Las partes de criatura se dividen en dos grupos con lógicas distintas:

| Grupo | Partes | Unidad de medida |
| --- | --- | --- |
| **No sensibles** | Pelaje, escamas, caparazón, plumaje, huesos, cuernos, garras, colmillos | kg |
| **Sensibles** | Glándulas, órganos, fluidos, sistema nervioso | unidades / litros |

Las partes no sensibles se extraen en volumen — hueso, escama, pelaje. Las sensibles exigen cortes exactos; un fallo en un órgano o una glándula arruina la muestra entera.

### Tiempo y rendimiento

#### Partes sensibles

| Tamaño de criatura | Tiempo base | Rendimiento base |
| --- | --- | --- |
| Pequeño | 120 min | 1 unidad |
| Mediano | 240 min | 2 unidades |
| Grande | 360 min | 3 unidades |
| Enorme | 480 min | 4 unidades |
| Gigantesco | 600 min | 5 unidades |

#### Partes no sensibles

| Tamaño de criatura | Tiempo base | Rendimiento base |
| --- | --- | --- |
| Pequeño | 60 min | 2 kg |
| Mediano | 120 min | 4 kg |
| Grande | 240 min | 8 kg |
| Enorme | 360 min | 15 kg |
| Gigantesco | 480 min | 25 kg |

### Riesgos de extracción

La extracción de partes de criatura es una de las principales interfaces naturales con presión de Infección y Veneno.

**Partes con riesgo de Infección** — exponen al extractor a contaminación biológica, parásitos, putrefacción o residuo interno:

- Pelaje, escamas, plumaje, órganos, fluidos

**Partes con riesgo de Veneno** — exponen al extractor a veneno, sacos de toxina, bordes contaminados o estructuras de entrega activas:

- Colmillos, glándulas, garras

En ambos casos, el riesgo escala con el grado del material:

| Grado extraído | Presión de riesgo |
| --- | --- |
| Común | Menor |
| Raro | Moderado |
| Excepcional | Grave |

El Narrador llama a la T.R. de Infección o Veneno cuando la ficción apoya un riesgo real de exposición.

---

## Conservación

De nada sirve arrancar una glándula intacta si se pudre en tu mochila antes de llegar al campamento o a la fragua. Los minerales y metales son estables, pero la biomasa y los reactivos exigen conservación inmediata.

### Clases de conservación

| Clase | Significado |
| --- | --- |
| **Estable** | No se deteriora de forma significativa en almacenamiento normal |
| **Perecedero** | Se deteriora con el tiempo sin conservación adecuada |
| **Volátil** | Se deteriora rápido, se desestabiliza o se vuelve peligroso sin manejo inmediato |

Como orientación general:

- Minerales, piedra y la mayoría de los metales son **estables**
- Pieles, fluidos, órganos, glándulas y muchos reactivos vegetales son **perecederos**
- Tejido nervioso, glándulas inestables, venenos frescos y tejidos similares son **volátiles**

Sin conservación válida, el material eventualmente:

- queda inválido para un proceso específico
- o se vuelve peligroso de manipular

### Conservación de materiales vivos

Conservar un material vivo no es almacenarlo; es mantener a un espécimen en cautiverio. Requieren **mantenimiento activo**. Dependiendo de la entrada del material, ese mantenimiento puede incluir:

- humedad controlada
- oscuridad
- circulación de aire
- medio de alimentación
- exposición a resonancia
- quietud taumática o carga taumática específica
- manejo adaptado a la especie de origen

### Perfiles de conservación de partes de criatura

| Parte | Kit mínimo | Tiempo en condiciones favorables | Requisito |
| --- | --- | --- | --- |
| Pelaje / Plumaje | Grado 1 | 1 mes | Almacenamiento seco, fresco, alejado de humedad |
| Escamas / Caparazón | Grado 2 | 2 meses | Limpiar residuo orgánico y almacenar seco |
| Colmillos / Garras | Grado 1 | 6 semanas | Secar completamente y mantener en baja humedad |
| Huesos / Cuernos | Grado 2 | 2 meses | Retirar tejido blando y tratar con conservante |
| Glándulas / Órganos | Grado 3 | 1 semana | Preservar en salino, alcohol o medio equivalente |
| Fluidos | Grado 1 | 2 semanas (sangre) / 1 mes (venenos) | Contenedores sellados y aislados |
| Sistema nervioso | Grado 3 | 3 días | Conservación controlada en medio especializado |

Las entradas individuales de criatura o tejido tauma-reactivo pueden modificar estos perfiles.
