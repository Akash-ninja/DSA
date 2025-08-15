class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # output list
        output = []

        # row and col size
        m = len(matrix)
        n = len(matrix[0])

        # pointers for iteration according to direction
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        # direction: 0: left to right, 1: top to bottom, 2: bottom to left, 3: bottom to top
        direction = 0

        # loop: iterates spirally
        while top <= bottom and left <= right:

            if direction == 0:
                # traverse: left to right
                for j in range(left, right + 1):
                    output.append(matrix[top][j])
                direction += 1
                top += 1

            elif direction == 1:
                # traverse: top to bottom
                for i in range(top, bottom + 1):
                    output.append(matrix[i][right])
                direction += 1
                right -= 1

            elif direction == 2:
                # traverse: right to left
                for j in range(right, left - 1, -1):
                    output.append(matrix[bottom][j])
                direction += 1
                bottom -= 1

            elif direction == 3:
                # traverse: bottom to top
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                direction = 0
                left += 1

        return output
