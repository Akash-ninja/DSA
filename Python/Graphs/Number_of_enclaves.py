class Solution:
    def dfs(self, row, col, grid):
        if (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == 1
        ):
            grid[row][col] = 0
            self.dfs(row + 1, col, grid)
            self.dfs(row - 1, col, grid)
            self.dfs(row, col - 1, grid)
            self.dfs(row, col + 1, grid)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Approach: DFS traversal (see surrounded regions problem for hint)
        """
        row = len(grid)
        col = len(grid[0])

        # 1. traverse and convert boundary 1's to 0
        for j in range(0, col):
            self.dfs(0, j, grid)
            self.dfs(row - 1, j, grid)

        for i in range(0, row):
            self.dfs(i, 0, grid)
            self.dfs(i, col - 1, grid)

        # 2. Count the left over(non-boundary) 1's
        num_of_enclaves = 0
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1:
                    num_of_enclaves += 1

        return num_of_enclaves
