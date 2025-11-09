# main.py
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from src.pagerank import compute_pagerank

# Step 1: Load dataset
edges = pd.read_csv("data/network_edges.csv")

# Step 2: Create a directed graph
G = nx.from_pandas_edgelist(edges, source="source", target="target", create_using=nx.DiGraph())

# Step 3: Print basic info
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("\nNodes:", list(G.nodes()))
print("Edges:", list(G.edges()))

# Step 4: Visualize the network
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # layout for better spacing
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=1000,
    font_size=10,
    arrowsize=15,
    edge_color="gray"
)


pagerank_scores = compute_pagerank(G)
print("\n=== PageRank Scores ===")
for node, score in sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {score:.4f}")

# Step 6: Display Top 5 nodes
top5 = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 nodes by PageRank:")
for node, score in top5:
    print(f"{node}: {score:.4f}")
plt.title("Directed Social Network Graph", fontsize=14)
plt.show()