import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np
import os

def create_fosas_map(output_path):
    fig, ax = plt.subplots(figsize=(12, 12), facecolor="#0b0c10")
    ax.set_facecolor("#0b0c10")
    
    # Define colors
    COLOR_BG = "#0b0c10"
    COLOR_WALLS = "#1f2833"
    COLOR_GRID = "#2a3642"
    COLOR_TERRACE_1 = "#1a1515"
    COLOR_TERRACE_2 = "#2b1c1c"
    COLOR_TERRACE_3 = "#3c2222"
    COLOR_PIT = "#4a0e17" # Deep Red blood-stained pit
    COLOR_RUBBLE = "#6e5d52" # Bone rubble
    COLOR_DOOR = "#45a29e"
    COLOR_TEXT = "#c5c6c7"
    
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    # Grid
    for x in range(0, 101, 10):
        ax.axvline(x, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
    for y in range(0, 101, 10):
        ax.axhline(y, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
        
    # Amphitheater Terraces (Concentric Circles)
    t1 = Circle((50, 50), 45, facecolor=COLOR_TERRACE_1, edgecolor=COLOR_WALLS, linewidth=3, zorder=2)
    ax.add_patch(t1)
    
    t2 = Circle((50, 50), 35, facecolor=COLOR_TERRACE_2, edgecolor=COLOR_WALLS, linewidth=3, zorder=3)
    ax.add_patch(t2)
    
    t3 = Circle((50, 50), 25, facecolor=COLOR_TERRACE_3, edgecolor=COLOR_WALLS, linewidth=3, zorder=4)
    ax.add_patch(t3)
    
    # Central Pit
    pit = Circle((50, 50), 15, facecolor=COLOR_PIT, edgecolor="#7a1725", linewidth=4, zorder=5)
    ax.add_patch(pit)
    
    # Surgical Tables (in the pit)
    table1 = Rectangle((42, 52), 6, 3, facecolor="#3a4a5c", edgecolor="#ffffff", zorder=6, angle=15)
    ax.add_patch(table1)
    table2 = Rectangle((48, 42), 6, 3, facecolor="#3a4a5c", edgecolor="#ffffff", zorder=6, angle=-20)
    ax.add_patch(table2)
    
    # Blood drains
    ax.add_patch(Circle((50, 50), 1, facecolor="#111", zorder=6))
    ax.add_patch(Circle((55, 45), 1, facecolor="#111", zorder=6))
    
    # The Rubble (Collapsed Bone Pillar)
    rubble_poly = Polygon([(55, 60), (45, 65), (50, 75), (65, 70), (60, 55)], facecolor=COLOR_RUBBLE, edgecolor="#3b322c", lw=2, zorder=7)
    ax.add_patch(rubble_poly)
    
    # The trapped Architect
    vesper_marker = Circle((53, 58), 1.5, facecolor="#c9b034", edgecolor="#ffffff", lw=1, zorder=8)
    ax.add_patch(vesper_marker)
    ax.text(53, 54, "ARQUITECTO\nVESPER", color="#c9b034", ha="center", va="center", fontsize=8, fontweight="bold", zorder=10)
    
    # Entrance (West)
    entrance = Rectangle((0, 45), 10, 10, facecolor="#12161a", edgecolor=COLOR_WALLS, lw=2, zorder=9)
    ax.add_patch(entrance)
    ax.text(5, 50, "ENTRADA\n(DESDE CRUCE)", color="#ffffff", ha="center", va="center", fontsize=7, fontweight="bold", rotation=90, zorder=10)
    
    # Exit to Nodo 4 (North)
    exit_door = Rectangle((45, 90), 10, 10, facecolor=COLOR_DOOR, alpha=0.6, edgecolor=COLOR_WALLS, lw=2, zorder=9)
    ax.add_patch(exit_door)
    ax.text(50, 95, "ESCLUSA SELLADA\n(AL NODO 04)", color="#ffffff", ha="center", va="center", fontsize=7, fontweight="bold", zorder=10)
    
    # Labels for terraces
    ax.text(50, 20, "GRADAS DE OBSERVACIÓN", color="#888888", ha="center", va="center", fontsize=10, fontweight="bold", zorder=10)
    
    # Compass
    ax.text(10, 90, "N", color=COLOR_TEXT, fontsize=18, fontweight="bold", ha="center", va="center", zorder=15)
    ax.plot([10, 10], [85, 95], color=COLOR_DOOR, lw=2, zorder=15)
    
    # Legend
    legend_box = Rectangle((2, 2), 55, 16, facecolor="#1f2833", alpha=0.8, edgecolor=COLOR_DOOR, lw=2, zorder=15)
    ax.add_patch(legend_box)
    ax.text(4, 14, "MAPA 07: FOSAS QUIRÚRGICAS", color="#ffffff", fontsize=14, fontweight="bold", zorder=16)
    ax.text(4, 11, "Nodo 03 - Ruta Este", color=COLOR_DOOR, fontsize=10, fontstyle='italic', zorder=16)
    ax.text(4, 5, "• Topografía: Anfiteatro descendente.\n• Escombro: Pilar óseo colapsado.\n• PDI: Arquitecto Vesper (Atrapado).", color=COLOR_TEXT, fontsize=10, linespacing=1.5, zorder=16)

    ax.axis('off')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=COLOR_BG, bbox_inches='tight', dpi=300)
    print(f"Mapa generado: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_07.png"
    create_fosas_map(output_file)
