# main.py
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from src.pagerank import compute_pagerank
from src.hits import compute_hits
from src.visualize import plot_multiple_graphs
from src.interactive_visualize import plot_interactive_graph  # ✅ new import for Plotly hover graphs

# Step 1: Load dataset
edges = pd.read_csv("data/network_edges.csv")

# Step 2: Create a directed graph
G = nx.from_pandas_edgelist(edges, source="source", target="target", create_using=nx.DiGraph())

# Step 3: Print basic info
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("\nNodes:", list(G.nodes()))
print("Edges:", list(G.edges()))

# Step 5: Compute PageRank
pagerank_scores = compute_pagerank(G)
print("\n=== PageRank Scores ===")
for node, score in sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {score:.4f}")

# Step 6: Display Top 5 nodes by PageRank
top5 = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 nodes by PageRank:")
for node, score in top5:
    print(f"{node}: {score:.4f}")

# Step 7: Compute HITS
authority_scores, hub_scores = compute_hits(G)

print("\n=== HITS: Authority Scores ===")
for node, score in sorted(authority_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {score:.4f}")

print("\n=== HITS: Hub Scores ===")
for node, score in sorted(hub_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {score:.4f}")

# Step 8: Display top 5 authorities and hubs
top5_authorities = sorted(authority_scores.items(), key=lambda x: x[1], reverse=True)[:5]
top5_hubs = sorted(hub_scores.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 Authorities:")
for node, score in top5_authorities:
    print(f"{node}: {score:.4f}")

print("\nTop 5 Hubs:")
for node, score in top5_hubs:
    print(f"{node}: {score:.4f}")

# Step 9: Three separate static visualizations (Matplotlib)
print("\nDisplaying static visualizations for PageRank, Authority, and Hub Scores...")
plot_multiple_graphs(G, pagerank_scores, authority_scores, hub_scores)

# Step 10: Interactive hover visualizations (Plotly)
print("\nDisplaying interactive hover visualizations...")

# Interactive PageRank Graph
plot_interactive_graph(G, pagerank_scores, score_label="PageRank", color="blue", title="Interactive PageRank Graph")

# Interactive Authority Graph
plot_interactive_graph(G, authority_scores, score_label="Authority", color="red", title="Interactive HITS - Authority Graph")

# Interactive Hub Graph
plot_interactive_graph(G, hub_scores, score_label="Hub", color="green", title="Interactive HITS - Hub Graph")
