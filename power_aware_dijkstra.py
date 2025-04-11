import random
import networkx as nx

class PowerAwareGraph:
    def __init__(self, num_nodes, connection_density=0.5):
        self.num_nodes = num_nodes
        self.graph = nx.Graph()
        self.powers = {i: round(random.uniform(0.5, 2.0), 2) for i in range(num_nodes)}
        self._generate_random_edges(connection_density)

    def _generate_random_edges(self, density):
        for i in range(self.num_nodes):
            for j in range(i+1, self.num_nodes):
                if random.random() < density:
                    base_cost = round(random.uniform(1.0, 10.0), 2)
                    power_weighted_cost = round(base_cost / (self.powers[i] * self.powers[j]), 2)
                    self.graph.add_edge(i, j, weight=power_weighted_cost)

    def dijkstra(self, source):
        dist = {node: float('inf') for node in self.graph.nodes}
        dist[source] = 0
        prev = {node: None for node in self.graph.nodes}
        visited = set()
        steps = []

        while len(visited) < len(self.graph.nodes):
            u = min((node for node in self.graph.nodes if node not in visited), key=lambda x: dist[x], default=None)
            if u is None: break
            visited.add(u)
            steps.append((u, dict(dist)))
            for v in self.graph.neighbors(u):
                weight = self.graph[u][v]['weight']
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u

        paths = {node: self._reconstruct_path(prev, source, node) for node in self.graph.nodes}
        return dist, paths, steps

    def _reconstruct_path(self, prev, src, tgt):
        path = []
        while tgt is not None:
            path.insert(0, tgt)
            tgt = prev[tgt]
        return path if path[0] == src else []

    def get_graph(self):
        return self.graph

    def random_source(self):
        return random.choice(list(self.graph.nodes))
