class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1

        max_vol = 0
        while left < right:
            # Volume = height of a container * width from left to right container
            volume = min(height[left], height[right]) * (right - left)
            max_vol = max(volume, max_vol)

            # Maximising height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol
