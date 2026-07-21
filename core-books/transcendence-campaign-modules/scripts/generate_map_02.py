import matplotlib.pyplot as plt
import networkx as nx
import os

def create_pointcrawl_map(output_path):
    # Setup graph
    G = nx.Graph()
    
    # Define nodes with categories for coloring
    nodes = {
        # NODO 1: Sumidero Quirúrgico
        "Túnel de Escape\n(Inicio)": {"pos": (0, 0), "cat": "start"},
        "El Mar de Ácido\n(Ruta Baja)": {"pos": (2, -1.5), "cat": "hazard"},
        "Puente de Hueso\n(Ruta Alta)": {"pos": (2, 1.5), "cat": "path"},
        "Cráter Central\n(Zona Cero)": {"pos": (4, 0), "cat": "danger"},
        
        # NODO 2: Nave de Drenaje (Matadero)
        "Entrada al\nMatadero": {"pos": (6, 0), "cat": "path"},
        "Bosque de Cadenas\n(Combate)": {"pos": (8, 1), "cat": "combat"},
        "Cabina del\nSupervisor": {"pos": (10, 2), "cat": "loot"},
        "Cruce del\nSótano": {"pos": (10, 0), "cat": "path"},
        "Filtros de Sangre\n(Exploración)": {"pos": (8, -1.5), "cat": "path"},
        
        # NODO 3: Anfiteatros
        "Fosas Quirúrgicas\n(Dilema)": {"pos": (12, -1.5), "cat": "story"},
        "Bóveda de Resina": {"pos": (12, -3), "cat": "loot"},
        
        # NODO 4: La Esclusa
        "Válvulas\nNeumáticas": {"pos": (14, 0), "cat": "puzzle"},
        "La Gran Esclusa\n(Salida)": {"pos": (16, 0), "cat": "exit"}
    }
    
    # Add nodes to graph
    for node, data in nodes.items():
        G.add_node(node, pos=data["pos"], cat=data["cat"])
        
    # Define edges (connections)
    edges = [
        ("Túnel de Escape\n(Inicio)", "El Mar de Ácido\n(Ruta Baja)"),
        ("Túnel de Escape\n(Inicio)", "Puente de Hueso\n(Ruta Alta)"),
        ("El Mar de Ácido\n(Ruta Baja)", "Cráter Central\n(Zona Cero)"),
        ("Puente de Hueso\n(Ruta Alta)", "Cráter Central\n(Zona Cero)"),
        ("El Mar de Ácido\n(Ruta Baja)", "Entrada al\nMatadero"),
        ("Puente de Hueso\n(Ruta Alta)", "Entrada al\nMatadero"),
        ("Cráter Central\n(Zona Cero)", "Entrada al\nMatadero"),
        
        ("Entrada al\nMatadero", "Bosque de Cadenas\n(Combate)"),
        ("Bosque de Cadenas\n(Combate)", "Cabina del\nSupervisor"),
        ("Cabina del\nSupervisor", "Cruce del\nSótano"),
        ("Cruce del\nSótano", "Filtros de Sangre\n(Exploración)"),
        ("Cruce del\nSótano", "Fosas Quirúrgicas\n(Dilema)"),
        ("Filtros de Sangre\n(Exploración)", "Bóveda de Resina"),
        ("Filtros de Sangre\n(Exploración)", "Fosas Quirúrgicas\n(Dilema)"),
        
        ("Bóveda de Resina", "Válvulas\nNeumáticas"),
        
        ("Válvulas\nNeumáticas", "La Gran Esclusa\n(Salida)")
    ]
    G.add_edges_from(edges)
    
    # Extract positions
    pos = nx.get_node_attributes(G, 'pos')
    
    # Define color palette
    colors = {
        "start": "#5c5c8a", # grayish blue
        "path": "#2a2a35",  # dark grey
        "hazard": "#4a4a20", # sickly green/brown
        "danger": "#4a0e17", # deep red
        "combat": "#6b1a22", # bright red
        "loot": "#b8860b",   # dark gold
        "story": "#4b0082",  # indigo
        "puzzle": "#2f4f4f", # slate
        "exit": "#1a5b82"    # dark blue (safety/exit)
    }
    
    # Map node categories to colors
    node_colors = [colors[G.nodes[n]['cat']] for n in G.nodes()]
    
    # Create plot
    plt.figure(figsize=(16, 9), facecolor="#050508")
    ax = plt.gca()
    ax.set_facecolor("#050508")
    
    # Draw edges (lines)
    nx.draw_networkx_edges(G, pos, edge_color="#3a3a4a", width=2, alpha=0.7)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000, 
                           edgecolors="#7a7a8a", linewidths=1.5)
    
    # Draw labels
    # Adjust y position for labels to appear below nodes slightly or centered
    label_pos = {k: (v[0], v[1]-0.3) for k, v in pos.items()}
    nx.draw_networkx_labels(G, pos, font_size=9, font_color="white", 
                            font_family="sans-serif", font_weight="bold")
    
    # Add title
    plt.title("NIVEL 2: EL DISTRITO INDUSTRIAL (POINTCRAWL)", color="white", fontsize=18, fontweight="bold", pad=20)
    
    # Remove margins and axes
    plt.margins(0.1)
    plt.axis("off")
    
    # Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor="#050508", bbox_inches='tight', dpi=300)
    print(f"Mapa Pointcrawl generado exitosamente en: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_02.png"
    create_pointcrawl_map(output_file)
