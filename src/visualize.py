# src/visualize.py
import matplotlib.pyplot as plt
import networkx as nx

def plot_multiple_graphs(G, pagerank_scores, authority_scores, hub_scores):
    """
    Plot three separate graphs:
    1. PageRank visualization (size ∝ PR, blue circles)
    2. Authority visualization (size ∝ authority, red squares)
    3. Hub visualization (size ∝ hub, green triangles)
    """

    # Common layout (so all three have same positioning)
    pos = nx.spring_layout(G, seed=42, k=0.6)

    plt.figure(figsize=(18, 6))
    plt.suptitle("PageRank and HITS Visualizations", fontsize=16, y=0.98)

    # === 1️⃣ PageRank Graph ===
    plt.subplot(1, 3, 1)
    node_sizes_pr = [6000 * pagerank_scores[node] for node in G.nodes()]
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="skyblue",
        node_size=node_sizes_pr,
        edge_color="gray",
        arrows=True,
        arrowsize=12,
        font_weight="bold"
    )
    plt.title("PageRank (Size ∝ Importance)", fontsize=12)

    # === 2️⃣ Authority Graph ===
    plt.subplot(1, 3, 2)
    node_sizes_auth = [6000 * authority_scores[node] for node in G.nodes()]
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightcoral",
        node_shape="s",  # square
        node_size=node_sizes_auth,
        edge_color="gray",
        arrows=True,
        arrowsize=12,
        font_weight="bold"
    )
    plt.title("HITS - Authority Scores (Red Squares)", fontsize=12)

    # === 3️⃣ Hub Graph ===
    plt.subplot(1, 3, 3)
    node_sizes_hub = [6000 * hub_scores[node] for node in G.nodes()]
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightgreen",
        node_shape="^",  # triangle
        node_size=node_sizes_hub,
        edge_color="gray",
        arrows=True,
        arrowsize=12,
        font_weight="bold"
    )
    plt.title("HITS - Hub Scores (Green Triangles)", fontsize=12)

    plt.tight_layout()
    plt.show()
