import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np
import os

def create_cruce_sotano_map(output_path):
    fig, ax = plt.subplots(figsize=(10, 10), facecolor="#0b0c10")
    ax.set_facecolor("#0b0c10")
    
    # Define colors
    COLOR_BG = "#0b0c10"
    COLOR_WALLS = "#1f2833"
    COLOR_GRID = "#2a3642"
    COLOR_FLOOR = "#12161a"
    COLOR_TEXT = "#c5c6c7"
    COLOR_HIGHLIGHT = "#45a29e"
    COLOR_BLOOD = "#4a0e17"
    
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    # Grid
    for x in range(0, 101, 10):
        ax.axvline(x, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
    for y in range(0, 101, 10):
        ax.axhline(y, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
        
    # The T-Intersection Floor
    # Vertical corridor from North (y=100 down to y=40)
    vert_floor = Rectangle((40, 40), 20, 60, facecolor=COLOR_FLOOR, edgecolor=COLOR_WALLS, linewidth=3, zorder=2)
    ax.add_patch(vert_floor)
    
    # Horizontal corridor (x=10 to x=90, y=40 to y=60)
    horiz_floor = Rectangle((10, 40), 80, 20, facecolor=COLOR_FLOOR, edgecolor=COLOR_WALLS, linewidth=3, zorder=2)
    ax.add_patch(horiz_floor)
    
    # Remove the inner walls (overlapping lines) by drawing a floor-colored polygon over the intersection
    intersection = Rectangle((40.5, 40.5), 19, 19, facecolor=COLOR_FLOOR, lw=0, zorder=3)
    ax.add_patch(intersection)
    
    # Elements
    # Drop zone (Escotillas)
    drop_zone = Rectangle((45, 90), 10, 10, facecolor=COLOR_BLOOD, alpha=0.4, hatch='//', edgecolor=COLOR_HIGHLIGHT, lw=2, zorder=4)
    ax.add_patch(drop_zone)
    ax.text(50, 95, "ZONA DE\nCAÍDA", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=10)
    
    # Blood trail / Vesper sign at intersection
    blood_sign = Polygon([(48, 55), (52, 55), (50, 58)], facecolor=COLOR_BLOOD, alpha=0.8, zorder=4)
    ax.add_patch(blood_sign)
    ax.text(50, 52, "GRABADO\nENSANGRENTADO", color=COLOR_BLOOD, ha="center", va="center", fontsize=8, fontweight="bold", zorder=10)
    
    # Exits
    # West exit
    west_exit = Rectangle((10, 40), 10, 20, facecolor="#2a4d3a", alpha=0.5, zorder=4) # greenish for toxic filters
    ax.add_patch(west_exit)
    ax.text(15, 50, "HACIA\nFILTROS", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=10)
    
    # East exit
    east_exit = Rectangle((80, 40), 10, 20, facecolor=COLOR_BLOOD, alpha=0.5, zorder=4)
    ax.add_patch(east_exit)
    ax.text(85, 50, "HACIA\nFOSAS", color="#ffffff", ha="center", va="center", fontsize=10, fontweight="bold", zorder=10)
    
    # Compass
    ax.text(10, 90, "N", color=COLOR_TEXT, fontsize=18, fontweight="bold", ha="center", va="center", zorder=15)
    ax.plot([10, 10], [85, 95], color=COLOR_HIGHLIGHT, lw=2, zorder=15)
    
    # Legend
    legend_box = Rectangle((2, 2), 48, 16, facecolor="#1f2833", alpha=0.8, edgecolor=COLOR_HIGHLIGHT, lw=2, zorder=15)
    ax.add_patch(legend_box)
    ax.text(4, 14, "MAPA 05: CRUCE DEL SÓTANO", color="#ffffff", fontsize=14, fontweight="bold", zorder=16)
    ax.text(4, 11, "Nodo 03 - Entrada", color=COLOR_HIGHLIGHT, fontsize=10, fontstyle='italic', zorder=16)
    ax.text(4, 5, "• Zona claustrofóbica.\n• Bifurcación táctica.", color=COLOR_TEXT, fontsize=10, linespacing=1.5, zorder=16)

    ax.axis('off')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=COLOR_BG, bbox_inches='tight', dpi=300)
    print(f"Mapa generado: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_05.png"
    create_cruce_sotano_map(output_file)
