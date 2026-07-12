import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np
import os

def create_filtros_map(output_path):
    fig, ax = plt.subplots(figsize=(12, 12), facecolor="#0b0c10")
    ax.set_facecolor("#0b0c10")
    
    # Define colors
    COLOR_BG = "#0b0c10"
    COLOR_WALLS = "#1f2833"
    COLOR_GRID = "#2a3642"
    COLOR_FANGO = "#2a4d3a" # Toxic Green/Brown
    COLOR_PIPES = "#8f5c38" # Rusty Bronze/Copper
    COLOR_CABINETS = "#1c4a78" # Medical Blue
    COLOR_TEXT = "#c5c6c7"
    COLOR_HIGHLIGHT = "#45a29e"
    
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    # Grid
    for x in range(0, 101, 10):
        ax.axvline(x, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
    for y in range(0, 101, 10):
        ax.axhline(y, color=COLOR_GRID, linewidth=0.5, alpha=0.3)
        
    # Main Cavern (Circle)
    cavern = Circle((50, 50), 45, facecolor=COLOR_FANGO, alpha=0.6, hatch='.', edgecolor=COLOR_WALLS, linewidth=5, zorder=2)
    ax.add_patch(cavern)
    ax.text(50, 20, "FANGO QUÍMICO Y\nSANGRE COAGULADA", color="#153625", ha="center", va="center", fontsize=14, fontweight="bold", zorder=10)

    # Entrance (East)
    entrance = Rectangle((90, 45), 10, 10, facecolor="#12161a", edgecolor=COLOR_WALLS, lw=2, zorder=3)
    ax.add_patch(entrance)
    ax.text(95, 50, "ENTRADA\n(DESDE CRUCE)", color="#ffffff", ha="center", va="center", fontsize=8, fontweight="bold", rotation=90, zorder=10)
    
    # The Pipe Maze (Acrobatics Challenge)
    # We draw several lines representing thick pipes connecting entrance to cabinets
    pipes = [
        [(90, 50), (75, 50)],
        [(75, 50), (60, 70)],
        [(75, 50), (70, 30)],
        [(70, 30), (50, 30)],
        [(60, 70), (45, 75)],
        [(45, 75), (25, 60)],
        [(50, 30), (35, 40)],
        [(35, 40), (25, 60)],
        [(25, 60), (15, 60)]
    ]
    for p in pipes:
        pipe_poly = Polygon(p, closed=False, edgecolor=COLOR_PIPES, linewidth=8, zorder=4)
        ax.add_patch(pipe_poly)
        # Inner pipe detail
        pipe_poly_in = Polygon(p, closed=False, edgecolor="#63391b", linewidth=4, zorder=5)
        ax.add_patch(pipe_poly_in)
        
    # Broken pipe gaps
    ax.plot([50, 48], [30, 31], color=COLOR_FANGO, lw=10, zorder=6) # Gap in a pipe
    ax.plot([67, 65], [72, 73], color=COLOR_FANGO, lw=10, zorder=6)
    
    # Toxic Vapor Clouds
    for _ in range(25):
        cx = np.random.uniform(15, 85)
        cy = np.random.uniform(15, 85)
        ax.add_patch(Circle((cx, cy), np.random.uniform(4, 10), facecolor="#6dc28a", alpha=0.15, zorder=7))
    
    # Sterilization Cabinets (West)
    cabinets = Rectangle((5, 50), 10, 20, facecolor=COLOR_CABINETS, edgecolor="#ffffff", lw=2, zorder=8)
    ax.add_patch(cabinets)
    ax.text(10, 60, "GABINETES DE\nESTERILIZACIÓN\n(BOTÍN)", color="#ffffff", ha="center", va="center", fontsize=8, fontweight="bold", rotation=90, zorder=10)
    
    # Door to Bóveda de Resina (South-West corner)
    resin_door = Polygon([(15, 10), (25, 5), (30, 10), (20, 15)], facecolor="#8c783e", alpha=0.7, zorder=8)
    ax.add_patch(resin_door)
    ax.text(22, 10, "PUERTA SELLADA\n(BÓVEDA DE RESINA)", color="#ffffff", ha="center", va="center", fontsize=7, fontweight="bold", rotation=-25, zorder=10)

    # Compass
    ax.text(10, 90, "N", color=COLOR_TEXT, fontsize=18, fontweight="bold", ha="center", va="center", zorder=15)
    ax.plot([10, 10], [85, 95], color=COLOR_HIGHLIGHT, lw=2, zorder=15)
    
    # Legend
    legend_box = Rectangle((2, 2), 52, 16, facecolor="#1f2833", alpha=0.8, edgecolor=COLOR_HIGHLIGHT, lw=2, zorder=15)
    ax.add_patch(legend_box)
    ax.text(4, 14, "MAPA 06: FILTROS DE SANGRE", color="#ffffff", fontsize=14, fontweight="bold", zorder=16)
    ax.text(4, 11, "Nodo 03 - Ruta Oeste", color=COLOR_HIGHLIGHT, fontsize=10, fontstyle='italic', zorder=16)
    ax.text(4, 5, "• Peligro Ambiental: Vapor Tóxico (Escaldado).\n• Caída al Fango Químico (Corrupción).\n• Botín Médico protegido por aspersores.", color=COLOR_TEXT, fontsize=10, linespacing=1.5, zorder=16)

    ax.axis('off')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=COLOR_BG, bbox_inches='tight', dpi=300)
    print(f"Mapa generado: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_06.png"
    create_filtros_map(output_file)
