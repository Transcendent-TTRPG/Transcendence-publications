import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, PathPatch
from matplotlib.path import Path
import matplotlib.patheffects as pe
import numpy as np

# ─── PALETA VESPER ─────────────────────────────────────────────────────────
BG       = '#050508' # Abismo exterior
FLOOR    = '#1a1a24' # Basalto oscuro
WALL     = '#8c8c73' # Hueso envejecido / Piedra acústica
BLOOD    = '#591a1a' # Canales de drenaje (rojo coagulado)
MOSS     = '#4d7339' # Musgo bioluminiscente
TEXT     = '#d8d8e8'
DIM      = '#6868a0'
DOOR_C   = '#8c8c73' # Puertas biológicas de piedra
STAIR_C  = '#4a4a5a' # Escalones tallados / Pozo

W, H = 24, 30
fig, ax = plt.subplots(figsize=(10, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# ─── GRID ──────────────────────────────────────────────────────────────────
for i in range(W + 1):
    ax.axvline(i, color='#111118', lw=0.5, zorder=1)
for i in range(H + 1):
    ax.axhline(i, color='#111118', lw=0.5, zorder=1)

# ─── PRIMITIVAS VESPER ──────────────────────────────────────────────────────

def circular_room(cx, cy, r, fc=FLOOR, label='', num=None, ls=7):
    ax.add_patch(Circle((cx, cy), r, fc=fc, ec=WALL, lw=2, zorder=2))
    if label:
        ax.text(cx, cy, label, color=TEXT, fontsize=ls,
                ha='center', va='center', family='monospace', zorder=5,
                path_effects=[pe.withStroke(linewidth=3, foreground=fc)])
    if num is not None:
        ax.text(cx - r*.7, cy + r*.7, str(num), color=DIM, fontsize=9,
                ha='center', va='center', family='monospace', zorder=6)

def rectangular_room(x, y, w, h, fc=FLOOR, label='', num=None, ls=7):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=WALL, lw=2, zorder=2))
    if label:
        ax.text(x+w/2, y+h/2, label, color=TEXT, fontsize=ls,
                ha='center', va='center', family='monospace', zorder=5,
                path_effects=[pe.withStroke(linewidth=3, foreground=fc)])
    if num is not None:
        ax.text(x+.4, y+h-.6, str(num), color=DIM, fontsize=9,
                ha='left', va='center', family='monospace', zorder=6)

def corridor(x, y, w, h, label=''):
    ax.add_patch(Rectangle((x, y), w, h, fc=FLOOR, ec=WALL, lw=2, zorder=2))
    if label:
        ax.text(x+w/2, y+h/2, label, color=TEXT, fontsize=8,
                ha='center', va='center', family='monospace', zorder=5, rotation=90,
                path_effects=[pe.withStroke(linewidth=3, foreground=FLOOR)])

def blood_channel(xs, ys):
    ax.plot(xs, ys, color=BLOOD, lw=2, zorder=3, alpha=0.8)

def door(cx, cy, horiz=True):
    s, t = 1.6, 0.3
    if horiz:
        ax.add_patch(Rectangle((cx-s/2, cy-t/2), s, t, fc=DOOR_C, ec=BG, lw=1.5, zorder=4))
    else:
        ax.add_patch(Rectangle((cx-t/2, cy-s/2), t, s, fc=DOOR_C, ec=BG, lw=1.5, zorder=4))

def pod(cx, cy):
    ax.add_patch(Circle((cx, cy), 0.5, fc=MOSS, ec=BG, lw=1, alpha=0.3, zorder=4))
    ax.add_patch(Circle((cx, cy), 0.2, fc=BG, ec='none', zorder=4))

# ─── DISEÑO DEL NIVEL 1 ─────────────────────────────────────────────────────

# 1. Foso de Gestación (Abajo)
circular_room(12, 8, 6, label='FOSO DE\nGESTACIÓN', num=1, ls=11)
# Vainas
for px, py in [(9.5, 10.5), (14.5, 11), (8.5, 7), (11, 4), (15, 6), (13, 9)]:
    pod(px, py)
# Cadáveres
ax.text(12, 12, 'X X X', color='#ff4444', fontsize=10, ha='center', va='center', zorder=5)

# 2. Corredor de Sangre
corridor(10.5, 14, 3, 7, label='CORREDOR')

# 3. Almacén de Contención (Anexo al corredor)
rectangular_room(13.5, 15, 5, 5, label='ALMACÉN DE\nCONTENCIÓN', num=2, ls=8)
# Bastidores en el almacén
ax.plot([14.5, 17.5], [18, 18], color=WALL, lw=1.5, zorder=4)
ax.plot([14.5, 17.5], [16, 16], color=WALL, lw=1.5, zorder=4)

# 4. Pozo Vertical (Chimenea de Escalada)
rectangular_room(10.5, 21, 3, 3, fc='#0a0a0f', label='', num=3, ls=8)
ax.text(12, 22.5, 'POZO\nVERTICAL\n(Ascensión)', color=DIM, fontsize=7, ha='center', va='center', zorder=5)
# Símbolo de pozo
ax.add_patch(Rectangle((11, 21.5), 2, 2, fc='none', ec=STAIR_C, lw=1, ls='--', zorder=4))
ax.add_patch(Rectangle((11.5, 22), 1, 1, fc='none', ec=STAIR_C, lw=1, ls='--', zorder=4))

# Puertas
door(12, 14, horiz=True)    # Portón Principal (Foso -> Corredor)
door(13.5, 16.5, horiz=False) # Puerta lateral (Corredor -> Almacén)

# Canales de drenaje (Sangre)
blood_channel([12, 12], [8, 14])       # Del centro del foso al portón
blood_channel([12, 12], [14, 21])      # Todo a lo largo del corredor
blood_channel([13.5, 12], [17.5, 17.5]) # Del almacén al corredor

# ─── TITULO ─────────────────────────────────────────────────────────────────
ax.text(W/2, H-1.5, 'CONTENEDORES VACÍOS - MAPA 1', color=TEXT, fontsize=16,
        ha='center', va='top', family='monospace', fontweight='bold', zorder=10)
ax.text(W/2, H-2.5, 'Nivel 3: El Drenaje', color=DIM, fontsize=12,
        ha='center', va='top', family='monospace', zorder=10)

ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout(pad=.3)

output_dir = '../assets/maps'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f'{output_dir}/mapa_01.png', format='png', facecolor=BG, bbox_inches='tight', dpi=200)
print(f"Mapa guardado en {output_dir}/mapa_01.png")
