import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle
import numpy as np
import os

def create_base_caverna_map(output_path):
    # Set up the figure for a tactical grid (e.g., 20x20 squares)
    fig, ax = plt.subplots(figsize=(10, 10), facecolor="#0b0c10")
    ax.set_facecolor("#0b0c10")
    
    # Theme Colors
    COLOR_BG = "#0b0c10"
    COLOR_WALLS = "#1f2833"
    COLOR_GRID = "#2a3642"
    COLOR_DEBRIS = "#1a222b"
    COLOR_DEBRIS_EDGE = "#45a29e"
    COLOR_TEXT = "#c5c6c7"
    COLOR_DANGER = "#a24545"
    COLOR_SAFE = "#2e4a3d"
    
    # Map limits (20x20 Grid)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    
    # 1. Tactical Grid (Casillas)
    # 1 unit = 1 casilla (e.g., 1.5 metros)
    for x in range(0, 21):
        ax.axvline(x, color=COLOR_GRID, linewidth=1, alpha=0.5)
    for y in range(0, 21):
        ax.axhline(y, color=COLOR_GRID, linewidth=1, alpha=0.5)
        
    # 2. El Muro Norte (La pared infranqueable por la que bajaron)
    muro_x = [0, 20, 20, 0]
    muro_y = [18, 18, 20, 20]
    muro_poly = Polygon(np.column_stack([muro_x, muro_y]), closed=True, 
                        facecolor=COLOR_WALLS, edgecolor="#000000", linewidth=3, zorder=2)
    ax.add_patch(muro_poly)
    # Texture for the wall
    for i in range(40):
        cx = np.random.uniform(0, 20)
        cy = np.random.uniform(18.2, 19.8)
        plt.plot([cx, cx+0.2], [cy, cy-0.2], color="#000000", lw=2, zorder=3)
    ax.text(10, 19, "ACANTILADO (Pared de la Caverna)", color="#ffffff", ha="center", va="center", fontsize=12, fontweight="bold", zorder=15)
    
    # 3. Zona de Aterrizaje (Punto de inicio de los PJs)
    landing_zone = Rectangle((6, 16), 8, 2, facecolor=COLOR_SAFE, alpha=0.4, edgecolor="#52cc7a", lw=2, linestyle='--', zorder=2)
    ax.add_patch(landing_zone)
    ax.text(10, 17, "ZONA DE DESCENSO (PJs)", color="#ffffff", ha="center", va="center", fontsize=9, fontweight="bold", zorder=15)
    
    # 4. El Laberinto de Escombros (Coberturas Masivas)
    # These represent the giant chunks of rock and bridge where the scavenger hides.
    # Escombro 1 (Izquierda Superior)
    esc1 = Polygon([(2, 11), (5, 14), (6, 12), (3, 8)], facecolor=COLOR_DEBRIS, edgecolor=COLOR_DEBRIS_EDGE, lw=2, zorder=5)
    ax.add_patch(esc1)
    
    # Escombro 2 (Centro) - Bloquea línea de visión directa
    esc2 = Polygon([(8, 9), (13, 11), (14, 8), (11, 6), (7, 7)], facecolor=COLOR_DEBRIS, edgecolor=COLOR_DEBRIS_EDGE, lw=2, zorder=5)
    ax.add_patch(esc2)
    ax.text(10.5, 8.5, "ESCOMBRO MASIVO\n(Cobertura Total)", color=COLOR_DEBRIS_EDGE, ha="center", va="center", fontsize=7, fontweight="bold", zorder=15)
    
    # Escombro 3 (Derecha)
    esc3 = Polygon([(15, 15), (18, 14), (19, 9), (16, 10)], facecolor=COLOR_DEBRIS, edgecolor=COLOR_DEBRIS_EDGE, lw=2, zorder=5)
    ax.add_patch(esc3)
    
    # Escombro 4 (Inferior Izquierda)
    esc4 = Polygon([(1, 2), (5, 4), (6, 2), (3, 0)], facecolor=COLOR_DEBRIS, edgecolor=COLOR_DEBRIS_EDGE, lw=2, zorder=5)
    ax.add_patch(esc4)
    
    # Escombro 5 (Inferior Derecha)
    esc5 = Polygon([(13, 3), (17, 5), (19, 2), (14, 1)], facecolor=COLOR_DEBRIS, edgecolor=COLOR_DEBRIS_EDGE, lw=2, zorder=5)
    ax.add_patch(esc5)

    # 5. El Cadáver Vesper (El objetivo del Carroñero y la clave del Silbato)
    # The scavenger killed a Vesper here, who holds the whistle needed for the puzzle door.
    vesper_x, vesper_y = 12, 10
    ax.add_patch(Circle((vesper_x, vesper_y), 0.4, facecolor="#8c1c1c", alpha=0.8, edgecolor="#ff4d4d", lw=1.5, zorder=4))
    # Pequeño rastro de sangre
    blood_poly = Polygon([(12, 10), (13, 9), (12.5, 8.5), (11, 9.5)], facecolor="#4a0e17", alpha=0.6, zorder=3)
    ax.add_patch(blood_poly)
    ax.text(vesper_x + 0.5, vesper_y + 0.5, "CADÁVER VESPER\n(Silbato)", color="#ff4d4d", ha="left", va="bottom", fontsize=8, fontweight="bold", zorder=15)
    
    # 6. Símbolos de Posibles Posiciones del Carroñero (Opcional, para el GM)
    carronero_spots = [(4, 13), (12, 13), (16, 13), (4, 3)]
    for sx, sy in carronero_spots:
        ax.plot(sx, sy, marker='x', color=COLOR_DANGER, markersize=8, markeredgewidth=2, zorder=6, alpha=0.7)
    
    # 7. Título y Leyenda
    # Compass
    ax.text(2, 17, "N", color=COLOR_TEXT, fontsize=16, fontweight="bold", ha="center", va="center", zorder=15)
    ax.plot([2, 2], [16, 16.5], color=COLOR_DEBRIS_EDGE, lw=2, zorder=15)
    
    # Legend Box
    legend_box = Rectangle((0.5, 0.5), 6, 2.5, facecolor="#1f2833", alpha=0.9, edgecolor=COLOR_DEBRIS_EDGE, lw=2, zorder=15)
    ax.add_patch(legend_box)
    
    ax.text(1, 2.5, "BASE DEL MURO (TACTICO)", color="#ffffff", fontsize=10, fontweight="bold", zorder=16)
    ax.text(1, 1.2, "• 1 Casilla = 1 metro\n• X Roja = Puntos de Acecho\n• Gris = Bloqueo de Visión", color=COLOR_TEXT, fontsize=7, linespacing=1.5, zorder=16)

    # Clean axes
    ax.axis('off')
    
    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=COLOR_BG, bbox_inches='tight', dpi=300)
    print(f"Mapa táctico generado en: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_05_emboscada_base.png"
    create_base_caverna_map(output_file)
