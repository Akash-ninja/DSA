class Solution:
    def isSafe(self, board, row, col):
        # checks upward column
        for i in range(0, row):
            if board[i][col] == "Q":
                return False

        # checks upward diagonal left
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # checks upward diagonal right
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtrack(self, board, row, solutions):
        """
        Main placing of queen logic sits here -
        Iterates the board column-wise then places the queen row-wise
        1. iteration done in a column fashion
        2. checks whether it is safe to place queens
        3. places the queen
        4. increments row and does the same thing row-wise
        5. discards if combination is wrong and undo to original board and repeats until iteration reaches the last row
        """
        n = len(board)

        # base condition
        if row == n:
            temp = []
            for i in range(0, row):
                temp.append("".join(board[i]))

            solutions.append(temp)
            return
        else:
            # 1
            for col in range(0, n):
                if self.isSafe(board, row, col):
                    board[row][col] = "Q"
                    self.backtrack(board, row + 1, solutions)  # recursive call
                    board[row][col] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Approach: Placing queens using backtracking method
        """
        # init
        solutions = []
        row = n
        board = [["." for col in range(n)] for row in range(n)]

        # invoke
        self.backtrack(board, 0, solutions)

        return solutions
