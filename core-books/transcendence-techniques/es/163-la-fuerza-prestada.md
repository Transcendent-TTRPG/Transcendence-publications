---
title: "La fuerza prestada"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, bufoni, torsion, reactive, utility, attack-redirection]
authority_refs:
  - Transcendence-design/data/system/techniques.yaml
  - Transcendence-design/docs/system/technique-la-fuerza-prestada.md
related:
  - core-books/transcendence-techniques/en/163-borrowed-force.md
  - core-books/transcendence-corebook/06-species/es/14-bufoni.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-acciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/05-heridas-y-dano.md
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
---

# La fuerza prestada

### Reactivo - Utilidad

**Rango Novato**

*El golpe encuentra otra carne.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | `3` | `1` |

## Requisitos

- Competencia Novato o superior con el arma utilizada.
- Arma con perfil `Torsión`.

## Palabras clave

- `Torsión`

## Efecto

Cuando se declare un ataque físico contra una sola criatura, puedes intervenir antes de resolver su defensa si tu arma puede alcanzar el arma o extremidad atacante en el punto de contacto que vas a alterar. Puedes intervenir aunque el ataque no vaya dirigido contra ti. Esta técnica no puede redirigir proyectiles ni ataques de área.

Elige otra criatura que ese mismo ataque pueda alcanzar mediante una trayectoria físicamente válida, sin aumentar su alcance ni atravesar obstáculos. Realiza una `T.A.` con tu arma de Torsión, enfrentada a la `T.A.` del agresor.

Si tu `T.A.` no supera la del agresor, el ataque continúa contra su destinatario original, que conserva su defensa habitual.

Si la superas, el ataque se dirige contra la criatura elegida. El agresor conserva el resultado del dado de su `T.A.` y ajusta únicamente los modificadores que dependan del nuevo destinatario. Esa `T.A.` se enfrenta a la `T.D.` de la criatura elegida.

Si el ataque conecta, el agresor resuelve su impacto y los efectos propios del contacto contra la protección del nuevo destinatario. Sus requisitos, márgenes y resistencias se comprueban contra esa criatura. No añades impacto ni efectos de tu propia arma.

Cada uso afecta un solo ataque, no toda una secuencia ni sus movimientos o ataques adicionales. Puedes intentar esta técnica una vez contra cada ataque. Un ataque ya redirigido mediante esta misma técnica no puede volver a redirigirse con ella. El nuevo destinatario conserva sus otras reacciones permitidas.

Pagas Ritmo y Desgaste aunque la intervención falle.

## Ejemplo

Un agresor ataca a tu compañero con `T.A.` 10. Puedes alcanzar el arma atacante y hay otra criatura en una trayectoria válida para ese mismo golpe. Tu `T.A.` obtiene 12: rediriges el ataque. Sin cambios en los modificadores del destinatario, conserva `T.A.` 10. La nueva criatura obtiene `T.D.` 11 y evita el golpe; no recibe impacto. Has pagado Ritmo 3 y Desgaste 1. Si tu intervención hubiera obtenido 10, el empate dejaría el ataque dirigido a tu compañero, que conservaría su defensa habitual.
