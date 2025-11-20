class Solution:
    def __init__(self):
        self.grid = []

    def isValid(self, row, col):
        # checks validity of rows and cols
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]):
            return False

        if self.grid[row][col] == "1":
            return True

        return False

    def dfs(self, row, col):
        if self.isValid(row, col):
            # once traverse, mark it as '2' for referring it as visited
            self.grid[row][col] = "2"

            # traverse left, right, up and down
            self.dfs(row + 1, col)
            self.dfs(row - 1, col)
            self.dfs(row, col + 1)
            self.dfs(row, col - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach: solution using DFS traversal
        """
        self.grid = grid  # sets grid globally

        island_count = 0  # answer

        row = len(grid)
        col = len(grid[0])

        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == "1":
                    island_count += 1
                    # traverse 1s through dfs
                    self.dfs(i, j)

        return island_count
