---
title: "Venenos"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 11
status: draft
canonical: false
tags: [ailments, venenos, poisons, toxins, alchemy, kit, administration]
related:
  - core-books/transcendence-corebook/11-ailments/en/04-poisons.md
  - core-books/transcendence-corebook/11-ailments/es/01-agravios.md
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Venenos

Un **Veneno** entra al organismo a través de una vía de administración — mordedura, ingestión, inhalación, contacto — y actúa desde dentro. No termina cuando termina la fuente: persiste en el cuerpo hasta que algo lo neutralice.

**Tirada de Resistencia:** `1d10 + Tenacidad + nivel de competencia en Resistencia a Venenos + bonificadores adicionales`

---

## Kit de Venenos

La manipulación de cualquier veneno requiere un **Kit de Venenos** adecuado a la rareza del veneno. Sin el kit correspondiente, el riesgo de autocontaminación es alto:

| Severidad del veneno | Riesgo de autocontaminación |
| --- | --- |
| Leve | 50% |
| Moderado | 75% |
| Grave | 100% |

---

## Identificación

Los personajes con conocimiento en **Entendimiento (Alquimia)** pueden identificar venenos desconocidos. La complejidad de la identificación se determina por el **Índice Alquímico** del veneno:

| Índice Alquímico | Nivel | Descripción |
| --- | --- | --- |
| 2–4 | Fundamentos | Venenos básicos; riesgos y efectos menores |
| 5–6 | Desafiante | Complejidad intermedia; riesgos y efectos moderados |
| 7–8 | Riguroso | Venenos complejos; efectos y riesgos significativos |
| 9 | Exigente | Venenos muy complejos; efectos peligrosos |
| 10 | Extremo | Excepcional potencia y peligrosidad |

---

## Aplicación

| Contexto | Tiempo |
| --- | --- |
| Fuera de combate | ~1 minuto |
| En combate | 1 acción estándar |

Los venenos pueden aplicarse en armas, alimentos o directamente sobre el objetivo, según la naturaleza del veneno y su vía de administración.

---

## Vías de Administración

| Vía | Descripción |
| --- | --- |
| **Inoculación** | Introducción directa en el torrente sanguíneo — mordeduras, picaduras, armas impregnadas |
| **Ingestión** | El veneno entra por el sistema digestivo — alimentos, bebidas, plantas contaminadas |
| **Inhalación** | El veneno se absorbe por los pulmones — gases, vapores, polvos |
| **Contacto** | El veneno se absorbe a través de la piel — requiere exposición directa o piel comprometida |

---

## Duración

Los Venenos tienen duración `hasta_eliminar` — permanecen activos aunque la fuente que los introdujo ya no esté presente.

---

## Tratamiento

Neutralizar un veneno activo en un organismo requiere un **Kit de Medicina** adecuado a la rareza del veneno. Sin el kit correspondiente no es posible el tratamiento.

| Kit de Medicina | Veneno tratable |
| --- | --- |
| Básico | Venenos comunes (Leve) |
| Avanzado | Venenos raros (hasta Moderado) |
| Especializado | Venenos excepcionales (hasta Grave) |

El tratamiento puede llevarse a cabo mediante técnicas de sanación o métodos alquímicos. La dificultad depende de la potencia y naturaleza del veneno.

---

## Catálogo

Los efectos de cada Veneno son **acumulativos por severidad**: Moderado incluye todo lo de Leve, Grave incluye todo lo de Moderado.

La penalización numérica de cada Veneno es igual al **bonificador de rango de la fuente** que lo introdujo en el organismo. La severidad determina qué restricciones adicionales se activan.

---

## Entorpecido

*La criatura cree que actúa. El cuerpo discrepa sobre el momento.*

**Aplicación:** Se aplica cuando un compuesto que interrumpe la transmisión neuromuscular entra al organismo por inoculación.

**Duración:** Hasta eliminar.

**Recuperación:** Requiere Kit de Medicina Avanzado (Leve) o Especializado (Moderado y Grave). El compuesto debe neutralizarse activamente — el descanso completo por sí solo no lo elimina.

**Índice Alquímico:** 7 (Riguroso)

| Severidad | Efectos |
| --- | --- |
| **Leve** | Todas las acciones cuestan Ritmo adicional igual al bonificador de rango de la fuente que aplicó Entorpecido. |
| **Moderado** | Leve, más: las acciones libres que requieren ejecución física cuestan 1 de Ritmo en lugar de 0. |
| **Grave** | Moderado, más: la penalización de Ritmo se duplica para las Reacciones — el bonificador de rango adicional se aplica dos veces específicamente para ellas. |

---

## Escaldado

*Apuntar requiere ver. Ver requiere quietud. Ninguna de las dos sobrevive el contacto.*

**Aplicación:** Se aplica cuando un alcaloide cáustico entra al organismo por inoculación y reacciona con tejidos sensoriales: membranas mucosas, ojos, terminaciones nerviosas superficiales.

**Duración:** Hasta eliminar.

**Recuperación:** Requiere Kit de Medicina Básico (Leve) o Avanzado (Moderado y Grave). El bajo Índice Alquímico facilita la identificación del compuesto.

**Índice Alquímico:** 5 (Desafiante)

| Severidad | Efectos |
| --- | --- |
| **Leve** | Todas las `T.A.` sufren una penalización igual al bonificador de rango de la fuente que aplicó Escaldado. |
| **Moderado** | Leve, más: las `T.A.` contra objetivos a más de 3 m sufren una penalización adicional de `−1` (la disrupción visual empeora con la distancia). |
| **Grave** | Moderado, más: el objetivo no puede beneficiarse de Ventaja de Ejecución en `T.A.` — aunque existan condiciones que normalmente la otorgarían, la disrupción sensorial impide aprovecharlas. |

---

## Erosionado

*La armadura resistió. El compuesto no lo tuvo en cuenta.*

**Aplicación:** Se aplica cuando un complejo enzimático entra al organismo por inoculación y actúa sistémicamente a través del torrente sanguíneo, descomponiendo las proteínas estructurales de las capas protectoras biológicas en todas las zonas del cuerpo.

**Duración:** Hasta eliminar.

**Recuperación:** Requiere Kit de Medicina Especializado en todas las severidades. El complejo enzimático no se degrada espontáneamente — requiere neutralización activa. Identificación mediante Entendimiento (Alquimia) a dificultad Rigurosa o superior.

**Índice Alquímico:** 8 (Riguroso)

| Severidad | Efectos |
| --- | --- |
| **Leve** | El Bloqueo de todas las zonas del objetivo se reduce en una cantidad igual al bonificador de rango de la fuente que aplicó Erosionado. |
| **Moderado** | Leve, más: el objetivo no puede beneficiarse de bonificaciones al Bloqueo procedentes de fuentes externas (mejoras de equipo, técnicas, acciones de aliados) mientras Erosionado esté activo — el tejido degradado no puede integrar protección suplementaria. |
| **Grave** | Moderado, más: el Bloqueo efectivo del objetivo en cualquier zona no puede superar 1, independientemente del valor base o los modificadores — la degradación proteica estructural es completa a esta severidad. |

---

## Saturado

*El cuerpo tiene fronteras. El compuesto disuelve al guardia.*

**Aplicación:** Se aplica cuando un compuesto nefrotóxico entra al organismo por inoculación y se acumula en el sistema renal, colapsando su capacidad de filtración.

**Duración:** Hasta eliminar.

**Recuperación:** Requiere Kit de Medicina Especializado para eliminar el compuesto del sistema renal. Dado que Saturado amplifica el efecto de todos los demás Agravios activos, debe priorizarse en el tratamiento. Identificación mediante Entendimiento (Alquimia) a dificultad Exigente.

**Índice Alquímico:** 9 (Exigente)

| Severidad | Efectos |
| --- | --- |
| **Leve** | Todas las `T.R.` del objetivo — contra Alteraciones, Venenos, Infecciones, Aflicciones y Maldiciones — sufren una penalización igual al bonificador de rango de la fuente que aplicó Saturado. |
| **Moderado** | Leve, más: las `T.R. de Venenos` se realizan a un umbral de dificultad superior — el sistema de filtración está más directamente colapsado y no puede resistir agentes tóxicos adicionales con eficacia. |
| **Grave** | Moderado, más: el nivel de competencia en Resistencia a Venenos del objetivo no contribuye a sus `T.R. de Venenos` mientras Saturado esté activo — la resistencia entrenada no puede aprovecharse cuando el sistema de filtración está completamente comprometido. |

---

## Inhibido

*La herida espera. La reparación no llega.*

**Aplicación:** Se aplica cuando un compuesto hepatotóxico entra al organismo por inoculación y suprime la síntesis hepática de proteínas reparadoras: factores de coagulación, factores de crecimiento, moduladores inflamatorios.

**Duración:** Hasta eliminar.

**Recuperación:** Inhibido debe neutralizarse antes de que cualquier herida o Agravio en el mismo objetivo pueda ser tratado. La neutralización del propio compuesto es tratamiento directo del veneno — no curación de heridas — y no está bloqueada por la restricción que el propio Inhibido impone. La severidad determina el kit requerido para esa neutralización.

**Índice Alquímico:** 9 (Exigente)

| Severidad | Efectos |
| --- | --- |
| **Leve** | Las acciones de Kit de Medicina dirigidas a esta criatura operan a un umbral de dificultad superior. Las técnicas de curación restauran la mitad de su cantidad normal (redondear hacia abajo). |
| **Moderado** | Las acciones de Kit de Medicina para tratamiento de heridas no tienen efecto. Las técnicas de curación restauran un cuarto de su cantidad normal (redondear hacia abajo). Neutralizar el propio Inhibido requiere Kit de Medicina Especializado y funciona normalmente — tratar el veneno no está bloqueado. |
| **Grave** | Ningún tratamiento de heridas (Kit de Medicina), técnica de curación ni acción de recuperación tiene efecto mientras Inhibido esté activo. Neutralizar Inhibido requiere Kit de Medicina Especializado y una `T.E.` de Medicina a dificultad Exigente. Una vez neutralizado, curación y tratamiento se reanudan con normalidad. |
