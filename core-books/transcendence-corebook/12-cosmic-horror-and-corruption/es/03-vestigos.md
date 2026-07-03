---
title: "Vestigos"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 12
status: draft
canonical: false
tags: [limbo, vestigo, aflicciones, canal, fatiga-del-patrón, horror-cósmico]
related:
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/01-el-limbo.md
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/02-el-descubrimiento.md
  - core-books/transcendence-corebook/11-ailments/es/03-aflicciones.md
authority_refs:
  - Transcendence-design/docs/system/limbo-manifestations.md
  - Transcendence-design/docs/system/limbo-entities.md
  - Transcendence-design/data/system/ailments.yaml
---

# Vestigos

Una vez que la mutación perceptual está completa, el vestigo puede activarse intencionalmente. El portador ya asimiló la distorsión y sabe cómo forzar al entorno a través del objeto. Lo que no sabe es cuántas veces más podrá hacerlo antes de que el anclaje ceda.

---

## El mecanismo

El vestigo no hace magia de la nada. Es un ecualizador antinatural que toma la física del entorno y la pervierte. Sesga, sincroniza o filtra el proceso físico que ya hay en la escena, siempre apoyado en un medio real: luz, sonido, vibración, calor, presión.

Un vestigo vinculado al sonido no crea sonido donde no hay ninguno. Opera a través del sonido que ya existe en la escena — lo redirige, lo amplifica en una dirección específica, lo confunde en un punto concreto. Si el medio que necesita no está presente, el vestigo no puede activarse.

Esto también define el alcance de lo que un vestigo puede hacer. Su efecto es real y puede ser decisivo — pero siempre es un efecto que la física del entorno podría explicar si alguien no supiera lo que está mirando. No rompe las reglas del mundo físico. Las usa con una precisión que el mundo físico solo no produciría.

El vestigo no espera intención. Cuando el medio que necesita está presente y alguien entra en contacto con el objeto, el Tauma opera — sin importar si el portador sabe lo que tiene, si lo busca deliberadamente, o si lo tomó sin saber qué era. No existen usos voluntarios e involuntarios en ningún sentido mecánico relevante: interactuar con el vestigo, es decir tocarlo, lo activa. El Tauma usa al portador; el portador no usa el Tauma.

---

## El coste de uso

Forzar la lógica del mundo físico desgasta al huésped. Cada uso de un vestigo exige una **T.R. de Aflicción**:

```text
T.R. de Aflicción = 1d10 + Compostura + nivel de competencia en Resistencia a Aflicciones + bonificadores adicionales
```

En caso de fallo, la disrupción avanza y la Intensidad de la Aflicción del portador en el sentido vinculado aumenta en `+1`. Un fallo no impide el uso — el vestigo se activa igual — pero te cuesta cordura y control biológico.

La dificultad de esta T.R. usa la escala estándar de Agravios con el NR del vestigo: **Leve: 8 + NR**, **Moderado: 13 + NR**, **Grave: 17 + NR**. A medida que la Intensidad escala, la siguiente tirada se vuelve más difícil. Para un portador de NR bajo frente a un vestigo de NR alto, el ciclo es casi inevitable: falla la T.R., la Intensidad sube, la siguiente tirada exige aún más. Cuando la Aflicción llega a Grave, el canal desborda hacia otros sentidos u otras aflicciones. No hay bloqueo de acceso — el Tauma no pide permiso — pero las consecuencias de usar un vestigo muy por encima del propio NR se acumulan con rapidez.

La Aflicción acumulada no es solo coste. A medida que la intensidad aumenta, las pistas de cualquier objeto del mismo sentido se vuelven más claras — el canal más cargado percibe más. Lo que el portador pierde en percepción ordinaria, lo redistribuye hacia lo que el Limbo le permite ver.

---

## La fatiga del patrón

La alteración antinatural no es eterna. El patrón de un vestigo tiene un número finito de usos. Ese número no es visible para el portador — no hay contador, no hay señal de advertencia. El patrón se agota de forma impredecible. Un vestigo puede durar tres usos o treinta. El portador no lo sabe mientras no lo vive.

Cuando el patrón se agota, el vestigo no explota ni se transforma. Simplemente pierde su anclaje de forma tan abrupta como un cristal que se quiebra. Sigue siendo el objeto que era — la pluma, la moneda, la vasija — pero el Tauma que lo impregnaba se ha disipado. Si alguien con Resonancia lo sondea ahora, encontrará lo que queda de una huella que ya no tiene fuerza.

La Aflicción que el portador acumuló durante el uso no desaparece con el agotamiento del vestigo. El canal que el cuerpo construyó sigue ahí. Lo que ya no existe es el objeto que lo alimentaba.

---

## Categorías de vestigo

El patrón no tiene una sola resistencia. Depende de qué tan profundo fue el consenso que lo creó: cuántos individuos creyeron en el objeto, durante cuánto tiempo, con cuánta convicción, y si la civilización de origen todavía existe para anclar el Tauma acumulado o si solo queda el eco de una fe muerta sin canal vivo hacia donde fluir.

La categoría de cada vestigo está definida en su propio diseño, junto con su NR. Es una propiedad fija del vestigo que determina dos cosas: la dificultad de las T.R. de Aflicción que genera sobre quienes entran en contacto con él cuando el medio está presente, y la velocidad con que su patrón cede. Esta clasificación no se comunica a los jugadores — forma parte del estado oculto del objeto.

### Tirada de agotamiento

Cada vez que el vestigo se activa — cuando el efecto se manifiesta a través del medio físico presente — el Narrador realiza en secreto una tirada de `1d100`. Si el resultado es igual o superior al **umbral de categoría**, el patrón se agota en ese momento. El portador descubre el agotamiento solo cuando el objeto deja de responder.

### Las cinco categorías

| Categoría | NR | Umbral | Probabilidad por activación | Activaciones promedio |
| --- | --- | --- | --- | --- |
| Fragmentario | 1–2 | 94 | 7 % | ~14 |
| Menor | 3–5 | 91 | 10 % | ~10 |
| Establecido | 6–8 | 88 | 13 % | ~8 |
| Profundo | 9–11 | 85 | 16 % | ~6 |
| Primordial | 12 | 81 | 20 % | ~5 |

**Fragmentario** — El consenso que lo creó fue pequeño o breve. Una comunidad reducida, una devoción de pocos años, una creencia que nunca alcanzó el centro de la cultura. El patrón es real pero delgado: hay poco Tauma que consumir, y por eso las activaciones apenas lo erosionan. Dura muchos usos. Lo que no tiene es profundidad — sus efectos son limitados.

**Menor** — Una comunidad de escala moderada sostuvo esta creencia durante generaciones, aunque nunca fue el eje de su cosmología. El patrón tiene más densidad que el Fragmentario, y cada activación arrastra más. Sigue siendo manejable, pero se gasta con mayor velocidad.

**Establecido** — El objeto era central para una civilización importante en el pico de su poder. Muchas personas, durante mucho tiempo, creyeron que hacía exactamente esto. El patrón es denso y coherente, y cada activación consume una fracción considerable de lo acumulado.

**Profundo** — Civilización antigua en el cénit de su poder, o dos o más culturas que sostuvieron la misma creencia de forma independiente. La convergencia multiplica la impronta. El patrón es intenso y cada activación lo convulsiona desde dentro.

**Primordial** — El consenso fue tan masivo, tan antiguo o tan total que el patrón acumula una densidad casi incomprensible. Esa densidad es exactamente lo que lo agota: cada activación arrastra una porción enorme del depósito acumulado. Los vestigos Primordiales suelen provenir de civilizaciones extintas — sin una fe viva que reponga lo que se consume, el Tauma no se recupera. Son los más devastadores y los más volátiles en igual medida.

### Criterios de asignación

Cuatro factores determinan la categoría de un vestigo:

- **Antigüedad** — ¿Cuánto tiempo duró la creencia antes de que el Tauma respondiera? Una creencia de veinte años produce resultados distintos a una de dos milenios.
- **Escala** — ¿Cuántas personas sostuvieron esta creencia en su momento de mayor difusión? Una aldea no equivale a un imperio.
- **Centralidad** — ¿Era este objeto el eje de la cosmología o un elemento periférico? Los objetos que una cultura consideró sagrados de forma transversal acumulan impronta más rápido que los que fueron importantes solo para un rito específico.
- **Anclaje** — ¿La civilización de origen todavía existe? Si existe, el Tauma sigue teniendo un canal vivo hacia el que fluir. Si está extinta, ese canal está sellado. El patrón no puede dispersarse hacia ningún lado. Solo puede permanecer.

---

## Lo que el vestigo no hace

Un vestigo no le da al portador un poder independiente de él. El portador no "aprende" a hacer lo que el vestigo hacía. Si el objeto se destruye, se pierde o se agota, el portador no retiene esa capacidad — retiene la Aflicción, retiene la percepción expandida que viene con ella, pero no el efecto.

Lo que el vestigo otorga mientras existe es acceso a algo que el portador, por sus propios medios, no puede producir.
