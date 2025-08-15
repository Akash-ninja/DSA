class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        right[n - 1] = height[n - 1]

        # left[i] = stores max value from left side till i-th index
        for i in range(1, n - 1):
            left[i] = max(left[i - 1], height[i])

        # right[j] = stores max value from right side till j-th index
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])

        trapped_water = 0
        # trapped_water = Min. height from both side - height of the building itself
        for i in range(1, n - 1):
            trapped_water += min(left[i], right[i]) - height[i]

        return trapped_water
