# PageRank & HITS – Ranking Webpages and Influencers

## 📘 Overview
This project implements two fundamental link analysis algorithms — **PageRank** and **HITS (Hyperlink-Induced Topic Search)** — to identify and rank the most important and influential nodes in a directed network.

The goal is to simulate how search engines and recommendation systems rank **webpages, research papers, or social media influencers** based on their interconnections.

---

## 🎯 Objectives
- Represent a real or synthetic **directed network** using an edge list (CSV).
- Compute **PageRank** values with a damping factor (E = 0.15).
- Compute **HITS** authority and hub scores iteratively until convergence.
- Visualize the network using:
  - Matplotlib (static visualization)
  - Plotly (interactive browser visualization with hover scores)

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies
Make sure Python (≥3.10) is installed, then run:

```bash
"pip install -r requirements.txt"