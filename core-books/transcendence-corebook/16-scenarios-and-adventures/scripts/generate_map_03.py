import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, PathPatch
from matplotlib.path import Path
import numpy as np
import os

def create_crater_map(output_path):
    fig, ax = plt.subplots(figsize=(12, 16), facecolor="#0b0c10")
    ax.set_facecolor("#0b0c10")
    
    # Define colors matching the dark/tactical theme
    COLOR_BG = "#0b0c10"
    COLOR_WALLS = "#1f2833"
    COLOR_GRID = "#2a3642"
    COLOR_CRATER = "#4a0e17"  # Deep red/burn
    COLOR_ACID = "#3a4a20"    # Sickly green
    COLOR_BRIDGE = "#6b7a8f"  # Bone/Stone grey
    COLOR_TEXT = "#c5c6c7"
    COLOR_HIGHLIGHT = "#45a29e" # Cyan for entrances/exits
    
    # 1. Base Grid (Decorative, not for movement, just to give it a "blueprint" feel)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 130)
    
    for x in range(0, 101, 10):
        ax.axvline(x, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
    for y in range(0, 131, 10):
        ax.axhline(y, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
        
    # 2. Outer Cavern Walls (Rough circular shape)
    # Using a jagged polygon to represent the massive cavern walls
    theta = np.linspace(0, 2*np.pi, 50)
    r = 45 + np.random.normal(0, 2, 50) # radius around 45 with some noise
    x_cavern = 50 + r * np.cos(theta)
    y_cavern = 65 + r * np.sin(theta)
    
    cavern_poly = Polygon(np.column_stack([x_cavern, y_cavern]), closed=True, 
                          facecolor="#12161a", edgecolor=COLOR_WALLS, linewidth=3, zorder=1)
    ax.add_patch(cavern_poly)
    
    # Add a thick outer boundary to mask everything outside the cavern
    # This is a bit of a trick: draw a massive rectangle with a hole in it.
    vertices = [(0,0), (100,0), (100,130), (0,130), (0,0)]
    for x, y in zip(x_cavern[::-1], y_cavern[::-1]):
        vertices.append((x,y))
    vertices.append(vertices[5]) # close inner loop
    
    codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY] + \
            [Path.MOVETO] + [Path.LINETO]*(len(x_cavern)-1) + [Path.CLOSEPOLY]
            
    mask_path = Path(vertices, codes)
    mask_patch = PathPatch(mask_path, facecolor=COLOR_BG, lw=0, zorder=10)
    ax.add_patch(mask_patch)
    
    # 3. Entrance (South) and Exit (North)
    # Entrance (Túnel de escape)
    entrance = Polygon([(45, 10), (55, 10), (53, 22), (47, 22)], facecolor=COLOR_HIGHLIGHT, alpha=0.5, zorder=2)
    ax.add_patch(entrance)
    ax.text(50, 15, "TÚNEL\n(DESDE EL FOSO)", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=15)
    
    # Exit (Hacia el Matadero)
    exit_poly = Polygon([(40, 108), (60, 108), (65, 120), (35, 120)], facecolor=COLOR_HIGHLIGHT, alpha=0.5, zorder=2)
    ax.add_patch(exit_poly)
    ax.text(50, 114, "ESCLUSA DE DRENAJE\n(AL MATADERO)", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=15)

    # 4. Central Crater (Blast Zone)
    # Drawing multiple concentric distorted circles for the crater
    for rad, alpha, col in [(20, 0.4, COLOR_CRATER), (15, 0.6, "#5c111c"), (8, 0.8, "#7a1725")]:
        crater_r = rad + np.random.normal(0, 1, 30)
        crater_x = 50 + crater_r * np.cos(np.linspace(0, 2*np.pi, 30))
        crater_y = 65 + crater_r * np.sin(np.linspace(0, 2*np.pi, 30))
        crater_poly = Polygon(np.column_stack([crater_x, crater_y]), closed=True, 
                              facecolor=col, alpha=alpha, zorder=2)
        ax.add_patch(crater_poly)
    ax.text(50, 65, "EPICENTRO\n(CARROÑEROS MASIVOS)", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=15)

    # 5. Acid Sea (East side)
    # Jagged shape representing pools of acid
    theta_acid = np.linspace(-np.pi/4, np.pi/2.5, 20)
    r_acid = 30 + np.random.normal(0, 2, 20)
    x_acid = 70 + r_acid * np.cos(theta_acid)
    y_acid = 65 + r_acid * np.sin(theta_acid)
    # close the shape against the wall
    x_acid = np.append(x_acid, [90, 90, 70])
    y_acid = np.append(y_acid, [90, 40, 40])
    
    acid_poly = Polygon(np.column_stack([x_acid, y_acid]), closed=True, 
                        facecolor=COLOR_ACID, alpha=0.6, edgecolor="#5c7a33", linewidth=2, zorder=2)
    ax.add_patch(acid_poly)
    ax.text(78, 65, "MAR DE ÁCIDO\n(RUTA INFERIOR)", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=15)
    
    # Add some "bubbles" in the acid sea
    for _ in range(15):
        bx = np.random.uniform(70, 85)
        by = np.random.uniform(45, 85)
        ax.add_patch(Circle((bx, by), np.random.uniform(0.5, 1.5), facecolor="#7bb543", alpha=0.5, zorder=3))

    # 5.5 Massive Cave-in (West side blocking the easy path)
    theta_debris = np.linspace(-np.pi/2.5, np.pi/2.5, 20)
    r_debris = 30 + np.random.normal(0, 3, 20)
    x_debris = 10 + r_debris * np.cos(theta_debris)
    y_debris = 65 + r_debris * np.sin(theta_debris)
    x_debris = np.append(x_debris, [0, 0, 10])
    y_debris = np.append(y_debris, [95, 35, 35])
    
    debris_poly = Polygon(np.column_stack([x_debris, y_debris]), closed=True, 
                          facecolor="#1a1e24", edgecolor="#2a3642", linewidth=2, zorder=3, hatch='//')
    ax.add_patch(debris_poly)
    ax.text(18, 65, "DERRUMBE ESTRUCTURAL\n(INTRANSITABLE)", color="#5c6a7a", ha="center", va="center", fontsize=9, fontweight="bold", rotation=90, zorder=15)

    # 6. Bone Bridge (Over the center)
    # A massive diagonal bridge broken in the middle
    # South segment
    bridge_s = Polygon([(46, 20), (54, 20), (45, 55), (37, 55)], facecolor=COLOR_BRIDGE, edgecolor="#ffffff", linewidth=1.5, zorder=5)
    ax.add_patch(bridge_s)
    # North segment
    bridge_n = Polygon([(36, 62), (44, 62), (55, 110), (45, 110)], facecolor=COLOR_BRIDGE, edgecolor="#ffffff", linewidth=1.5, zorder=5)
    ax.add_patch(bridge_n)
    
    # Bridge details (shadows/texture lines)
    ax.plot([50, 41], [20, 55], color="#3a4a5c", lw=1, zorder=6)
    ax.plot([40, 50], [62, 110], color="#3a4a5c", lw=1, zorder=6)
    
    # Bridge Label
    ax.text(32, 45, "PUENTE DE HUESO\n(RUTA AÉREA INESTABLE)", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", rotation=75, zorder=15)

    # 7. Compass and Legend
    # Compass
    ax.text(10, 115, "N", color=COLOR_TEXT, fontsize=24, fontweight="bold", ha="center", va="center", zorder=15)
    ax.plot([10, 10], [108, 122], color=COLOR_HIGHLIGHT, lw=2, zorder=15)
    ax.plot([7, 13], [115, 115], color=COLOR_TEXT, lw=1, zorder=15)
    
    # Title & Legend Box
    legend_box = Rectangle((2, 2), 40, 18, facecolor="#1f2833", alpha=0.8, edgecolor=COLOR_HIGHLIGHT, lw=2, zorder=15)
    ax.add_patch(legend_box)
    
    ax.text(4, 16, "NIVEL 2: EL SUMIDERO QUIRÚRGICO", color="#ffffff", fontsize=14, fontweight="bold", zorder=16)
    ax.text(4, 13, "Mapa Topográfico de Referencia", color=COLOR_HIGHLIGHT, fontsize=10, fontstyle='italic', zorder=16)
    ax.text(4, 9, "• Sin Cuadrícula Táctica (Escala Kilométrica)\n• Ruta Inferior: Fango Tóxico\n• Ruta Superior: Viga Colapsada", color=COLOR_TEXT, fontsize=9, linespacing=1.5, zorder=16)

    # Final touches
    ax.axis('off')
    
    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=COLOR_BG, bbox_inches='tight', dpi=300)
    print(f"Mapa topográfico del cráter generado en: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_03.png"
    create_crater_map(output_file)
