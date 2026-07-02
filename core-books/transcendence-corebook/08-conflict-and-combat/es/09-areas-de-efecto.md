---
title: "Áreas de Efecto"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [combat, grid, area, cone, radius, line]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/es/07-cobertura-visibilidad-y-ocultacion.md
---

# Áreas de Efecto

Algunas técnicas, armas naturales y detonaciones ambientales no apuntan a una criatura específica mediante una Tirada de Ataque tradicional, sino que proyectan su fuerza sobre una zona completa. Todas las criaturas, y en algunos casos las estructuras o elementos del entorno, que se encuentren dentro de esa zona se ven afectadas.

Transcendence contempla tres formas geométricas principales para las áreas de efecto. Dado que el juego puede resolverse tanto en un grid táctico como en el teatro de la mente, la regla prioriza la lógica física de la expansión.

## Origen y Expansión

Toda área de efecto tiene un **origen**. Usualmente es la casilla que ocupa el atacante, pero en técnicas arrojadizas o explosiones remotas, el origen es la casilla o punto de detonación en el espacio. Las áreas se expanden desde ese punto ignorando las coberturas menores, pero son bloqueadas por coberturas totales (como un muro de contención sin fisuras) a menos que la técnica indique específicamente que atraviesa materiales o los destruye mediante Potencia.

---

## 1. Área Circular (Radio)

El efecto se expande en todas las direcciones desde el punto de origen. En descripciones de reglas y técnicas, su área se indica como `Circular X m` (por ejemplo, *Circular 8 m*).

**Resolución en Grid:**
Para determinar qué casillas cubre una explosión circular, mide la distancia máxima `X` en líneas rectas (ortogonalmente) desde el centro. En las direcciones diagonales, el efecto se expande la mitad de esa distancia real en casillas. El resultado es un área que se aproxima a un círculo táctico, cubriendo el centro y difuminándose equitativamente hacia los bordes.

*Si una criatura tiene al menos la mitad de su base o casilla dentro del área demarcada, se considera afectada.*

---

## 2. Área Cónica (Cono)

El efecto estalla desde el origen en una proyección angular que se ensancha a medida que avanza. Un cono siempre se dispara en una dirección declarada por el atacante.

**Resolución en Grid:**
La regla fundamental del cono es que **su ancho máximo en el punto más lejano es igual a su longitud total.**
Si disparas un cono de 5 metros:
- Inicia en la casilla donde se aplica el efecto con 1 metro de ancho.
- Por cada metro (casilla) que avanza hacia adelante, se expande 1 metro hacia los lados simétricamente.
- Cuando alcanza su límite de 5 metros de longitud, su base o frente de impacto tiene exactamente 5 metros de ancho.
Esto forma un triángulo perfecto en el mapa táctico. Cualquier criatura ubicada parcial o totalmente dentro de ese cono, o en la línea diagonal que lo delimita, sufre el efecto.

---

## 3. Área Lineal (Línea)

La forma más directa y concentrada. El efecto viaja en línea recta desde el punto de origen hacia una dirección declarada. Su área se define por su longitud máxima.

**Resolución en Grid:**
A menos que la técnica especifique un grosor distinto, una línea tiene **1 metro de ancho** (1 casilla). Atraviesa directamente las casillas en la trayectoria indicada hasta alcanzar su longitud máxima o chocar contra una cobertura total invulnerable que absorba el impacto. Si disparas en diagonal, la línea afecta cualquier casilla por la que la trayectoria recta cruce el centro.

---

## Otros Tipos de Alcance y Área

- **1 Criatura u Objeto:** Técnicas de precisión clínica. No tienen área.
- **Tú:** El efecto recae estrictamente sobre el cuerpo, armas o mente de quien activa la técnica.
- **Rango Sensorial:** Utilizado mayormente para rastreo e investigación. El área no tiene un límite duro en metros, sino que el efecto se expande hasta el límite natural o físico de tu percepción (visión, olfato, audición) en ese entorno específico antes de ser bloqueado por el terreno.
