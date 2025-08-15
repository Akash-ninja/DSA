class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = False
        first_col = False

        row = len(matrix)
        col = len(matrix[0])

        # mark first row
        for j in range(col):
            if matrix[0][j] == 0:
                first_row = True
                break

        # mark first column
        for i in range(row):
            if matrix[i][0] == 0:
                first_col = True
                break

        # Main loop: Starts from (1,1)
        # mark rows and column to set 0's
        for i in range(1, row):
            for j in range(1, col):
                # print(i,j)
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Setting 0's here:
        # By chekcing their heads (row or col's first row)
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # sets 0 in first row
        for j in range(col):
            if first_row:
                matrix[0][j] = 0

        # sets 0 in first col
        for i in range(row):
            if first_col:
                matrix[i][0] = 0
