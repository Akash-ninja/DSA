class UnweightedGraph:
    def __init__(self, nodes, directed=False):
        self.adj_list = [[] for _ in range(nodes)]
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def bfs(self):
        visited = {}
        nodes = len(self.adj_list)
        for i in range(0, nodes):
            visited[i] = False

        for i in range(0, nodes):
            # traverse through each non-visited node
            if not visited[i]:
                visited[i] = True
                self.bfs_core(i, visited)
        print()

    def bfs_core(self, x, visited: dict):
        queue = []
        queue.append(x)  # 1. enqueue into queue
        visited[x] = True  # 2. mark as visited

        while queue:  # 3. loop until queue is empty
            node = queue.pop(0)
            print(node, end=" ")

            # 4. traverse through each unvisited neighbor
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self):
        visited = {}
        nodes = len(self.adj_list)
        for i in range(0, nodes):
            visited[i] = False

        for i in range(0, nodes):
            # traverse through each non-visited node
            if not visited[i]:
                visited[i] = True
                self._dfs_core_iterative(i, visited)
        print()

    def _dfs_core_iterative(self, x, visited: dict):
        stack = []
        stack.append(x)  # 1. push into the stack

        while stack:  # 3. loop until stack is empty
            node = stack[-1]  # gets the topmost element from the stack
            print(node, end=" ")
            stack.pop()

            # 4. traverse through each unvisited neighbor
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

    def dfs_recursive(self):
        visited = {}
        nodes = len(self.adj_list)
        for i in range(0, nodes):
            visited[i] = False

        for i in range(0, nodes):
            # traverse through each non-visited node
            if not visited[i]:
                self._dfs_core_recursive(i, visited)
        print()

    def _dfs_core_recursive(self, x, visited: dict):
        if not visited.get(x):
            visited[x] = True
            print(x, end=" ")

            for nei in self.adj_list[x]:
                if not visited[nei]:
                    self._dfs_core_recursive(nei, visited)

    # When you try to visit a node, the node can be in either of 3 states
    # States used to detect_cycle 'U', 'V' and 'P', U = Unprocessed, V = Visited and P = Processed
    def detect_cycle(self):
        state = {}
        nodes = len(self.adj_list)

        for i in range(0, nodes):
            state[i] = "U"

        for i in range(0, nodes):
            if state.get(i) == "U":
                self._detect_cycle_core(i, state)
        print()

    def _detect_cycle_core(self, x, state):
        if state.get(x) == "U":
            state[x] = "V"
            print(x, end=" ")

            for nei in self.adj_list[x]:
                self._detect_cycle_core(nei, state)

            # once the node's neighbors are visited
            state[x] = "P"

        elif state.get(x) == "V":
            print(f"\nCycle found at node {x}")
            break

    def print_graph(self):
        print(self.adj_list)


# graph for BFS, 2 connected components
# graph = UnweightedGraph(7)
# graph.add_edge(0, 1)
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
# graph.add_edge(3, 1)
# graph.add_edge(4, 5)
# graph.add_edge(5, 6)

# graph.print_graph()

# graph.bfs()

# graph for DFS
# graph = UnweightedGraph(7)
# graph.add_edge(0, 1)
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
# graph.add_edge(2, 5)  # extra edge added
# graph.add_edge(3, 1)
# graph.add_edge(4, 5)
# graph.add_edge(5, 6)

# graph.print_graph()

# graph.dfs()
# graph.dfs_recursive()


graph = UnweightedGraph(4, directed=True)
graph.add_edge(0, 1)
graph.add_edge(2, 1)
graph.add_edge(1, 3)
graph.add_edge(3, 2)

graph.print_graph()

graph.detect_cycle()
