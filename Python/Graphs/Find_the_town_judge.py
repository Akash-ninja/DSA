class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Approach: Using graph theory, in-degree and out-degree of a node concept
        """
        # initialising
        in_deg = [0] * (n + 1)
        out_deg = [0] * (n + 1)

        for i in range(0, len(trust)):
            edge = trust[i]
            from_node = edge[0]
            to_node = edge[1]

            # making of in-degree and out-degree of a node in graph
            out_deg[from_node] += 1
            in_deg[to_node] += 1

        for i in range(1, n + 1):
            # if there is any node that has all incoming edges and no outgoing edge -> thats the node we are looking for
            if in_deg[i] == n - 1 and out_deg[i] == 0:
                return i

        return -1
