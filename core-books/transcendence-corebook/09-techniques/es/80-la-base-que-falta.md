---
title: "La Base Que Falta"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, interrupcion, attack, reactive, drakkai, desequilibrado, alteracion]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# La Base Que Falta

### Reactivo - Ataque

**Rango Novato**

*Cuando el pie busca apoyo, la garra ya lo está esperando.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| T.R. (Alteraciones) | T.I. | `6` | `2` |

## Requisitos

- Perfil de arma: `Interrupción`

## Keywords

- `Interrupción`
- `Desequilibrado`

## Efecto

Cuando un enemigo dentro de tu alcance comienza una acción de ataque, realiza una T.A. con tu perfil de `Interrupción` contra el atacante. Esta tirada reemplaza tu T.D. contra esa acción. Compara tu T.A. con la T.A. del atacante.

Si tu T.A. es igual o mayor que la del atacante, la acción falla y resuelves tu T.I. normalmente. El atacante realiza una T.R. (Alteraciones) contra `Desequilibrado`: si falla, queda `Desequilibrado` a la severidad determinada por tu rango de competencia.

Si tu T.A. es menor que la del atacante, la interrupción falla y la acción resuelve como si tu T.D. hubiera fallado.

| Rango | Severidad |
| --- | --- |
| 1–2 | Leve |
| 3–4 | Moderado |
| 5–6 | Grave |