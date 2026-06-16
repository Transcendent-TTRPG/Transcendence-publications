---
title: "Fórmulas de Tiradas, NR y Hoja de Criatura"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 14
status: draft
canonical: false
tags: [criaturas, fórmulas, tiradas, NR, construcción-encuentros, hoja-criatura, narrador]
related:
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/01-doctrina.md
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/02-zonas.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/
authority_refs:
  - Transcendence-design/docs/system/creatures.md
---

# Fórmulas de Tiradas, NR y Hoja de Criatura

---

## Fórmulas de tiradas

Todas las tiradas de criatura usan el NR como escalador principal. Las características se definen por criatura según su anatomía y rol.

| Tirada | Común | Campeón | Elite |
| --- | --- | --- | --- |
| T.A. | 1d10 + NR + característica | 1d10 + ⌈NR × 1,5⌉ + característica | 1d10 + NR × 2 + característica |
| T.D. | 1d10 + NR + característica | 1d10 + ⌈NR × 1,5⌉ + característica | 1d10 + NR × 2 + característica |
| T.R. | 1d10 + NR + característica | 1d10 + ⌈NR × 1,5⌉ + característica | 1d10 + NR × 2 + característica |
| T.E. | 1d10 + NR + característica | 1d10 + ⌈NR × 1,5⌉ + característica | 1d10 + NR × 2 + característica |
| T.I. | daño × ⌈NR ÷ 3⌉ + característica | daño × ⌈NR ÷ 2⌉ + característica × 2 | daño × NR + característica × 3 |

⌈x⌉ = redondear hacia arriba

Estas son líneas base de calibración. Ajusta por criatura si comportamientos específicos justifican pesos de tirada distintos entre zonas o tipos de ataque.

---

## NR y construcción de encuentros

La categoría define el rango de NR recomendado relativo al NR del grupo (NRg):

| Categoría | Offset de NR | Nivel de amenaza |
| --- | --- | --- |
| Común | NRg + 1 a 2 | Desafío relevante; exige atención |
| Campeón | NRg + 3 a 5 | Amenaza seria; requiere enfoque táctico |
| Elite | NRg + 6 a 10+ | Amenaza existencial; requiere preparación, conocimiento y coordinación |

Estos rangos son puntos de partida. Ajusta según la composición del grupo, la información que tengan sobre la criatura, y el nivel de preparación que hayan podido reunir.

Recuerda: un Común puede tener el mismo NR que un Campeón o un Elite. Lo que diferencia a cada categoría no es el NR, sino el tipo de presión que ejerce en el encuentro.

---

## Hoja de criatura

Las criaturas no usan hoja de personaje. El Narrador trabaja con una ficha compacta que registra solo lo que importa para las tiradas, los ciclos y el comportamiento en combate.

### Cabecera

```
Nombre · NR · Naturaleza · Categoría · Rol
```

### Características

Solo las que la criatura usa en sus tiradas. No todas las características del sistema — solo las relevantes para sus técnicas, ataques y procesos.

```
[Característica]: [valor]
[Característica]: [valor]
...
```

### Zonas

| Zona | Designación | PV | Bloqueo | Al colapsar |
| --- | --- | --- | --- | --- |
| [nombre] | Zona / Núcleo | [valor] | [valor] | [qué pasa] |

### Rasgos

```
[Nombre del rasgo]
  Condición: [cuándo se activa]
  Efecto:    [Ventaja de Ejecución en qué tirada]
```

### Ciclos autónomos

```
[Nombre del ciclo]
  Ritmo:     [costo por activación]
  Efecto:    [qué ocurre al dispararse]
  Ancla:     [zona / ambiental]
```

### Para criaturas Elite

```
Metamorfosis
  Fase [N]: se activa cuando [zona] colapsa
    — [qué cambia: comportamientos, ciclos, entorno]

Apoteosis
  [efecto de la fase final]

Golpe Final
  [condición + acción coordinada requerida]
```

---

## Workflow de diseño

Seguir este orden evita criaturas donde los números existen pero el cuerpo no puede explicar el comportamiento, o donde el comportamiento existe pero no tiene zona que lo sostenga.

1. **Define qué hace la criatura en combate.** Lista todos los comportamientos: tipos de ataque, respuestas defensivas, efectos recurrentes, presencia ambiental.
2. **Identifica la parte del cuerpo que habilita cada comportamiento.** Esto no es sabor opcional — es el trabajo de diseño. Si no puedes identificar una parte del cuerpo para un comportamiento, el comportamiento no está listo para ser escrito.
3. **Asigna cada zona su designación** (Zona o Núcleo) según su función, no su posición anatómica. La garganta de una criatura que respira fuego puede ser Núcleo si todo depende de ella.
4. **Define naturaleza, categoría y rol.** Esto te da el offset de NR, el alcance de ciclos, los multiplicadores de PV y los multiplicadores de Bloqueo.
5. **Aplica las fórmulas de zona.** PV y Bloqueo son derivados, no inventados. Aplica el modificador de cobertura por zona para diferenciar Bloqueo entre zonas blandas y duras.
6. **Escribe las técnicas** ancladas a sus zonas.
7. **Escribe los ciclos autónomos** anclados a sus zonas (biológicos) o como presencia ambiental (ciclos ambientales Elite). Respeta el alcance de la categoría.
8. **Escribe los rasgos.** Para cada rasgo: condición de activación, tirada afectada, cómo puede descubrirla un jugador.
9. **Define las consecuencias del colapso de zona.** Para cada zona: ¿qué comportamiento desaparece? ¿qué ciclo se retira del ATB? Si es Elite, ¿activa una fase de Metamorfosis?
10. **Si es Elite: define las fases de Metamorfosis y la Apoteosis.** Cada fase dispara en un colapso específico. Cada fase cambia algo del encuentro — comportamientos, ciclos, entorno. La Apoteosis y el Golpe Final cierran el encuentro.
