---
title: "Aflicciones"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 11
status: draft
canonical: false
tags: [ailments, aflicciones, afflictions, conditions, progression, vínculo, vestigio]
related:
  - core-books/transcendence-corebook/11-ailments/en/03-afflictions.md
  - core-books/transcendence-corebook/11-ailments/es/01-agravios.md
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Aflicciones

Las **Aflicciones** son disrupciones mentales, perceptuales o de estado interno. A diferencia de las Alteraciones — que son disrupciones fisiológicas directas del cuerpo — las Aflicciones comprometen la estabilidad interna del ser: juicio, percepción, regulación emocional, integridad cognitiva.

Una Aflicción puede tener origen en exposición psíquica, contacto con vestigios o vínculos, trauma sostenido, presencia de horror o infusión extranatural. Lo que la define es que el resultado es una disrupción del estado interno que no se resuelve como una lesión física ordinaria.

**Tirada de Resistencia:** `1d10 + Compostura + nivel de competencia en Resistencia a Aflicciones + bonificadores adicionales`

---

## Intensidad y Progresión

Las Aflicciones no tienen una duración fija. En cambio, tienen una **Intensidad** — un valor que sube o baja según cómo el personaje lleva su estado, su exposición a ciertos elementos y su acceso a recuperación.

Una Aflicción comienza en **Intensidad Leve** (5 puntos) y puede progresar a través de tres umbrales:

| Severidad | Umbral de Intensidad |
| --- | --- |
| **Leve** | 5 |
| **Moderado** | 10 |
| **Grave** | 15 |

El umbral de Intensidad también determina la dificultad de las pruebas relevantes durante el proceso de empeoramiento y recuperación.

Cuando la Intensidad de una Aflicción sube lo suficiente para cruzar el siguiente umbral, la Aflicción avanza a esa severidad. Cuando baja por debajo del umbral actual, retrocede.

---

## Factores de Empeoramiento

Los siguientes factores aumentan la Intensidad de una Aflicción activa:

| Factor | Modificador |
| --- | --- |
| Noche sin descanso completo | `+1` |
| Interacción con un vestigio — usarlo o descubrirlo | `+1` |
| Interacción con un vínculo — descubrirlo | `+1` |

Cada factor se aplica una vez por evento o período relevante.

---

## Factores de Tratamiento

Los siguientes factores reducen la Intensidad de una Aflicción activa:

| Factor | Modificador |
| --- | --- |
| Noche de buen descanso | `−1` |
| Sesión de Meditación efectiva | `−1` |

---

## Regla de Aflicción Nueva

Una vez que una Aflicción ha progresado a **Intensidad Grave**, el personaje ya no puede empeorar esa Aflicción individualmente. En cambio, la próxima vez que reciba una Aflicción — ya sea la misma u otra — recibe una **nueva Aflicción separada** que comienza en Intensidad Leve.

Las Aflicciones paralelas activas son estados distintos. Cada una lleva su propio umbral y responde a sus propios factores de empeoramiento y tratamiento de forma independiente.

---

## Catálogo

### Vista

#### Esquizofrenia Paranoide

*Disrupción paranoide del juicio de amenaza. El personaje interpreta presencias neutras o ambiguas como fuentes de peligro inminente. La lectura de intención queda contaminada.*

**Disparador:** cuando percibe una criatura en un contexto de incertidumbre, ambigüedad social o amenaza potencial no confirmada.

**T.E.:** Astucia contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Astucia relacionadas con intención, lectura social o detección de amenaza. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Astucia; si falla → Aterrorizado Leve por el resto de la escena. |
| **Grave** | Moderado, más: si falla esa T.E. → también queda Atrapado Leve por el resto de la escena. |

**Canal Extranatural:** puede detectar genuinamente amenazas ocultas, intenciones disimuladas y entidades que se presentan como presencias benignas.

---

#### Agnosia Visual

*Pérdida de la capacidad de reconocimiento funcional. El personaje ve objetos y criaturas pero la cognición falla al intentar identificarlos o asignarles función.*

**Disparador:** al intentar interactuar con un objeto de forma deliberada, o al intentar reconocer una criatura específica.

**T.E.:** Identificación (Intelecto) contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Identificación. |
| **Moderado** | Leve, más: al activarse el disparador sobre un objeto, debe superar T.E. de Identificación; si falla → la interacción no se resuelve esa activación. |
| **Grave** | Moderado, más: el disparador también aplica para reconocer criaturas; si falla → no puede distinguirla del entorno ni dirigir acciones contra ella específicamente esa activación. |

**Canal Extranatural:** ve símbolos ocultos, inscripciones extranaturales y geometrías imposibles en los objetos del entorno.

---

#### Alucinaciones Visuales

*Superposición de imágenes falsas sobre la percepción real. El personaje recibe estímulos visuales que no tienen correlato en el mundo físico.*

**Disparador:** al inicio de cada activación del personaje, o cuando el Narrador lo determine durante una escena de alta carga visual o presencia extranatural.

**T.E.:** Percepción (Sabiduría) contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Percepción visual. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Percepción; si falla → Confundido Leve por el resto de la escena. |
| **Grave** | Moderado, más: si falla esa T.E. → también queda Desorientado Leve por el resto de la escena. |

**Canal Extranatural:** percibe realidades superpuestas, ecos y huellas de presencias extranaturales que ya no están o aún no han llegado.

---

### Oído

#### Tinnitus

*Zumbido o tono persistente que interfiere con la Percepción auditiva y la concentración sostenida.*

**Disparador:** al realizar una acción que requiera concentración sostenida o Percepción auditiva activa.

**T.E.:** Percepción (Sabiduría) contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Percepción auditiva. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Percepción; si falla → Impedido Leve por el resto de la escena. |
| **Grave** | Moderado, más: si falla esa T.E. → Sobrecargado Leve por el resto de la escena en lugar de Impedido Leve. |

**Canal Extranatural:** escucha susurros ocultos, frecuencias extranaturales y comunicaciones entre entidades que no son perceptibles para otros.

---

#### Hiperacusia

*Hipersensibilidad al sonido. Estímulos auditivos repentinos o sostenidos producen una respuesta de colapso desproporcionada.*

**Disparador:** al exponerse a sonidos repentinos, sostenidos o de alta intensidad.

**T.E.:** Enfoque (Compostura) contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Compostura. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Enfoque; si falla → Aturdido Leve por el resto de la escena. |
| **Grave** | Moderado, más: si falla esa T.E. → Ensordecido Leve por el resto de la escena en lugar de Aturdido Leve. |

**Canal Extranatural:** percibe vibraciones sutiles no acústicas: tensiones emocionales, presencias ocultas, movimientos en el plano adyacente.

---

#### Eco Persistente

*El oído interno registra ecos sin correlato real. El sistema vestibular, ligado al oído, queda comprometido, afectando el equilibrio y la orientación espacial.*

**Disparador:** al intentar orientarse, moverse con precisión o mantener el equilibrio en terreno exigente.

**T.E.:** Equilibrio (Agilidad) contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Percepción auditiva y T.E. de Orientación. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Equilibrio; si falla → Desequilibrado Leve por el resto de la escena. |
| **Grave** | Moderado, más: si falla esa T.E. → Paralizado Leve por el resto de la escena en lugar de Desequilibrado Leve. |

**Canal Extranatural:** escucha ecos de otras realidades y percibe movimientos de presencias en el plano adyacente.

---

### Olfato

#### Phantosmia

*Percepción olfativa de olores sin origen físico. Los estímulos fantasma saturan y desestabilizan la regulación interna.*

**Disparador:** al encontrarse en una escena de alta tensión o proximidad extranatural confirmada o sospechada.

**T.E.:** Contención (Compostura) contra la Intensidad actual. No aplica a T.C.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Compostura. No aplica a T.C. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Contención; si falla → Sobrecargado Leve por el resto de la escena. |
| **Grave** | Moderado, más: si falla esa T.E. → Sobrecargado Moderado por el resto de la escena en lugar de Sobrecargado Leve. |

**Canal Extranatural:** detecta rastros de corrupción y Tauma; percibe la presencia de entidades extranaturales por olor antes de detectarlas por otros medios.

---

#### Hiperosmia

*Hipersensibilidad olfativa. Los olores del entorno resultan invasivos e incapacitantes.*

**Disparador:** al exponerse a olores intensos, concentrados o activos en el entorno.

**T.E.:** Enfoque (Compostura) contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Enfoque. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Enfoque; si falla → Aturdido Leve por el resto de la escena. |
| **Grave** | Moderado, más: la Preparación del personaje se reduce a 0; si falla esa T.E. → también queda Sobrecargado Leve por el resto de la escena. |

**Canal Extranatural:** rastrea criaturas invisibles por olor; detecta presencias extranaturales activas en el área.

---

### Gusto

#### Disgeusia

*Distorsión persistente del gusto. Cualquier ingesta resulta repulsiva o ajena, interfiriendo con el descanso y la recuperación.*

**Disparador:** al intentar comer o beber durante un descanso.

**T.E.:** Contención (Compostura) contra la Intensidad actual.

| Intensidad | Efecto en caso de fallo |
| --- | --- |
| **Leve** | Pierde 1 nivel de recuperación de Fatiga en ese descanso. |
| **Moderado** | Pierde 2 niveles de recuperación de Fatiga y no puede realizar actividades adicionales durante ese descanso. |
| **Grave** | No recupera Fatiga ni reduce la Intensidad de ninguna Aflicción activa en ese descanso. |

**Canal Extranatural:** detecta sustancias corrompidas, envenenadas o impregnadas de presencia extranatural al probarlas o estar en su proximidad directa.

---

#### Compulsión Alimentaria

*Impulso irrefrenable de consumir materia al terminar situaciones de alta carga hostil. La compulsión escala con la Intensidad hacia consumos cada vez más peligrosos.*

**Disparador:** al terminar una escena hostil o al encontrar cadáveres, restos o tejido orgánico accesible.

**T.E.:** Contención (Compostura) contra la Intensidad actual.

| Intensidad | Efecto en caso de fallo |
| --- | --- |
| **Leve** | Debe consumir materia inerte — tierra, polvo, residuos, insectos. Recibe Desequilibrado Leve. |
| **Moderado** | Debe consumir materia orgánica contaminada — tejido muerto, fluidos, restos de criatura. Recibe Infección Leve. |
| **Grave** | Debe consumir material tóxico o cáustico — carne envenenada, fluidos activos, material corrosivo. Recibe Infección Leve y Veneno Leve. |

**Canal Extranatural:** recibe fragmentos de visión o memoria residual del material consumido — imágenes, emociones, instantes del pasado del organismo o entidad.

---

### Tacto

#### Formicación

*Sensación persistente de movimiento bajo la piel: hormigueo, presión o contacto sin origen externo. El coste de acción se expande a medida que la Intensidad aumenta.*

**Efecto pasivo:** no requiere T.E. de activación.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Acciones de contacto físico directo cuestan +1 Ritmo adicional. |
| **Moderado** | Técnicas físicas y T.E. de Enfoque cuestan +1 Ritmo adicional. |
| **Grave** | Todas las acciones cuestan +1 Ritmo adicional. |

**Canal Extranatural:** percibe entidades incorporales y rastros del plano adyacente a través del contacto físico directo.

---

#### Anestesia Parcial

*Pérdida parcial de la sensación de daño externo. El cuerpo no registra correctamente las señales de peligro, y las defensas de resistencia quedan reducidas.*

**Efecto pasivo:** no requiere T.E. de activación.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.R. contra Alteraciones. |
| **Moderado** | Penalización de −1 a T.R. contra Alteraciones e Infecciones. |
| **Grave** | Penalización de −1 a T.R. contra Alteraciones, Infecciones y Venenos. |

**Canal Extranatural:** percibe el plano intangible; detecta presencias sin forma física en el área inmediata.

---

#### Hipertacto

*Hipersensibilidad táctil. El contacto con objetos o criaturas produce estímulos desproporcionados que desestabilizan la regulación interna.*

**Disparador:** al tocar un objeto o una criatura de forma deliberada.

**T.E.:** Enfoque (Compostura) contra la Intensidad actual.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Enfoque al tocar objetos o criaturas. |
| **Moderado** | Leve, más: al activarse el disparador, debe superar T.E. de Enfoque; si falla → Sobrecargado Leve por el resto de la escena. |
| **Grave** | Moderado, más: si falla esa T.E. → Impedido Leve por el resto de la escena en lugar de Sobrecargado Leve. |

**Canal Extranatural:** siente corrientes de energía en los objetos; detecta propiedades ocultas y procedencias extranaturales al contacto directo.
