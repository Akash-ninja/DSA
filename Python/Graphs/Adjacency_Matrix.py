class MatrixGraph:
    def __init__(self, nodes, directed=False):
        self.adj_matrix = []
        self.adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.adj_matrix[u][v] = weight
        if not self.directed:
            self.adj_matrix[v][u] = weight

    def print_graph(self):
        print(self.adj_matrix)


graph = MatrixGraph(4)

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

graph.print_graph()
