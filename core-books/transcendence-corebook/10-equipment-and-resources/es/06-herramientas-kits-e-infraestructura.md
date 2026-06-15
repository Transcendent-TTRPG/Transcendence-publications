---
title: "Herramientas, Kits e Infraestructura"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 10
status: draft
canonical: false
tags: [herramientas, kits, planos, ingeniería, infraestructura, fabricación, criaturas-gigantes]
related:
  - core-books/transcendence-corebook/10-equipment-and-resources/es/01-materiales.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/02-extraccion-y-conservacion.md
  - core-books/transcendence-corebook/10-equipment-and-resources/es/03-fabricacion-equipo.md
authority_refs:
  - Transcendence-design/docs/system/materials-and-fabrication.md
  - Transcendence-design/data/system/materials-and-fabrication.yaml
---

# Herramientas, Kits e Infraestructura

La especialización **Ingeniería** produce los instrumentos que hacen posible el trabajo de todas las demás especializaciones. No fabrica armas ni elixires — fabrica las herramientas y sistemas necesarios para que otros las fabriquen, extraigan o combatan.

El dominio de Ingeniería abarca cuatro categorías de producción:

- **Herramientas y kits** para todas las especializaciones: Herrería, Sastrería, Alquimia, Joyería, Medicina, Minería, Herboristería, e Ingeniería misma.
- **Arneses y equipo de monta** para criaturas domesticadas o capturadas — desde monturas de tamaño mediano hasta sistemas de fijación para bestias enormes.
- **Herramientas de exploración** — equipamiento para terreno difícil, espeleología, escalada, navegación y supervivencia en entornos hostiles.
- **Equipo de operación en criaturas de escala gigantesca** — sistemas de movimiento, anclaje y trabajo sobre bestias de tamaño gigantesco o colosal, donde el cuerpo de la criatura es el terreno.

---

## Planos

Un Plano es el documento que define la estructura, materiales y proceso de fabricación de una herramienta, kit o instalación. Sin él no es posible comenzar la producción.

Los Planos los crea y los usa la especialización Ingeniería. Como los Diseños de equipo, un Plano no caduca y puede usarse para fabricar múltiples copias del mismo objeto.

### Costo de adquisición del Plano

El costo de un Plano tiene dos componentes:

| Componente | Qué representa |
| --- | --- |
| **Complejidad** | La dificultad de diseño e instrucción del objeto |
| **Disponibilidad** | El acceso al conocimiento técnico específico |

#### Costo por complejidad

| Complejidad | Costo base | Dificultad de fabricación |
| --- | --- | --- |
| Simple | 50 S | Desafiante |
| Complejo | 200 S | Exigente |
| Avanzado | 600 S | Extremo |

#### Recargo por disponibilidad

| Disponibilidad del plano | Recargo |
| --- | --- |
| General | +0 S |
| Limitada | +100 S |
| Especializada | +200 S |
| Rara | +300 S |
| Singular | +400 S |

**Costo total del Plano = Costo por complejidad + Recargo por disponibilidad.**

Ejemplo: Un Plano de complejidad compleja y disponibilidad especializada cuesta 200 + 200 = **400 S**.

---

## Proceso de fabricación

Para fabricar cualquier herramienta o kit se necesita:

1. **Un Plano** del objeto a fabricar.
2. **Los materiales** en los tipos y cantidades especificados.
3. **La especialización Ingeniería** al rango suficiente para la complejidad del Plano.

Cuando el personaje declara una sesión de fabricación:

- Realiza una tirada de **Ingeniería** al inicio. La dificultad la determina la complejidad del Plano.
- Si la tirada **falla**: el tiempo se consume sin avance.
- Si la tirada **tiene éxito**: el personaje trabaja durante las horas requeridas y produce el objeto.

### Tiempo de fabricación

El tiempo de fabricación de una herramienta o kit se calcula con la siguiente fórmula:

> **Horas = Peso del objeto terminado (kg) × Grado máximo de los materiales × Factor de complejidad**

| Complejidad | Factor |
| --- | --- |
| Simple | × 1 |
| Complejo | × 1,5 |
| Avanzado | × 2 |

El "Grado máximo" es el grado más alto entre todos los materiales que componen el objeto.

**Ejemplo:** Un Alambique Alquímico pesa 10 kg, requiere acero y vidrio de grado 3, y tiene complejidad compleja: 10 × 3 × 1,5 = **45 horas**.

**Ejemplo:** Un Kit de Costura pesa 2 kg, requiere acero y algodón de grado 1, y tiene complejidad simple: 2 × 1 × 1 = **2 horas**.

---

## Catálogo de Planos

A continuación se presentan herramientas y kits representativos organizados por especialización de destino. El costo total listado incluye materiales y labor; el costo del Plano es adicional y se paga una sola vez.

---

### Herrería

| Herramienta | Complejidad | Peso | Materiales principales | Costo total (mat + labor) | Disponibilidad |
| --- | --- | --- | --- | --- | --- |
| Martillo de Forja | Simple | 2,5 kg | Acero (2 kg, grado 3), Roble (1 kg, grado 3) | 350 S | General |
| Tenazas | Simple | 3,5 kg | Acero (4 kg, grado 2) | 400 S | General |
| Molde de Fundición | Complejo | 20 kg | Piedra (10 kg, grado 3), Roca (10 kg, grado 3) | 500 S | Limitada |
| Yunke | Simple | 150 kg | Acero (150 kg, grado 1) | 5.100 S | Limitada |
| Forja Tradicional | Complejo | 500 kg | Piedra (250 kg, grado 1), Roca (250 kg, grado 1) | 4.000 S | Especializada |

---

### Sastrería

| Herramienta | Complejidad | Peso | Materiales principales | Costo total (mat + labor) | Disponibilidad |
| --- | --- | --- | --- | --- | --- |
| Kit de Costura | Simple | 2 kg | Acero (2 kg, grado 1), Algodón (1 kg, grado 1) | 100 S | General |
| Kit de Tintes y Brochas | Simple | 1,5 kg | Pino (1 kg, grado 1), Lana (1 kg, grado 1), Algodón (1 kg, grado 1) | 200 S | General |
| Mesa de Corte | Complejo | 15 kg | Ébano (15 kg, grado 2) | 800 S | Limitada |
| Prensa de Cuero | Avanzado | 25 kg | Acero (25 kg, grado 1) | 1.000 S | Especializada |

---

### Alquimia

| Herramienta | Complejidad | Peso | Materiales principales | Costo total (mat + labor) | Disponibilidad |
| --- | --- | --- | --- | --- | --- |
| Mortero y Maja | Simple | 3 kg | Cuarzo (3 kg, grado 3) | 320 S | General |
| Balanza de Precisión | Simple | 2 kg | Acero (3 kg, grado 3), Vidrio (2 kg, grado 3) | 450 S | General |
| Kit de Calderos | Complejo | 5 kg | Cromo (4 kg, grado 1), Vidrio (2 kg, grado 1) | 300 S | Limitada |
| Alambique Alquímico | Complejo | 10 kg | Acero (8 kg, grado 3), Vidrio (2 kg, grado 3) | 1.000 S | Limitada |

---

### Joyería

| Herramienta | Complejidad | Peso | Materiales principales | Costo total (mat + labor) | Disponibilidad |
| --- | --- | --- | --- | --- | --- |
| Kit de Orfebrería | Complejo | 4 kg | Acero (3 kg, grado 1), Cromo (2 kg, grado 1) | 400 S | Limitada |
| Lupa y Tornillo de Banco | Complejo | 2 kg | Cromo (2 kg, grado 3), Cristal (2 kg, grado 3) | 600 S | Limitada |
| Horno de Joyería | Complejo | 30 kg | Acero (25 kg, grado 2), Cromo (5 kg, grado 2) | 2.700 S | Limitada |

---

### Ingeniería (herramientas de trabajo)

| Herramienta | Complejidad | Peso | Materiales principales | Costo total (mat + labor) | Disponibilidad |
| --- | --- | --- | --- | --- | --- |
| Herramientas de Precisión | Complejo | 5 kg | Cromo (3 kg, grado 2), Acero (2 kg, grado 2), Cristal (2 kg, grado 2) | 1.200 S | Especializada |
| Herramientas Mecánicas | Complejo | 12 kg | Cromo (6 kg, grado 2), Acero (4 kg, grado 2), Cobre (2 kg, grado 2) | 1.000 S | Especializada |

---

## Arneses y equipo de monta

Los arneses y equipos de monta son sistemas fabricados por Ingeniería para controlar, transportar o trabajar con criaturas capturadas o domesticadas. No son herramientas de uso personal — son sistemas diseñados para criaturas específicas.

El equipo de monta cubre:

- **Arneses de control** — arneses de cabeza, cuello y cuerpo para dirigir la criatura durante el desplazamiento.
- **Sistemas de carga** — sillas, plataformas y contenedores para transportar peso sobre la criatura.
- **Equipo de sujeción** — mecanismos para mantener a una criatura inmóvil durante procedimientos de Medicina o extracción.

El tamaño de la criatura determina la complejidad mínima del equipo:

| Tamaño de criatura | Complejidad mínima del arnés |
| --- | --- |
| Pequeño | Simple |
| Mediano | Simple |
| Grande | Complejo |
| Enorme | Complejo |
| Gigantesco | Avanzado |

---

## Equipo para operación en criaturas gigantescas

Las criaturas de escala gigantesca o colosal representan un entorno de trabajo, no solo un combate. Su superficie corporal puede ser el terreno de misiones enteras — para localizar órganos vitales, aplicar procedimientos de Medicina a escala masiva, extraer materiales desde zonas internas, o neutralizar amenazas parásitas que habitan el cuerpo de la bestia.

Ingeniería produce los sistemas especializados que hacen esto posible:

- **Garfios y cables de anclaje** — para fijar posición en superficies de piel gruesa, membrana o escama.
- **Plataformas de trabajo portátiles** — estructuras plegables que se despliegan en puntos de anclaje para trabajar sin movimiento activo.
- **Sistemas de tracción** — mecanismos que permiten escalar o desplazarse por la superficie exterior de la criatura sin consumir esfuerzo constante.
- **Instrumentos de perforación asistida** — para acceder a zonas internas sin herramientas de extracción genéricas.

Cada uno de estos sistemas tiene su Plano específico. El Narrador determina cuáles están disponibles en el mundo y a qué costo.

---

## Herramientas de exploración

Las herramientas de exploración son equipamiento general para entornos difíciles — cavernas, alturas, agua, oscuridad, o terreno sin sendero.

Ejemplos de producción Ingeniería en este dominio:

- **Kits de escalada** — cuerdas, pernos, garfios y sistemas de descenso controlado.
- **Herramientas de espeleología** — equipamiento para movimiento y supervivencia en entornos subterráneos.
- **Sistemas de navegación** — instrumentos de orientación y mapeado en terreno sin referencias visuales claras.
- **Equipamiento de supervivencia** — filtros de agua, refugios portátiles, medios de señalización.

Como con todo equipo de Ingeniería, cada herramienta de exploración tiene su Plano específico con complejidad, materiales y costo propios.
