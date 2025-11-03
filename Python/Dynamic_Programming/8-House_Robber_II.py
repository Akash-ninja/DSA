class Solution:
    def __init__(self):
        self.dp = []

    def house_rob(self, start, end, nums):
        self.dp = [0] * len(nums)
        self.dp[start] = nums[start]
        self.dp[start + 1] = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            # if i-th selected then i-2 will be selected
            # or else (i-1)th selected
            self.dp[i] = max(nums[i] + self.dp[i - 2], self.dp[i - 1])

        return self.dp[end]

    def rob(self, nums: List[int]) -> int:
        """
        Approach: Solved using DP tabular method (Bottom-up)
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.house_rob(0, n - 2, nums), self.house_rob(1, n - 1, nums))
