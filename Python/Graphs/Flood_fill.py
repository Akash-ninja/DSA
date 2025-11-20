class Solution:
    def dfs(self, row, col, image, old_color, new_color):
        if (
            row < 0
            or col < 0
            or row >= len(image)
            or col >= len(image[0])
            or image[row][col] != old_color  # same as old color then no need to change
        ):
            return None

        image[row][col] = new_color
        self.dfs(row - 1, col, image, old_color, new_color)
        self.dfs(row + 1, col, image, old_color, new_color)
        self.dfs(row, col - 1, image, old_color, new_color)
        self.dfs(row, col + 1, image, old_color, new_color)

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        Approach: using graph theory dfs traversal
        """
        # if the new the color cell is same as present one
        if image[sr][sc] == color:
            return image

        # start dfs from given source row and col
        self.dfs(sr, sc, image, image[sr][sc], color)
        return image
