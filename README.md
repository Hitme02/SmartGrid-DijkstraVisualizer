# ⚡ SmartGrid Dijkstra Visualizer

A Streamlit-based interactive dashboard that compares Standard Dijkstra and Power-Aware Dijkstra algorithms for optimal energy routing in smart grid systems.

---

## 🚀 Features

- 🔍 Dual Graph View (Standard vs Power-Aware)
- 🧭 Traversal Animation
- 🔁 Shortest Path Highlight Toggle
- ➕ Live Node Addition
- 📊 Cost Comparison Charts (% improvement)
- 📥 CSV Export of Metrics

---

## ⚖️ Standard Dijkstra vs Power-Aware Dijkstra — What's the Difference?

Imagine you're finding the fastest route from your house to all other houses in a city.

- 🧭 **Standard Dijkstra**  
  Just finds the shortest path in terms of distance.  
  It doesn’t care about traffic, road conditions, or energy availability — it just looks for the lowest number.

- ⚡ **Power-Aware Dijkstra**  
  It still tries to find the best path, but it also checks how much "power" is available on each road.  
  If a path has low energy availability (like a weak or unstable energy line), it avoids it — even if it’s shorter.  
  This is more realistic in smart grids where we care about power flow and stability.

---

### 💡 How It's Used in This Dashboard

- Both algorithms start from the same source node.
- They calculate the shortest paths to all other nodes.
- This dashboard helps you compare:
  - 🟦 The cost to reach each node (Standard vs Power-Aware)
  - 📈 How much improvement (or loss) is observed with power-awareness
  - ⏱ Execution time to evaluate performance
- Visualizations include:
  - Bar charts 📊 comparing costs and improvements
  - Percentage improvement calculations 🔢
  - Step-by-step traversal animations 🧭

---

## 📁 Project Structure

```
SmartGrid-DijkstraVisualizer/
├── streamlit_dijkstra_dashboard.py       # Main Streamlit app
├── standard_dijkstra.py                  # Standard Dijkstra logic
├── power_aware_dijkstra.py               # Power-aware Dijkstra logic
├── requirements.txt                      # Dependencies
├── README.md                             # This file
└── .gitignore                            # (Optional) Git exclusions
```

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/SmartGrid-DijkstraVisualizer.git
cd SmartGrid-DijkstraVisualizer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run streamlit_dijkstra_dashboard.py
```

Then open the local URL shown in the terminal (usually http://localhost:8501).

---

## 💡 Usage

- Use the sidebar to control number of nodes and graph density.
- View graphs and step-by-step animations of Dijkstra’s traversal.
- Toggle between standard and power-aware routing modes.
- Add new nodes live, export costs to CSV, and observe improvement.
