import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, PathPatch
from matplotlib.path import Path
import numpy as np
import os

def create_matadero_map(output_path):
    fig, ax = plt.subplots(figsize=(12, 16), facecolor="#0b0c10")
    ax.set_facecolor("#0b0c10")
    
    # Define colors matching the dark/tactical theme
    COLOR_BG = "#0b0c10"
    COLOR_WALLS = "#1f2833"
    COLOR_GRID = "#2a3642"
    COLOR_DEEP = "#4a0e17"     # Fosas Quirúrgicas (Deep Red)
    COLOR_CABIN = "#3a4a5c"    # Cabina de Supervisión
    COLOR_WALKWAY = "#6b7a8f"  # Pasarelas
    COLOR_TEXT = "#c5c6c7"
    COLOR_HIGHLIGHT = "#45a29e" # Entradas/Salidas
    COLOR_CHAINS = "#1a232c"   # Zona de cadenas
    
    # 1. Base Grid
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 130)
    
    for x in range(0, 101, 10):
        ax.axvline(x, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
    for y in range(0, 131, 10):
        ax.axhline(y, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
        
    # 2. Main Building Walls (Industrial Rectangular Shape)
    # The Matadero is an enclosed industrial nave
    nave_x = [15, 85, 85, 15]
    nave_y = [20, 20, 110, 110]
    
    nave_poly = Polygon(np.column_stack([nave_x, nave_y]), closed=True, 
                          facecolor="#12161a", edgecolor=COLOR_WALLS, linewidth=4, zorder=1)
    ax.add_patch(nave_poly)
    
    # Masking outside
    vertices = [(0,0), (100,0), (100,130), (0,130), (0,0)]
    for x, y in zip(nave_x[::-1], nave_y[::-1]):
        vertices.append((x,y))
    vertices.append(vertices[5]) # close inner loop
    
    codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY] + \
            [Path.MOVETO] + [Path.LINETO]*(len(nave_x)-1) + [Path.CLOSEPOLY]
            
    mask_path = Path(vertices, codes)
    mask_patch = PathPatch(mask_path, facecolor=COLOR_BG, lw=0, zorder=10)
    ax.add_patch(mask_patch)
    
    # 3. Entrance and Exit
    # Entrance (La Puerta del Matadero)
    entrance = Polygon([(40, 18), (60, 18), (60, 22), (40, 22)], facecolor=COLOR_HIGHLIGHT, alpha=0.5, zorder=2)
    ax.add_patch(entrance)
    ax.text(50, 15, "PUERTA HERMÉTICA\n(ACORDE HIDRÁULICO)", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=15)
    
    # Exit (Escotilla hacia Anfiteatros)
    exit_poly = Polygon([(45, 108), (55, 108), (55, 112), (45, 112)], facecolor=COLOR_HIGHLIGHT, alpha=0.5, zorder=2)
    ax.add_patch(exit_poly)
    ax.text(50, 115, "ESCOTILLAS\n(AL NODO 03)", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=15)

    # 4. Fosas Quirúrgicas / Filtros de Sangre (Lower Levels - Planta Baja)
    # Left Side
    fosa_l = Polygon([(20, 30), (35, 30), (35, 100), (20, 100)], facecolor=COLOR_DEEP, alpha=0.6, hatch='\\\\', edgecolor="#7a1725", linewidth=2, zorder=2)
    ax.add_patch(fosa_l)
    ax.text(27.5, 65, "FILTROS DE SANGRE\n(PLANTA BAJA)", color="#ffffff", ha="center", va="center", fontsize=9, fontweight="bold", rotation=90, zorder=15)
    
    # Right Side
    fosa_r = Polygon([(65, 30), (80, 30), (80, 100), (65, 100)], facecolor=COLOR_DEEP, alpha=0.6, hatch='//', edgecolor="#7a1725", linewidth=2, zorder=2)
    ax.add_patch(fosa_r)
    ax.text(72.5, 65, "FOSAS QUIRÚRGICAS\n(PLANTA BAJA)", color="#ffffff", ha="center", va="center", fontsize=9, fontweight="bold", rotation=-90, zorder=15)

    # 5. Bosque de Cadenas (Upper Level - Area of Combat)
    cadenas_poly = Polygon([(35, 30), (65, 30), (65, 100), (35, 100)], facecolor=COLOR_CHAINS, alpha=0.8, edgecolor=COLOR_GRID, linewidth=2, zorder=3)
    ax.add_patch(cadenas_poly)
    ax.text(50, 85, "EL BOSQUE DE CADENAS\n(ZONA DE EMBOSCADA)", color="#7a8c9e", ha="center", va="center", fontsize=10, fontweight="bold", zorder=15)

    # Add chain dots
    for _ in range(80):
        cx = np.random.uniform(36, 64)
        cy = np.random.uniform(32, 98)
        # Avoid the central cabin
        if not (45 <= cx <= 55 and 55 <= cy <= 65):
            ax.add_patch(Circle((cx, cy), 0.5, facecolor="#c5c6c7", alpha=0.4, zorder=4))

    # 6. Cabina de Supervisión y Pasarelas (Upper Level)
    # Walkways
    walkway_1 = Polygon([(50, 22), (50, 55)], closed=False, edgecolor=COLOR_WALKWAY, linewidth=6, zorder=4)
    ax.add_patch(walkway_1)
    walkway_2 = Polygon([(35, 60), (65, 60)], closed=False, edgecolor=COLOR_WALKWAY, linewidth=6, zorder=4)
    ax.add_patch(walkway_2)

    # Central Cabin
    cabin_poly = Rectangle((45, 55), 10, 10, facecolor=COLOR_CABIN, edgecolor="#ffffff", linewidth=2, zorder=5)
    ax.add_patch(cabin_poly)
    ax.text(50, 60, "CABINA DE\nSUPERVISIÓN", color="#ffffff", ha="center", va="center", fontsize=9, fontweight="bold", zorder=15)

    # 7. Compass and Legend
    # Compass
    ax.text(10, 115, "N", color=COLOR_TEXT, fontsize=24, fontweight="bold", ha="center", va="center", zorder=15)
    ax.plot([10, 10], [108, 122], color=COLOR_HIGHLIGHT, lw=2, zorder=15)
    ax.plot([7, 13], [115, 115], color=COLOR_TEXT, lw=1, zorder=15)
    
    # Title & Legend Box
    legend_box = Rectangle((2, 2), 48, 18, facecolor="#1f2833", alpha=0.8, edgecolor=COLOR_HIGHLIGHT, lw=2, zorder=15)
    ax.add_patch(legend_box)
    
    ax.text(4, 16, "NIVEL 2: EL MATADERO DE TINTA", color="#ffffff", fontsize=14, fontweight="bold", zorder=16)
    ax.text(4, 13, "Mapa Topográfico de Referencia", color=COLOR_HIGHLIGHT, fontsize=10, fontstyle='italic', zorder=16)
    ax.text(4, 9, "• Sin Cuadrícula Táctica (Escala Kilométrica)\n• Planta Alta: Cadenas y Pasarelas\n• Planta Baja: Drenaje Quirúrgico", color=COLOR_TEXT, fontsize=9, linespacing=1.5, zorder=16)

    # Final touches
    ax.axis('off')
    
    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=COLOR_BG, bbox_inches='tight', dpi=300)
    print(f"Mapa topográfico generado en: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_04.png"
    create_matadero_map(output_file)
