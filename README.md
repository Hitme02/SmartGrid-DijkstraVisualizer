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
