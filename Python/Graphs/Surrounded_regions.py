class Solution:
    def dfs(self, row, col, board):
        #
        if (
            row >= 0
            and col >= 0
            and row < len(board)
            and col < len(board[0])
            and board[row][col] == "P"
        ):
            board[row][col] = "O"
            self.dfs(row - 1, col, board)
            self.dfs(row + 1, col, board)
            self.dfs(row, col - 1, board)
            self.dfs(row, col + 1, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Uses graph theory DFS traversal
        """
        row = len(board)
        col = len(board[0])

        # 1. convert all the 'O' to 'P'
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == "O":
                    board[i][j] = "P"

        # 2. traverse boundary attached 'O' and convert to 'P'
        # 1st row
        for j in range(0, col):
            self.dfs(0, j, board)

        # last row
        for j in range(0, col):
            self.dfs(row - 1, j, board)

        # 1st col
        for i in range(0, row):
            self.dfs(i, 0, board)

        # last col
        for i in range(0, row):
            self.dfs(i, col - 1, board)

        # 3. converted left over P's to 'X' (captured)
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == "P":
                    board[i][j] = "X"
