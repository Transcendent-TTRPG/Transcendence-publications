---
title: "Cobertura, Visibilidad y Ocultación"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [cover, visibility, concealment, perception, stealth, combat, environment]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/07-cover-visibility-and-concealment.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-acciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/06-impacto-critico-y-romper-partes.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-desgaste-aguante-fatiga.md
  - core-books/transcendence-corebook/12-gm-toolkit/es/01-condiciones-del-entorno.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/es/01-especializaciones.md
authority_refs:
  - Transcendence-design/docs/system/cover-visibility-concealment.md
  - Transcendence-design/data/system/cover-visibility-concealment.yaml
  - Transcendence-design/docs/system/environmental-conditions.md
  - Transcendence-design/docs/system/roll-types.md
---

# Cobertura, Visibilidad y Ocultación

Cobertura, visibilidad y ocultación resuelven tres problemas distintos de la escena.

La Cobertura es protección física. Algo bloquea, desvía, absorbe o interrumpe una línea de ataque. La Visibilidad define qué tan lejos y con qué claridad se pueden distinguir detalles. La Ocultación define si una criatura está localizada con precisión por un enemigo.

Una criatura puede tener Cobertura sin estar oculta. Puede estar dentro de niebla densa sin que nada detenga un golpe. Puede estar oculta detrás de una barrera aunque el entorno tenga buena luz. La mesa debe resolver cada capa por separado.

---

## Cobertura

La Cobertura es protección física o estructural que interfiere con una línea de ataque.

Niebla, humo y oscuridad no son Cobertura por sí mismos. Reducen Visibilidad y pueden ayudar a ocultarse, pero no detienen un golpe.

| Cobertura | Criterio | Efecto |
| --- | --- | --- |
| Cobertura Ligera | Protege una parte menor del cuerpo o interfiere parcialmente la línea. | -1 a la Tirada de Ataque del atacante. |
| Cobertura Media | Protege una parte importante del cuerpo, con aperturas claras. | -3 a la Tirada de Ataque del atacante. |
| Cobertura Total | No hay línea directa de ataque hacia el objetivo. | No puede ser objetivo de ataques directos. |

### Cobertura Ligera

El objetivo no está completamente expuesto, pero todavía puede atacarse con una línea razonable.

Ejemplos: mueble bajo, baranda, roca pequeña, tronco delgado, borde de una puerta o cobertura que protege aproximadamente un cuarto del cuerpo.

### Cobertura Media

El objetivo está protegido por un obstáculo significativo, pero conserva alguna exposición.

Ejemplos: árbol grueso, roca grande, barricada, ventana, abertura, esquina de muro o cobertura que protege la mitad del cuerpo o más sin cubrirlo todo.

### Cobertura Total

El obstáculo bloquea completamente la línea directa.

Ejemplos: pared sólida, puerta cerrada, trinchera sin exposición, estructura cerrada o masa que cubre por completo al objetivo.

Un objetivo con Cobertura Total puede ser afectado por ataques de área, Técnicas que alteren la ruta de ataque, destrucción del obstáculo, rodeo, elevación, rebote, explosión u otra ficción que permita evitar la línea directa.

---

## Destruir Cobertura

La Cobertura física puede destruirse si el objeto que la produce tiene material, Potencia y Durabilidad.

Para romper Cobertura, usa la regla normal de ruptura.

```text
Potencia Crítica >= Durabilidad del objeto
```

Si la Potencia Crítica es igual o superior a la Durabilidad, la Cobertura se rompe o deja de proteger según su naturaleza.

Si la Potencia Crítica es menor, la Cobertura no se rompe, pero pierde 1 punto de Durabilidad. Los ataques normales no reducen Durabilidad por defecto; debe existir un Intento de ruptura válido, Impacto Crítico, Técnica o regla específica.

---

## Cobertura y Tipos de Ataque

La Cobertura aplica contra ataques cuerpo a cuerpo, ataques a distancia y proyectiles siempre que el objeto interrumpa materialmente la línea del ataque.

Si el atacante está en un ángulo donde la Cobertura ya no bloquea la línea, no aplica. La Cobertura es geométrica y material, no un estado fijo unido al personaje.

### Escudos como Cobertura

Los escudos son la fuente principal de Cobertura portátil.

Un escudo da Cobertura principalmente a la celda o espacio de su portador. Cubrir a otra criatura normalmente requiere una Técnica, una Reacción de escudo o una regla que permita extender esa Cobertura fuera del espacio propio.

La Cobertura otorgada por escudo depende del tamaño del escudo, tamaño del portador, tamaño de la criatura cubierta, ángulo del ataque y capacidad del portador para cargar y controlar el escudo.

### Cobertura y áreas

Contra ataques de área, la Cobertura solo ayuda si el objeto puede interponerse entre la criatura y el origen, dirección o expansión del efecto.

| Situación | Efecto |
| --- | --- |
| La Cobertura bloquea claramente el área. | Aplica Cobertura normal. |
| La Cobertura protege parcialmente contra el área. | Aplica la mitad del penalizador de Cobertura, redondeando hacia abajo. |
| El área rodea, llena o ignora la Cobertura. | La Cobertura no aplica. |

Una barricada puede ayudar contra una explosión frontal. No ayuda contra gas que llena toda la zona o fuego que cae desde arriba.

---

## Visibilidad

La Visibilidad define qué tan lejos y con qué claridad una criatura puede distinguir detalles visuales.

Para medición en tablero:

```text
1 metro = 1 casilla
```

El juego puede usarse con grid o medición flexible. El grid es recomendable cuando hay combate, áreas, Cobertura, posición aproximada o movimiento táctico relevante.

### Rango visual estándar

En condiciones claras, una criatura puede reconocer detalles relevantes hasta 60 metros.

Más allá de ese rango, una acción que dependa de distinguir detalles visuales requiere una Tirada de Especialización de Percepción. El Narrador aumenta la dificultad según distancia, tamaño, movimiento, contraste y condiciones ambientales.

Regla simple:

```text
+1 Nivel de Referencia por cada 10 metros más allá del rango visual efectivo
```

No uses incrementos de 2 metros. Producen demasiado conteo en mesa y no aportan decisiones útiles.

---

## Rangos de Visibilidad Reducida

| Condición | Intensidad | Rango visual efectivo |
| --- | --- | ---: |
| Lluvia | Ligera | 24 m |
| Lluvia | Intensa | 15 m |
| Lluvia | Tormenta | 8 m |
| Nieve | Ligera | 24 m |
| Nieve | Intensa | 15 m |
| Nieve | Tormenta de nieve | 8 m |
| Niebla | Ligera | 20 m |
| Niebla | Densa | 10 m |
| Niebla | Espesa | 5 m |
| Humo | Leve | 20 m |
| Humo | Denso | 5 m |
| Humo | Asfixiante | 2 m |
| Polvo o arena | Leve | 25 m |
| Polvo o arena | Moderado | 12 m |
| Polvo o arena | Tormenta | 5 m |
| Oscuridad absoluta | Sin fuente de luz | 0 m |
| Oscuridad extranatural | Activa | 0 m, salvo contramedida válida |

Estos valores son guías de referencia. Si la condición ya está representada como entorno Moderado, Severo, Desastroso o Extremo, usa la severidad del entorno como autoridad principal.

---

## Fuentes de Luz

Las fuentes de luz establecen un rango visual efectivo cuando el entorno no tiene iluminación suficiente.

| Fuente | Rango claro | En condición visual densa |
| --- | ---: | ---: |
| Vela | 2 m | 1 m |
| Antorcha | 4 m | 2 m |
| Lámpara de aceite | 6 m | 3 m |

Una fuente de luz no elimina humo, niebla, polvo ni Oscuridad extranatural por sí sola. Solo permite ver dentro del rango que todavía pueda atravesar.

### Oscuridad absoluta y Oscuridad extranatural

La Oscuridad absoluta ocurre cuando no hay luz natural, artificial ni reflejada suficiente para ver. En esas condiciones, el rango visual es 0 m.

La Oscuridad extranatural también reduce el rango visual a 0 m, pero no se resuelve con una fuente de luz ordinaria. La Oscuridad extranatural asociada al elemento Oscuridad bloquea luz natural y fuentes comunes de iluminación.

Para contrarrestarla se necesita una fuente compatible: luz extranatural asociada al elemento Luz, artefacto, Técnica, condición ambiental opuesta o regla específica.

---

## Percepción y Sentidos

Percepción no significa solo visión. Representa la capacidad de localizar, distinguir o interpretar señales sensoriales.

Un personaje puede usar Percepción para ver, escuchar, oler, sentir vibración, reconocer contacto, leer señales químicas, usar ecolocalización u otro sentido especial si lo posee.

Los sentidos especiales usan la misma estructura de Percepción salvo que una regla diga otra cosa. Una criatura con un sentido especial puede tener bonificadores adicionales y no queda bloqueada por efectos que no interfieran con ese sentido.

Ejemplo: una criatura que rastrea por olor puede ignorar Oscuridad visual para localizar un objetivo, pero puede sufrir penalizadores por viento, agua, humo químico o una Técnica que altere olores.

---

## Combate sin Visión

Una criatura que no puede ver a su objetivo no pierde automáticamente todas sus competencias.

En su lugar:

- no puede elegir con precisión objetivos que no haya localizado;
- no puede usar Técnicas que requieran lectura visual clara;
- puede atacar una posición aproximada con penalización o dificultad aumentada;
- puede defenderse peor contra amenazas que no puede leer;
- puede usar otros sentidos si son relevantes.

| Situación | Efecto |
| --- | --- |
| Objetivo localizado por cualquier sentido relevante. | Puede ser objetivo; aplica penalización o Nivel de Referencia solo si la señal es débil, indirecta o difícil de interpretar. |
| Objetivo no localizado. | No puede ser objetivo de ataque directo. |

La Tirada de Impacto no pierde todos sus bonos por falta de visión. Si el ataque conecta, el Impacto se resuelve normalmente salvo que una regla específica diga lo contrario.

---

## Ocultación

La Ocultación es un estado táctico: una criatura no está localizada con precisión por uno o más enemigos.

No es invisibilidad, no es inmunidad y no borra evidencia física. Significa que el enemigo no sabe exactamente dónde está la criatura o no puede fijarla como objetivo directo.

### Ocultarse

Ocultarse es una acción base cuando se realiza bajo presión.

| Acción | Ritmo | Desgaste | Tirada |
| --- | ---: | ---: | --- |
| Ocultarse | 5 | 1 | Tirada de Especialización apropiada contra dificultad del entorno o Percepción enemiga |

Fuera de una escena hostil, Ocultarse no necesita Costo de ritmo. El Narrador solo pide la tirada si hay riesgo, oposición o consecuencia.

Una criatura puede intentar ocultarse si cumple al menos una de estas condiciones:

- tiene Cobertura Media o Cobertura Total;
- está fuera del rango visual efectivo de los enemigos relevantes;
- está dentro de una condición de Visibilidad reducida que pueda ocultar su posición;
- cuenta con una Técnica, rasgo, artefacto o preparación que permita Ocultación.

Además, ningún enemigo relevante debe tenerla localizada claramente por un sentido aplicable. No basta con querer desaparecer mientras alguien la ve, oye, huele o percibe con claridad.

Si un enemigo la tiene localizada sin obstrucción, la criatura debe crear primero una oportunidad real: romper línea de visión, entrar en Cobertura, entrar en humo, niebla, Oscuridad, vegetación, multitud o ruido suficiente, usar una distracción, moverse fuera del rango efectivo del sentido que la localiza, o usar una Técnica, rasgo, artefacto o preparación que permita ocultarse aun bajo observación.

### Tirada para ocultarse

La criatura realiza una Tirada de Especialización apropiada contra la dificultad del entorno o contra la Percepción de los enemigos, según la escena.

Especializaciones típicas:

- Sigilo para ocultarse por silencio, control corporal y posición;
- Supervivencia para ocultarse en terreno natural, vegetación, clima o rastros;
- otra especialización si un rasgo, Técnica o artefacto lo justifica.

La Ocultación se registra por enemigo o por grupo de enemigos. Un personaje puede estar oculto para un guardia, pero no para otro que lo vio entrar.

---

## Efectos de la Ocultación

Mientras una criatura esté oculta para un enemigo:

- ese enemigo no puede elegirla como objetivo de ataques directos de “una criatura”;
- puede atacar un área o posición sospechada si tiene una razón para hacerlo;
- puede buscarla con Percepción, Técnica o acción específica de escena;
- puede reaccionar a señales obvias, ruido, contacto o cambios del entorno.

La Ocultación no protege contra efectos de área que cubran la posición real.

### Atacar desde Ocultación

Atacar desde Ocultación puede dar una ventaja de apertura si el objetivo no reacciona a tiempo.

Antes de resolver el ataque, las criaturas relevantes dentro de 10 metros pueden intentar detectar la acción si tienen un sentido aplicable. Usa Tirada de Especialización de Percepción contra la Ocultación activa o la dificultad del entorno.

Una criatura fuera de 10 metros solo puede intentar esta detección si tiene un sentido especial, Técnica, preparación o posición que justifique reaccionar a esa señal.

| Resultado de Percepción | Efecto |
| --- | --- |
| Falla | El ataque conserva ventaja de apertura. |
| Tiene éxito | Detecta la acción a tiempo; el atacante no obtiene ventaja de apertura contra esa criatura. |

Si el ataque conserva ventaja de apertura, obtiene +3 a la Tirada de Ataque contra objetivos que no detectaron la acción a tiempo.

Atacar desde Ocultación siempre compromete la Ocultación, incluso si el ataque falla. Después del ataque, resuelve posición aproximada o detección según la escena.

---

## Mantener y Perder Ocultación

La Ocultación se mantiene mientras la criatura no dé una señal suficiente para localizarla.

Acciones que comprometen la Ocultación:

- atacar cuerpo a cuerpo;
- atacar a distancia;
- moverse entre coberturas;
- correr;
- hablar fuerte;
- manipular un objeto visible o ruidoso;
- interactuar con una fuente de luz;
- cambiar de posición en un entorno silencioso.

Comprometer la Ocultación no significa revelar automáticamente la posición exacta. Significa que hay una señal suficiente para que enemigos cercanos intenten localizarla.

Cuando una criatura compromete su Ocultación, las criaturas relevantes dentro de 10 metros pueden intentar una Tirada de Especialización de Percepción si tienen un sentido aplicable. Criaturas fuera de 10 metros necesitan un sentido especial, Técnica, preparación o circunstancia que justifique la detección.

Decir “creo que está allí” o señalar una posición sospechada no revela por sí mismo a una criatura oculta. Comunicar una sospecha permite coordinar ataques al área o dirigir búsqueda, pero no elimina penalizadores ni convierte la posición en exacta.

---

## Posición Aproximada Incierta

Una acción puede revelar posición aproximada sin revelar posición exacta.

Ejemplos: una flecha sale desde una zona de arbustos, una piedra cae desde una cornisa, una voz se oye desde el oeste o una sombra cruza detrás de humo.

La posición aproximada incierta existe para que el detector reciba una pista jugable sin saber si acertó. El jugador debe saber que su personaje percibió algo, pero no si esa percepción fue correcta.

### Jugador oculto, criatura detecta

Si el jugador es quien está oculto:

1. El jugador tira la misma especialización que usó para ocultarse, o la especialización apropiada si la ficción cambió.
2. El Narrador tira Percepción por la criatura que intenta detectarlo.
3. Si Percepción supera la Ocultación, la criatura localiza la posición real del personaje.
4. Si Percepción no supera la Ocultación, el Narrador tira 1d8 y la criatura actúa hacia la posición falsa indicada por esa dirección, si su comportamiento lo justifica.

### Criatura oculta, jugador detecta

Si una criatura es quien está oculta:

1. El jugador tira Percepción.
2. El Narrador tira en secreto la Ocultación de la criatura.
3. El Narrador también tira 1d8 en secreto al mismo tiempo, declarando solo que está resolviendo Ocultación.
4. Si la Percepción del jugador supera la Ocultación, el Narrador señala la posición real.
5. Si la Percepción del jugador no supera la Ocultación, el Narrador señala la posición falsa indicada por el 1d8.

El Narrador no declara si la tirada del jugador tuvo éxito o falló. El punto mostrado es lo que el personaje cree haber percibido.

Los empates favorecen a la criatura oculta.

| 1d8 | Dirección |
| --- | --- |
| 1 | Noroeste |
| 2 | Norte |
| 3 | Noreste |
| 4 | Oeste |
| 5 | Este |
| 6 | Suroeste |
| 7 | Sur |
| 8 | Sureste |

En grid, el resultado del 1d8 corresponde por defecto a la casilla adyacente a la posición real de la criatura oculta en esa dirección. Si la criatura ocupa más de una casilla, usa la casilla adyacente al borde de su espacio en esa dirección.

Si esa casilla no es válida, está bloqueada o no es plausible, usa la Cobertura, celda o área plausible más cercana en esa misma dirección. En juego sin grid, usa una zona cercana creíble en esa dirección.

---

## Detectar Criaturas Ocultas

No existe una acción universal separada llamada Buscar. Buscar se resuelve como una Tirada de Especialización de Percepción, una Técnica o una acción específica de la escena si el Narrador la exige por tiempo, posición o presión.

En un éxito, la criatura detecta la posición para sí misma. Puede comunicar una sospecha o dirección si la escena permite hablar, señalar o coordinarse, pero esa comunicación no revela automáticamente a la criatura para todos.

La detección provocada ocurre cuando una criatura oculta produce una señal suficiente para que otros tengan oportunidad de notarla. El Narrador puede pedir Percepción, usar un umbral fijo o revelar información parcial si la señal es obvia.

La detección provocada no reemplaza el uso deliberado de Percepción o Técnicas. Sirve para resolver señales creadas por la criatura oculta, no para escanear gratis todo el entorno.

---

## Límites de Balance

La Ocultación necesita límites porque puede volverse demasiado fuerte si impide demasiadas respuestas.

Reglas de seguridad:

- Ocultarse requiere una razón física, ambiental o técnica;
- la Ocultación se mide por enemigo, no como estado universal;
- oculto no significa intocable;
- los efectos de área siguen funcionando si cubren la posición real;
- atacar suele revelar o poner en riesgo la Ocultación;
- la Percepción especializada puede acelerar detección, pero no debe borrar todo el juego de señales;
- criaturas con sentidos no visuales pueden ignorar o reducir Ocultación visual;
- habilidades, Técnicas o criaturas pueden declarar que ignoran Ocultación bajo condiciones específicas.
