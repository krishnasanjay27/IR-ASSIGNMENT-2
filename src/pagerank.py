# src/pagerank.py
import networkx as nx

def compute_pagerank(G, d=0.85, tol=1e-4, max_iter=100):
    """
    Compute PageRank values iteratively for a directed graph.
    :param G: Directed graph (NetworkX DiGraph)
    :param d: Damping factor (default 0.85)
    :param tol: Convergence tolerance
    :param max_iter: Max number of iterations
    :return: Dictionary of {node: PageRank value}
    """
    N = len(G)
    if N == 0:
        return {}

    # Step 1: Initialize all PageRank values equally
    pr = {node: 1 / N for node in G.nodes()}

    # Step 2: Iterate until convergence
    for _ in range(max_iter):
        new_pr = {}
        for node in G.nodes():
            incoming_nodes = list(G.predecessors(node))
            rank_sum = 0
            for j in incoming_nodes:
                out_degree = G.out_degree(j)
                if out_degree > 0:
                    rank_sum += pr[j] / out_degree
            new_pr[node] = (1 - d) / N + d * rank_sum

        # Step 3: Check convergence
        diff = sum(abs(new_pr[n] - pr[n]) for n in G.nodes())
        if diff < tol:
            break
        pr = new_pr

    return pr
