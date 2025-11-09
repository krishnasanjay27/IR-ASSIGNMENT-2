# src/visualize.py
import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G, pagerank_scores, authority_scores, hub_scores):
    """
    Visualize the directed graph with PageRank, Authority, and Hub highlights.
    """
    # Determine top authorities and hubs (top 5 each)
    top_authorities = sorted(authority_scores, key=authority_scores.get, reverse=True)[:5]
    top_hubs = sorted(hub_scores, key=hub_scores.get, reverse=True)[:5]

    # Node sizes based on PageRank
    node_sizes = [5000 * pagerank_scores[node] for node in G.nodes()]

    # Node colors based on category
    node_colors = []
    for node in G.nodes():
        if node in top_authorities:
            node_colors.append("green")
        elif node in top_hubs:
            node_colors.append("red")
        else:
            node_colors.append("lightblue")

    # Layout and draw
    plt.figure(figsize=(9, 7))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=node_sizes,
        font_size=10,
        arrowsize=15,
        edge_color="gray"
    )

    plt.title("Network Visualization — PageRank, Hubs, and Authorities", fontsize=14)
    plt.savefig("results/network_plot.png", dpi=300, bbox_inches="tight")
    plt.show()
