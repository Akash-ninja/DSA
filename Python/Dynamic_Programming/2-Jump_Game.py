class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Approach: using DP, cal reachable_index until I can reach the end and compare it with max_reachable value
        """
        max_reachable = nums[0]

        n = len(nums)
        i = 1
        while i < n and max_reachable >= i:
            reachable_index = i + nums[i]
            if reachable_index > max_reachable:
                max_reachable = reachable_index

            i += 1

        return max_reachable >= n - 1
