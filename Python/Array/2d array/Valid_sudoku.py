import math


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Init: 9 rows need 9 sets of rows
        row_set = [0] * 9
        col_set = [0] * 9
        grid_set = [0] * 9

        # Init: setting all sets
        for i in range(9):
            row_set[i] = {0}
            col_set[i] = {0}
            grid_set[i] = {0}

        # Scan the board and check in the set and if not present then add
        for i in range(9):
            for j in range(9):
                value = board[i][j]

                # No value, ignore it
                if value == ".":
                    continue

                # calculate grid no.
                grid_no = math.floor(i / 3) * 3 + math.floor(j / 3)

                isPresentInRow = value in row_set[i]
                isPresentInCol = value in col_set[j]
                isPresentInGrid = value in grid_set[grid_no]

                if isPresentInRow or isPresentInCol or isPresentInGrid:
                    return False

                row_set[i].add(value)
                col_set[j].add(value)
                grid_set[grid_no].add(value)

        return True
