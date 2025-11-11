# src/interactive_visualize.py
import plotly.io as pio
pio.renderers.default = "browser"   # ✅ ensures graphs open in your system browser (e.g., Chrome)

import plotly.graph_objects as go
import networkx as nx

def plot_interactive_graph(G, scores, score_label="Score", color="blue", title="Interactive Graph"):
    """
    Create an interactive network visualization using Plotly.
    Hovering over each node shows its score.
    Opens automatically in your default browser (e.g., Chrome).
    """

    # === Layout for nodes ===
    pos = nx.spring_layout(G, seed=42)

    # Node positions
    x_nodes = [pos[node][0] for node in G.nodes()]
    y_nodes = [pos[node][1] for node in G.nodes()]

    # === Edge coordinates ===
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    # === Edge trace ===
    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines"
    )

    # === Node trace ===
    node_text = [f"{node}<br>{score_label}: {scores[node]:.4f}" for node in G.nodes()]

    node_trace = go.Scatter(
        x=x_nodes,
        y=y_nodes,
        mode="markers+text",
        text=list(G.nodes()),
        textposition="top center",
        hoverinfo="text",
        hovertext=node_text,
        marker=dict(
            showscale=True,
            colorscale="Blues",
            color=[scores[node] for node in G.nodes()],
            size=[30 + 100 * scores[node] for node in G.nodes()],
            colorbar=dict(
                thickness=15,
                title=dict(text=f"{score_label} Value", side="right"),
                xanchor="left"
            ),
            line_width=2
        )
    )

    # === Figure layout ===
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=dict(
                text=title,
                font=dict(size=16)
            ),
            showlegend=False,
            hovermode="closest",
            margin=dict(b=0, l=0, r=0, t=40),
            annotations=[
                dict(
                    text="Interactive Network Visualization",
                    showarrow=False,
                    xref="paper",
                    yref="paper",
                    x=0.005,
                    y=-0.002
                )
            ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
    )

    # === Show in browser ===
    fig.show()
