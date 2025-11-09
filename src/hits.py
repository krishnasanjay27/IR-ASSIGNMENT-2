# src/hits.py
import math

def compute_hits(G, tol=1e-4, max_iter=2):
    """
    Compute HITS (Authority and Hub) scores iteratively for a directed graph.
    :param G: Directed graph (NetworkX DiGraph)
    :param tol: Convergence tolerance
    :param max_iter: Max number of iterations
    :return: Two dictionaries: authority_scores, hub_scores
    """
    nodes = list(G.nodes())
    N = len(nodes)
    
    # Step 1: Initialize authority and hub values to 1
    authority = {node: 1.0 for node in nodes}
    hub = {node: 1.0 for node in nodes}

    # Step 2: Iterate until convergence
    for _ in range(max_iter):
        new_authority = {}
        new_hub = {}

        # Update authority: sum of hub values of incoming nodes
        for node in nodes:
            new_authority[node] = sum(hub[n] for n in G.predecessors(node))

        # Update hub: sum of authority values of outgoing nodes
        for node in nodes:
            new_hub[node] = sum(authority[n] for n in G.successors(node))

        # Normalize authority and hub values
        norm_auth = (sum(v for v in new_authority.values()))
        norm_hub = (sum(v for v in new_hub.values()))

        for node in nodes:
            if norm_auth != 0:
                new_authority[node] /= norm_auth
            if norm_hub != 0:
                new_hub[node] /= norm_hub

        # Check for convergence
        diff = sum(abs(new_authority[n] - authority[n]) + abs(new_hub[n] - hub[n]) for n in nodes)
        if diff < tol:
            break

        authority = new_authority
        hub = new_hub

    return authority, hub
