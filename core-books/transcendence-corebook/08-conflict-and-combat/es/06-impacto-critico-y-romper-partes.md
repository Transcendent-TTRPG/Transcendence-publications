---
title: "Impacto Crítico y Romper Partes"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [critical-impact, breaking-parts, potency, durability, equipment, creature-parts, combat]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/06-critical-impact-and-breaking-parts.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/05-heridas-y-dano.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-acciones.md
  - core-books/transcendence-corebook/03-core-rules/es/02-rolling-system-and-competencies.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/README.md
  - core-books/transcendence-corebook/13-adversaries-and-bestiary/es/README.md
authority_refs:
  - Transcendence-design/docs/system/wounds-and-damage.md
  - Transcendence-design/data/system/wounds-and-damage.yaml
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
  - Transcendence-design/data/system/equipment.yaml
section_modes:
  - heading: "Ejemplo: dado crítico designado"
    writing_mode: example
  - heading: "Ejemplo: ruptura fallida"
    writing_mode: example
  - heading: "Ejemplo: parte de criatura"
    writing_mode: example
---

# Impacto Crítico y Romper Partes

El Impacto Crítico define cuándo un golpe encontró una entrada excepcional. Romper Partes define qué puede hacer ese golpe contra una estructura concreta: una pieza de armadura, un escudo, un arma, una mandíbula, una placa natural o cualquier parte que el encuentro haya vuelto relevante.

Este sistema no convierte todos los críticos en daño adicional automático. Separa tres preguntas distintas: si el golpe fue crítico, si existe un objetivo rompible válido y si la Potencia del ataque supera la Durabilidad del objetivo.

---

## Impacto Crítico

Un Impacto Crítico ocurre cuando el dado crítico designado de la Tirada de Impacto muestra su valor máximo.

Cuando una Tirada de Impacto usa varios dados, el atacante designa un dado antes de tirar. En mesa, se usa un dado de color distinto. En una herramienta digital, se etiqueta uno de los dados como crítico. Solo ese dado puede validar Impacto Crítico.

| Dado de Impacto | Resultado crítico |
| --- | ---: |
| d4 | 4 |
| d6 | 6 |
| d8 | 8 |
| d10 | 10 |
| d12 | 12 |

Los demás dados de la Tirada de Impacto suman daño o presión normalmente. No validan crítico por sí solos, aunque muestren su valor máximo.

### Ejemplo: dado crítico designado

Un personaje tira `3d8` de Impacto. Antes de tirar, declara que el dado rojo es el dado crítico. Si el dado rojo muestra `8`, hay Impacto Crítico. Si los otros dos dados muestran `8` y el dado rojo no, el Impacto aumenta por sus valores, pero no hay Impacto Crítico.

---

## Qué Permite un Impacto Crítico

Un Impacto Crítico permite acceder a opciones críticas definidas por el arma, Técnica, objetivo o encuentro.

Por defecto, puede permitir:

- intentar Romper Partes contra un objetivo rompible declarado;
- aplicar daño crítico si el modelo del PNJ lo define;
- activar una Técnica que requiera Impacto Crítico;
- aplicar una consecuencia física si el ataque o la parte la declaran.

Un Impacto Crítico no fuerza una Herida Crítica contra personajes jugadores por sí mismo. La severidad de la herida sigue dependiendo de la relación entre Impacto y Bloqueo, salvo que una regla específica aumente esa severidad.

---

## Declarar un Objetivo Rompible

Para intentar Romper Partes, el atacante debe declarar un objetivo rompible antes de resolver la ruptura. Algunas Técnicas pueden exigir que esa declaración ocurra antes de la Tirada de Ataque o antes de la Tirada de Impacto.

Un objetivo rompible debe cumplir tres condiciones:

1. El ataque puede alcanzarlo.
2. La superficie puede romperse, deshabilitarse o quedar inutilizada por ese tipo de fuerza.
3. La escena, criatura, equipo o Técnica reconoce esa parte como relevante.

Objetivos válidos pueden incluir:

- arma;
- escudo;
- pieza de armadura;
- objeto sostenido o portado;
- mandíbula;
- cuerno;
- caparazón;
- ala;
- cola;
- extremidad;
- articulación;
- placa natural;
- punto vital;
- parte destructible definida por el encuentro.

Tejido blando ordinario no se trata como estructura rompible por defecto. Puede ser objetivo de daño, herida o Agravio, pero no de Romper Partes, salvo que la criatura tenga esa zona definida como estructura, punto vital o parte destructible.

---

## Potencia Crítica

La Potencia Crítica mide si el golpe puede romper la estructura declarada.

```text
Potencia Crítica = Potencia base x Multiplicador de Potencia
```

La Potencia base proviene del material, construcción o perfil del arma. El Multiplicador de Potencia proviene del tipo de arma.

| Tipo de arma | Multiplicador | Lectura de ruptura |
| --- | ---: | --- |
| Lanzas | 80% | Presión concentrada en punto. Mejor contra aberturas que contra masa rígida. |
| Hachas | 120% | Corte pesado que abre material y compromete bordes resistentes. |
| Mazas | 150% | Impacto contundente contra armadura, hueso, placa y estructura dura. |
| Hojas largas | 100% | Balance entre corte amplio y transmisión estable. |
| Dagas | 50% | Precisión alta, baja ruptura contra estructuras resistentes. |
| Hojas cortas | 75% | Corte rápido con ruptura moderada. |
| Armas arrojadizas | 40% | Contacto preciso, poca masa para ruptura sostenida. |
| Armas a distancia | 60% | Perforación o impacto a distancia con ruptura limitada. |
| Armas flexibles | 30% | Control y desbalance más que destrucción material directa. |

Los valores concretos de Potencia base pertenecen al catálogo de armas, materiales y partes de criatura. Esta sección define cómo se usan, no qué valor tiene cada material.

---

## Resolver la Ruptura

Cuando existe un intento válido de ruptura, compara Potencia Crítica contra Durabilidad.

```text
Potencia Crítica >= Durabilidad del objetivo
```

| Comparación | Resultado |
| --- | --- |
| Potencia Crítica >= Durabilidad | El objetivo se rompe, se deshabilita o queda inutilizado. |
| Potencia Crítica < Durabilidad | El objetivo no se rompe y pierde 1 punto de Durabilidad. |

La pérdida de Durabilidad solo ocurre durante un intento válido de ruptura. Un ataque normal no reduce Durabilidad por defecto.

Un intento válido puede surgir por:

- Impacto Crítico contra un objetivo rompible declarado;
- Técnica que permita romper sin Impacto Crítico;
- Técnica que amplíe el rango de validación de ruptura;
- regla específica de arma, criatura, objeto o escena.

### Ejemplo: ruptura fallida

Un atacante logra Impacto Crítico e intenta romper un escudo con Durabilidad `9`. Su Potencia Crítica final es `7`. El escudo no se rompe, pero pierde `1` punto de Durabilidad y queda en `8`. Su Bloqueo no cambia por esa pérdida. El escudo sigue funcionando hasta romperse.

---

## Equipo Roto

Una pieza de equipo rota deja de aportar la función que dependía de su integridad.

Si una armadura, escudo o protección aportaba Bloqueo, deja de aportar ese Bloqueo hasta ser reparada o reemplazada. Si un arma se rompe, no puede usarse para ataques normales ni Técnicas que requieran esa arma, salvo que una regla permita usarla en estado dañado.

La pérdida de Durabilidad no reduce Bloqueo de forma gradual. La pieza funciona hasta romperse. Esto evita recalcular valores menores después de cada golpe y mantiene la mesa enfocada en el momento de ruptura.

---

## Partes de Criatura

Una parte de criatura puede tener Tirada de Defensa, HP, Bloqueo, Potencia, Durabilidad y habilidades vinculadas.

Romper una parte no solo reduce números. Cambia qué puede hacer la criatura. Una mandíbula rota puede impedir un aliento. Un ala rota puede impedir vuelo. Una placa rota puede abrir un punto vulnerable. Un cuerno roto puede terminar una señal de mando.

El bloque del enemigo debe indicar qué partes existen, qué valores tienen y qué habilidades dependen de ellas. Las criaturas importantes deberían organizarse en cinco lugares principales para que la mesa pueda leerlas sin perderse en anatomía excesiva.

### Ejemplo: parte de criatura

Un lobo de hielo tiene `Mandíbula` como parte rompible. Esa parte tiene Durabilidad propia y sostiene la habilidad `Aliento Helado`. Si los personajes rompen la Mandíbula, el lobo no puede usar `Aliento Helado` mientras esa parte siga rota, aunque el resto de la criatura conserve HP.

---

## Técnicas y Ruptura

Las Técnicas pueden modificar la relación normal entre crítico y ruptura.

Una Técnica puede:

- permitir un intento de ruptura sin Impacto Crítico;
- ampliar los resultados del dado crítico que validan ruptura;
- aumentar Potencia;
- ignorar parte de la Durabilidad;
- declarar como rompible una parte que normalmente no lo sería;
- aplicar una consecuencia adicional si la ruptura ocurre.

Una Técnica debe decir exactamente cuál de esas cosas permite. Si solo aumenta daño, no permite ruptura por sí misma. Si solo amplía validación de ruptura, no aumenta Potencia. Si declara una parte nueva como objetivo, todavía debe existir una forma creíble de alcanzarla.

---

## Orden de Resolución

Cuando un ataque puede generar ruptura, usa este orden:

1. Declarar ataque y objetivo normal.
2. Declarar objetivo rompible si la regla o Técnica lo exige.
3. Resolver Tirada de Ataque contra Tirada de Defensa.
4. Si el ataque falla, no hay ruptura.
5. Si el ataque conecta, realizar Tirada de Impacto.
6. Verificar si el dado crítico designado valida Impacto Crítico o si una Técnica permite ruptura de otra forma.
7. Calcular Potencia Crítica.
8. Comparar Potencia Crítica contra Durabilidad.
9. Aplicar ruptura o pérdida de 1 Durabilidad.
10. Resolver daño, herida, HP, cambio de fase o consecuencia adicional según el objetivo.

Si una regla altera este orden, debe decirlo. Una Técnica reactiva, una trampa, una criatura o una parte de jefe pueden insertar pasos propios, pero la mesa siempre debe saber cuándo se declaró el objetivo rompible y cuándo se valida la ruptura.

---

## Límites

Un ataque no rompe cualquier cosa solo porque fue crítico.

El objetivo debe ser alcanzable, materialmente afectable y relevante para la escena. Un arma ligera puede encontrar críticos con frecuencia, pero fallar contra Durabilidad alta. Un arma pesada puede romper estructuras duras, pero no hacer el trabajo fino de una daga. La elección del arma importa porque la ruptura no mide la misma superficie que el daño.

Las reglas de extracción de recursos no se resuelven aquí. Si una parte rota pierde valor como material, trofeo o muestra, se define en la sección de extracción.
