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

*Las presencias neutras empiezan a tener intención. El cuerpo las trata como amenazas antes de que la mente decida.*

Lees intención donde puede que no la haya. Una persona que espera en la puerta, una mirada que se sostiene un segundo, un movimiento en el borde del campo visual — el cuerpo ya calculó la amenaza antes de que puedas evaluarla. No es que estés equivocado todo el tiempo. El problema es que no puedes distinguir cuándo lo estás.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Astucia relacionadas con intención, lectura social o detección de amenaza. |
| **Moderado** | Penalización de −2 a T.E. de Astucia; si fallas, quedas Aterrorizado Leve. |
| **Grave** | Penalización de −3 a T.E. de Astucia; si fallas, quedas Aterrorizado Moderado y Atrapado Moderado. |

**Canal Extranatural:** puede detectar genuinamente amenazas ocultas, intenciones disimuladas y entidades que se presentan como presencias benignas.

---

#### Agnosia Visual

*La imagen llega. El significado no.*

Ves con claridad. El objeto está ahí, sus bordes definidos, su forma completa — pero no sabes qué es. El reconocimiento directo ya no funciona de manera confiable. Tienes que construir el significado a través del contexto, la posición, cualquier pista que no sea la identificación inmediata.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Identificación. |
| **Moderado** | Penalización de −2 a T.E. de Identificación; si fallas, la acción que la requería no se resuelve esa activación. |
| **Grave** | Penalización de −3 a T.E. de Identificación; si la T.E. fallida era para reconocer una criatura, tampoco puedes distinguirla del entorno ni dirigir acciones contra ella específicamente esa activación. |

**Canal Extranatural:** ve símbolos ocultos, inscripciones extranaturales y geometrías imposibles en los objetos del entorno.

---

#### Alucinaciones Visuales

*Lo que ve no siempre está ahí. Lo que está ahí no siempre puede verse.*

A veces percibes cosas que no están. A veces no percibes cosas que sí están. No hay consistencia en cuál falla. Aprendiste a dudar de las figuras en el borde del campo visual, de los objetos que aparecen sin haber estado antes — pero tampoco puedes estar completamente seguro de los que sí estaban.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Percepción visual. |
| **Moderado** | Penalización de −2 a T.E. de Percepción visual; si fallas, quedas Confundido Leve. |
| **Grave** | Penalización de −3 a T.E. de Percepción visual; si fallas, quedas Confundido Moderado y Desorientado Moderado. |

**Canal Extranatural:** percibe realidades superpuestas, ecos y huellas de presencias extranaturales que ya no están o aún no han llegado.

---

### Oído

#### Tinnitus

*El tono no se va. Todo lo demás llega desde un poco más lejos.*

Escuchas un pitido, zumbido o frecuencia constante que no tiene fuente en el entorno. No cambia con el silencio. Todo lo demás llega a través de ese ruido de fondo que solo tú percibes — y hay sonidos que directamente no alcanzan.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Percepción auditiva. |
| **Moderado** | Penalización de −2 a T.E. de Percepción auditiva; si fallas, quedas Impedido Leve. |
| **Grave** | Penalización de −3 a T.E. de Percepción auditiva; si fallas, quedas Sobrecargado Moderado. |

**Canal Extranatural:** escucha susurros ocultos, frecuencias extranaturales y comunicaciones entre entidades que no son perceptibles para otros.

---

#### Hiperacusia

*No hace falta que sea fuerte. El cuerpo responde como si lo fuera.*

El volumen perdió su escala. Un cubierto sobre una superficie, una puerta que se cierra, una conversación a distancia normal — cualquier sonido que antes era neutro ahora produce una respuesta física desproporcionada. No es solo que moleste. El cuerpo lo trata como una amenaza.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Compostura. |
| **Moderado** | Penalización de −2 a T.E. de Compostura; si fallas, quedas Aturdido Leve. |
| **Grave** | Penalización de −3 a T.E. de Compostura; si fallas, quedas Ensordecido Moderado. |

**Canal Extranatural:** percibe vibraciones sutiles no acústicas: tensiones emocionales, presencias ocultas, movimientos en el plano adyacente.

---

#### Eco Persistente

*El oído escucha dos veces. El suelo no siempre responde igual.*

Los sonidos llegan con un desfase que no tiene origen real. La primera vez cuando ocurren; la segunda, fracciones de segundo después, como si el entorno los repitiera. No puedes calibrar de dónde vienen con precisión, y ese error se propaga al equilibrio — el suelo ya no responde del todo como esperas.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Percepción auditiva y T.E. de Orientación. |
| **Moderado** | Penalización de −2 a T.E. de Percepción auditiva y T.E. de Orientación; si fallas cualquier T.E. de Equilibrio, quedas Desequilibrado Leve. |
| **Grave** | Penalización de −3 a T.E. de Percepción auditiva y T.E. de Orientación; si fallas esa T.E., quedas Paralizado Moderado. |

**Canal Extranatural:** escucha ecos de otras realidades y percibe movimientos de presencias en el plano adyacente.

---

### Olfato

#### Phantosmia

*El olor viene de ningún lado. El cuerpo reacciona igual.*

Percibes olores que no tienen fuente en el entorno. Pueden ser familiares o desconocidos, neutros o intensamente desagradables — pero ninguno corresponde a algo presente. El cuerpo reacciona igual: el asco, la alerta o la anticipación que activa un olor fuerte llegan completos aunque el olor sea una invención del sistema olfativo.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Compostura. No aplica a T.C. |
| **Moderado** | Penalización de −2 a T.E. de Compostura (no aplica a T.C.); si fallas cualquier T.E. de Contención, quedas Sobrecargado Leve. |
| **Grave** | Penalización de −3 a T.E. de Compostura (no aplica a T.C.); si fallas esa T.E., quedas Sobrecargado Moderado en lugar de Sobrecargado Leve. |

**Canal Extranatural:** detecta rastros de corrupción y Tauma; percibe la presencia de entidades extranaturales por olor antes de detectarlas por otros medios.

---

#### Hiperosmia

*No hace falta que sea intenso. El olfato ya no tiene escala.*

El olfato ya no tiene rango. Un nivel de intensidad que antes era neutro — la ropa de alguien cercano, el metal de un arma, el aire de un espacio cerrado — ahora llega como si estuviera concentrado a una distancia mínima. Concentrarte mientras el entorno olfativo es activo requiere un esfuerzo que antes no tenías que hacer.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Enfoque. |
| **Moderado** | Penalización de −2 a T.E. de Enfoque; si fallas, quedas Aturdido Leve. |
| **Grave** | Penalización de −3 a T.E. de Enfoque; tu Preparación se reduce a 0; si fallas, quedas Sobrecargado Moderado. |

**Canal Extranatural:** rastrea criaturas invisibles por olor; detecta presencias extranaturales activas en el área.

---

### Gusto

#### Disgeusia

*Cualquier ingesta llega como si no debiera estar ahí. El cuerpo lo reconoce, pero no lo acepta.*

El sabor de lo que comes o bebes llega alterado — amargo donde no debería, metálico, o equivocado de una forma que no puedes describir con precisión. El cuerpo lo trata como algo que no debería estar ahí. El acto de ingerir se convierte en una negociación que a veces no puedes sostener.

Al intentar comer o beber durante un descanso, realiza una T.E. de Contención (Compostura) contra la Intensidad actual.

| Intensidad | Efecto en caso de fallo |
| --- | --- |
| **Leve** | Pierdes 1 nivel de recuperación de Fatiga en ese descanso. |
| **Moderado** | Pierdes 2 niveles de recuperación de Fatiga y no puedes realizar actividades adicionales durante ese descanso. |
| **Grave** | No recuperas Fatiga ni reduces la Intensidad de ninguna Aflicción activa en ese descanso. |

**Canal Extranatural:** detecta sustancias corrompidas, envenenadas o impregnadas de presencia extranatural al probarlas o estar en su proximidad directa.

---

#### Compulsión Alimentaria

*Al terminar la violencia, algo más reclama atención. La compulsión no distingue qué es comestible.*

Al final de una escena de violencia, o ante la presencia de restos orgánicos, algo reclama atención con una urgencia que no distingue comestible de incomestible. No es hambre en el sentido ordinario — es una presión que se instala antes de que puedas procesarla, y que no desaparece hasta que cedes o la contienes de forma activa.

Al terminar una escena hostil o al encontrar cadáveres, restos o tejido orgánico accesible, realiza una T.E. de Contención (Compostura) contra la Intensidad actual.

| Intensidad | Efecto en caso de fallo |
| --- | --- |
| **Leve** | Debes consumir materia inerte — tierra, polvo, residuos, insectos. Recibes Desequilibrado Leve. |
| **Moderado** | Debes consumir materia orgánica contaminada — tejido muerto, fluidos, restos de criatura. Recibes Infección Moderado. |
| **Grave** | Debes consumir material tóxico o cáustico — carne envenenada, fluidos activos, material corrosivo. Recibes Infección Moderado y Veneno Moderado. |

**Canal Extranatural:** recibe fragmentos de visión o memoria residual del material consumido — imágenes, emociones, instantes del pasado del organismo o entidad.

---

### Tacto

#### Formicación

*Algo se mueve bajo la piel. No hay nada afuera que lo explique.*

Sientes movimiento bajo la piel — no es dolor exactamente, es presencia. Algo que se desplaza, que cambia de lugar, que responde al movimiento de tus propios músculos. No hay nada externo que lo explique y no hay manera de aliviarlo con contacto. Mantener el enfoque en lo que tienes delante requiere ignorar algo que el cuerpo trata como urgente.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Técnicas de ataque cuestan +1 Ritmo adicional. |
| **Moderado** | Técnicas de ataque y T.E. de Enfoque cuestan +1 Ritmo adicional. |
| **Grave** | Todas las acciones cuestan +1 Ritmo adicional. |

**Canal Extranatural:** percibe entidades incorporales y rastros del plano adyacente a través del contacto físico directo.

---

#### Anestesia Parcial

*El daño llega. La señal que debería registrarlo no siempre llega completa.*

La información que te dice cuánto daño recibiste llega incompleta o con retraso. No es que no sientas nada — es que lo que registras no siempre es proporcional a lo que ocurrió. Puedes recibir un golpe serio y que el cuerpo no lo transmita con la urgencia que debería. El problema no es la ausencia de dolor: es no poder confiar en él como señal.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.R. contra Alteraciones. |
| **Moderado** | Penalización de −2 a T.R. contra Alteraciones e Infecciones. |
| **Grave** | Penalización de −3 a T.R. contra Alteraciones, Infecciones y Venenos. |

**Canal Extranatural:** percibe el plano intangible; detecta presencias sin forma física en el área inmediata.

---

#### Hipertacto

*El contacto siempre produjo algo. Ahora produce demasiado.*

El contacto produce más de lo que debería. La textura de tu ropa, el peso de lo que cargas, la mano de alguien sobre tu hombro — todo llega con una intensidad que no tiene relación con lo que ocurre. Concentrarte en medio de ese ruido táctil constante requiere un esfuerzo que el cuerpo no siempre puede sostener.

| Intensidad | Efecto |
| --- | --- |
| **Leve** | Penalización de −1 a T.E. de Enfoque. |
| **Moderado** | Penalización de −2 a T.E. de Enfoque; si fallas, quedas Sobrecargado Leve. |
| **Grave** | Penalización de −3 a T.E. de Enfoque; si fallas, quedas Impedido Moderado. |

**Canal Extranatural:** siente corrientes de energía en los objetos; detecta propiedades ocultas y procedencias extranaturales al contacto directo.
