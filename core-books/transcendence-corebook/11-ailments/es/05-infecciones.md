---
title: "Infecciones"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 11
status: draft
canonical: false
tags: [ailments, infecciones, infections, contagion, incubation, spread]
related:
  - core-books/transcendence-corebook/11-ailments/en/05-infections.md
  - core-books/transcendence-corebook/11-ailments/es/01-agravios.md
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Infecciones

Una **Infección** es el entorno reclamando tu cuerpo. Entra al organismo, incuba en silencio como un parásito, y en algún momento florece. Una vez activa, no solo te consume desde adentro si no recibes tratamiento, sino que te convierte en un vector biológico que amenaza a todo tu escuadrón.

**Tirada de Resistencia:** `1d10 + Tenacidad + nivel de competencia en Resistencia a Infecciones + bonificadores adicionales`

---

## Contagio

El **Contagio** representa la resistencia inmunológica del cuerpo ante una exposición inicial. Cuando un personaje es expuesto a una fuente infecciosa, debe superar una **T.R. de Infecciones** con la dificultad especificada en la entrada de esa Infección.

Si falla, la Infección se establece en su organismo y comienza el período de incubación.

---

## Incubación

Cada Infección tiene un **período de incubación** variable según la enfermedad. Durante este período la Infección está anclada en el organismo pero permanece en estado de latencia asintomática — no hay deterioro funcional visible sobre el personaje.

Una vez que el período de incubación termina, los síntomas se manifiestan, los efectos de la Infección se activan y la Infección puede comenzar a propagarse.

---

## Propagación

Una vez que el período de incubación termina y la infección se manifiesta, el huésped se convierte en un riesgo biológico por **contacto físico directo**. Cualquier criatura que entre en contacto físico con un portador de una Infección activa debe superar una **T.R. de Infecciones** con la dificultad especificada en la entrada de esa Infección para evitar ser contagiada.

La dificultad de contagio y la dificultad de propagación pueden ser distintas — cada entrada de Infección especifica ambas si difieren.

---

## Catálogo

---

## Infección de Herida

*Una herida mal cerrada no es solo dolor — es una puerta. Bacterias, esporas y parásitos oportunistas entran donde el tejido ya no puede defenderse.*

**Aplicación:** Se establece cuando una herida abierta entra en contacto con material contaminado — cadáveres, agua estancada, suelo con alta carga orgánica, extracción de criatura sin kit adecuado, o herramientas no esterilizadas. La T.R. de Infecciones se realiza al finalizar la escena donde ocurrió la exposición.

**Incubación:** 1 Descanso Corto. Los síntomas (enrojecimiento, calor local, supuración) se manifiestan antes del primer Descanso Completo.

**Contagio:** Desafiante (8)

**Propagación:** Solo por contacto directo con la zona infectada sin protección — manipular la herida sin kit. Fundamentos (5). No se propaga por contacto casual.

**Escalación:** Sin tratamiento antes de cada Descanso Completo, escala un nivel de severidad.

**Duración:** hasta eliminar

**Recuperación:** T.E. Medicina durante Descanso Completo. Una T.E. exitosa reduce la severidad un nivel. Kit Básico (Leve), Kit Avanzado (Moderado), Kit Especializado (Grave).

**Índice Alquímico:** 4 — fácil de identificar; cualquier entrenamiento básico en Medicina o Alquimia reconoce los signos.

| Severidad | Efectos |
| --- | --- |
| **Leve** | Las ranuras de la zona infectada no pueden liberarse con Tratar mientras la infección esté activa, aunque la T.E. de Medicina tenga éxito. La infección debe tratarse primero. |
| **Moderado** | Leve, más: la zona infectada tampoco puede ser Estabilizada — el tejido rechaza la intervención de cierre. |
| **Grave** | Moderado, más: al inicio de cada Descanso Completo sin tratamiento previo, la zona infectada suma 1 ranura ocupada. Si la zona colapsa, aplican las reglas normales de zona colapsada. |

---

## Fiebre de Colapso

*El cuerpo tiene una respuesta para casi todo. Esta lo obliga a pelear dos batallas al mismo tiempo — y ninguna las puede ganar.*

**Aplicación:** Contacto físico sostenido con un portador sintomático — combate cuerpo a cuerpo, atención médica sin protección, agua o alimento compartidos en el mismo recipiente. La T.R. de Infecciones se realiza al terminar la escena de exposición.

**Incubación:** 1 Descanso Completo. El personaje parece en buen estado hasta que aparecen los síntomas sistémicos: escalofríos, temperatura, desorientación leve.

**Contagio:** Desafiante (8)

**Propagación:** Contacto físico con un portador sintomático, incluyendo descanso compartido en espacio cerrado. Desafiante (8). Se propaga fácilmente entre grupos que no separan al infectado.

**Escalación:** Sin tratamiento, escala un nivel de severidad por cada Descanso Completo adicional.

**Duración:** hasta eliminar

**Recuperación:** T.E. Medicina durante Descanso Completo. Una T.E. exitosa reduce la severidad un nivel. Kit Avanzado (Leve y Moderado), Kit Especializado (Grave). El Descanso Completo con T.E. exitosa recupera Fatiga normalmente para ese descanso.

**Índice Alquímico:** 6

| Severidad | Efectos |
| --- | --- |
| **Leve** | El Descanso Completo recupera solo 2 niveles de Fatiga en lugar de 3. |
| **Moderado** | El Descanso Completo recupera solo 1 nivel de Fatiga. |
| **Grave** | El Descanso Completo no recupera Fatiga. El cuerpo no puede metabolizar el estrés mientras la fiebre consume sus recursos. |

---

## Podredumbre Necrótica

*No es que el tejido muera. Es que algo lo reemplaza.*

**Aplicación:** Exposición a criaturas necrotizantes, heridas causadas por garras o mordiscos de portadores activos, o contacto directo con materia orgánica en estado de putrefacción avanzada. La T.R. de Infecciones se realiza inmediatamente tras la exposición.

**Incubación:** 1 Descanso Completo. Sin síntomas visibles. Al manifestarse: decoloración y pérdida local de sensación en la zona de exposición.

**Contagio:** Exigente (14)

**Propagación:** Solo por contacto directo con tejido infectado expuesto — herida abierta, fluidos de la zona afectada. Desafiante (8). No se propaga por contacto casual o proximidad.

**Escalación:** Sin tratamiento, escala un nivel de severidad por cada Descanso Completo adicional.

**Duración:** hasta eliminar

**Recuperación:** T.E. Medicina durante Descanso Completo. Una T.E. exitosa reduce la severidad un nivel. Kit Especializado en todas las severidades. Identificación del agente requiere Entendimiento (Alquimia o Medicina) a dificultad Rigurosa.

**Índice Alquímico:** 9

| Severidad | Efectos |
| --- | --- |
| **Leve** | Las ranuras de todas las zonas heridas del objetivo no pueden liberarse con Tratar mientras la infección esté activa. |
| **Moderado** | Leve, más: al inicio de cada Descanso Completo sin tratamiento previo, la zona de mayor ocupación suma 1 ranura ocupada. Si la zona colapsa, aplican las reglas normales. |
| **Grave** | Moderado, pero la suma de ranura ocurre también al inicio de cada Descanso Corto de 60 minutos sin tratamiento. Si una zona ya está colapsada, la suma pasa a la siguiente zona de mayor ocupación. |
