class Solution:
    def __init__(self):
        self.adj_list = []
        self.state = []
        self.cycle_found = False

    def dfs(self, node):
        if self.state[node] == "U":
            self.state[node] = "V"

            # fetch the neighbour node from adjacency list
            neighbours = self.adj_list[node]

            # traverse the neighbour
            for nei in range(0, len(neighbours)):
                self.dfs(neighbours[nei])

            # mark the node as processed
            self.state[node] = "P"

        elif self.state[node] == "V":
            # if it reaches same visited node then a cycle is detected
            self.cycle_found = True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach: takes the help of Topological ordering of graph
        """
        self.state = ["U"] * numCourses
        self.adj_list = [[] for _ in range(0, numCourses)]

        # forms adjacency list
        for i in range(0, len(prerequisites)):
            edge_point = prerequisites[i]
            from_node = edge_point[1]
            to_node = edge_point[0]

            self.adj_list[from_node].append(to_node)

        # traverse the graph via DFS and detects back edge
        for i in range(0, numCourses):
            if self.state[i] == "U":
                self.dfs(i)

            if self.cycle_found:
                return False

        return not self.cycle_found
