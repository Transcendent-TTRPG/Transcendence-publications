import matplotlib.pyplot as plt
import networkx as nx
import os

def create_pointcrawl_map(output_path):
    # Setup graph
    G = nx.Graph()
    
    # Define nodes with categories for coloring
    nodes = {
        "Esclusa de Cuarentena\n(Entrada)": {"pos": (0, 0), "cat": "start"},
        
        "Suburbios Colmena\n(Fango Acústico)": {"pos": (3, 0), "cat": "danger"},
        "Mercado de Carne\n(Callejón)": {"pos": (3, -2), "cat": "loot"},
        
        "Jardines de Cultivo\n(Flora Abisal)": {"pos": (6, 0), "cat": "hazard"},
        "Anfiteatro de\nVeneración": {"pos": (9, 0), "cat": "combat"},
        
        "Agujas del\nDirectorio": {"pos": (12, 0), "cat": "story"},
        "Clínica de Pureza\n(Exploración)": {"pos": (12, 2), "cat": "loot"},
        
        "Elevador del Trono\n(Salida)": {"pos": (15, 0), "cat": "exit"}
    }
    
    # Add nodes to graph
    for node, data in nodes.items():
        G.add_node(node, pos=data["pos"], cat=data["cat"])
        
    # Define edges (connections)
    edges = [
        ("Esclusa de Cuarentena\n(Entrada)", "Suburbios Colmena\n(Fango Acústico)"),
        ("Suburbios Colmena\n(Fango Acústico)", "Mercado de Carne\n(Callejón)"),
        ("Suburbios Colmena\n(Fango Acústico)", "Jardines de Cultivo\n(Flora Abisal)"),
        ("Jardines de Cultivo\n(Flora Abisal)", "Anfiteatro de\nVeneración"),
        ("Anfiteatro de\nVeneración", "Agujas del\nDirectorio"),
        ("Agujas del\nDirectorio", "Clínica de Pureza\n(Exploración)"),
        ("Agujas del\nDirectorio", "Elevador del Trono\n(Salida)")
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
    plt.figure(figsize=(16, 6), facecolor="#050508")
    ax = plt.gca()
    ax.set_facecolor("#050508")
    
    # Draw edges (lines)
    nx.draw_networkx_edges(G, pos, edge_color="#3a3a4a", width=2, alpha=0.7)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000, 
                           edgecolors="#7a7a8a", linewidths=1.5)
    
    # Draw labels
    # Adjust y position for labels to appear centered
    nx.draw_networkx_labels(G, pos, font_size=9, font_color="white", 
                            font_family="sans-serif", font_weight="bold")
    
    # Add title
    plt.title("ACTO 3: EL DISTRITO RESIDENCIAL (MACRO MAPA)", color="white", fontsize=18, fontweight="bold", pad=20)
    
    # Remove margins and axes
    plt.margins(0.1)
    plt.axis("off")
    
    # Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor="#050508", bbox_inches='tight', dpi=300)
    print(f"Mapa Pointcrawl generado exitosamente en: {output_path}")

if __name__ == "__main__":
    output_file = "/Users/juangomez/Transcendence-workspace/Transcendence-publications/core-books/transcendence-corebook/assets/maps/mapa_10_distrito_residencial.png"
    create_pointcrawl_map(output_file)
