import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import time

from standard_dijkstra import SmartGridGraph as StdGraph
from power_aware_dijkstra import PowerAwareGraph as PowerGraph

# Streamlit Page Config
st.set_page_config(layout='wide', page_title='⚡ SmartGrid: Dijkstra Comparison Dashboard')
st.title("⚡ SmartGrid: Dijkstra Comparison Dashboard")

# Sidebar Configuration
st.sidebar.header("⚙️ Configuration")
num_nodes = st.sidebar.slider("Number of Nodes", 5, 20, 10)
density = st.sidebar.slider("Connection Density", 0.2, 1.0, 0.4)
highlight_path = st.sidebar.checkbox("🔦 Highlight Shortest Path", value=False)

# Initialize Session State
if "std_graph" not in st.session_state:
    st.session_state.std_graph = StdGraph(num_nodes, density)
if "pow_graph" not in st.session_state:
    st.session_state.pow_graph = PowerGraph(num_nodes, density)

# Generate Random Graphs
def regenerate_graphs():
    st.session_state.std_graph = StdGraph(num_nodes, density)
    st.session_state.pow_graph = PowerGraph(num_nodes, density)

if st.sidebar.button("🔁 Regenerate Graphs"):
    regenerate_graphs()

# Live Node Addition
with st.sidebar.expander("➕ Add New Node"):
    new_node = st.number_input("Node ID", min_value=num_nodes, step=1)
    target_node = st.number_input("Connect to Node", min_value=0, max_value=new_node-1, step=1)
    weight = st.number_input("Edge Weight", min_value=1.0, value=5.0)

    if st.button("Add Node to Graph"):
        st.session_state.std_graph.add_node(new_node)
        st.session_state.pow_graph.add_node(new_node)
        st.session_state.std_graph.add_edge(new_node, target_node, weight)
        st.session_state.pow_graph.add_edge(new_node, target_node, weight)

# Dijkstra Execution
def run_dijkstra(graph_obj, source):
    start = time.time()
    dist, paths, steps = graph_obj.dijkstra(source)
    end = time.time()
    return dist, paths, steps, graph_obj.get_graph(), round(end - start, 6)

available_nodes = list(st.session_state.std_graph.get_graph().nodes())
source_node = st.selectbox("📍 Select Source Node", available_nodes, index=0)
dest_node = st.selectbox("🎯 Select Destination Node", available_nodes, index=min(1, len(available_nodes)-1))

std_dist, std_paths, std_steps, std_nx, std_time = run_dijkstra(st.session_state.std_graph, source_node)
pow_dist, pow_paths, pow_steps, pow_nx, pow_time = run_dijkstra(st.session_state.pow_graph, source_node)

# Draw Graphs
col1, col2 = st.columns(2)
with col1:
    st.subheader("📘 Standard Dijkstra Graph")
    fig, ax = plt.subplots()
    pos = nx.spring_layout(std_nx)
    nx.draw(std_nx, pos, with_labels=True, node_color='skyblue', ax=ax)
    nx.draw_networkx_edge_labels(std_nx, pos, edge_labels={(u, v): d['weight'] for u, v, d in std_nx.edges(data=True)}, ax=ax)
    if highlight_path and dest_node in std_paths:
        path = std_paths[dest_node]
        nx.draw_networkx_edges(std_nx, pos, edgelist=list(zip(path, path[1:])), width=3, edge_color='red', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("🔋 Power-Aware Dijkstra Graph")
    fig2, ax2 = plt.subplots()
    pos2 = nx.spring_layout(pow_nx)
    nx.draw(pow_nx, pos2, with_labels=True, node_color='lightgreen', ax=ax2)
    nx.draw_networkx_edge_labels(pow_nx, pos2, edge_labels={(u, v): round(d['weight'], 2) for u, v, d in pow_nx.edges(data=True)}, ax=ax2)
    if highlight_path and dest_node in pow_paths:
        path2 = pow_paths[dest_node]
        nx.draw_networkx_edges(pow_nx, pos2, edgelist=list(zip(path2, path2[1:])), width=3, edge_color='purple', ax=ax2)
    st.pyplot(fig2)

# Comparison Results
st.markdown("### 📊 Dijkstra Comparison Metrics")
st.markdown(f"✅ **Standard Source:** {source_node} | ⏱️ Time: `{std_time}s`")
st.markdown(f"✅ **Power-Aware Source:** {source_node} | ⏱️ Time: `{pow_time}s`")

df = pd.DataFrame({
    "Node": std_dist.keys(),
    "Standard Cost": std_dist.values(),
    "Power-Aware Cost": [pow_dist.get(k, float('inf')) for k in std_dist.keys()]
})
df["% Improvement"] = ((df["Standard Cost"] - df["Power-Aware Cost"]) / df["Standard Cost"]) * 100

st.subheader("📈 Path Cost Comparison")
st.bar_chart(df.set_index("Node")[["Standard Cost", "Power-Aware Cost"]])

st.subheader("📉 % Improvement Over Standard")
st.bar_chart(df.set_index("Node")[["% Improvement"]])

csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download CSV", csv, "dijkstra_comparison.csv", "text/csv")

# Traversal Animation
st.markdown("### 🧭 Standard Dijkstra Traversal Animation")
step = st.slider("Step", 0, len(std_steps)-1, 0, key="std_step")
st.json({"Visited": std_steps[step][0], "Distances": std_steps[step][1]})

st.markdown("### 🧭 Power-Aware Dijkstra Traversal Animation")
step2 = st.slider("Step (Power-Aware)", 0, len(pow_steps)-1, 0, key="pow_step")
st.json({"Visited": pow_steps[step2][0], "Distances": pow_steps[step2][1]})
