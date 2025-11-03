class Solution:
    def __init__(self):
        self.dp = []

    def partition(self, i, target, nums):
        # if target becomes -ve then false
        if target < 0:
            return False

        if i == len(nums):
            return target == 0

        # fetch from memoized value
        if self.dp[i][target] is not None:
            return self.dp[i][target]

        # similar to knapsack problem
        take = self.partition(i + 1, target - nums[i], nums)
        skip = self.partition(i + 1, target, nums)

        self.dp[i][target] = take or skip

        return self.dp[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        """
        Approach: using DP recursion + memoization
        Observation: if sum of all elements is odd => partition not possible
        """
        nums_sum = sum(nums)

        # observation implementation
        if (nums_sum % 2) != 0:
            return False

        n = len(nums)
        target = int(nums_sum / 2)

        # filling dp[nums.size][target]
        self.dp = [[None for _ in range(target + 1)] for _ in range(n)]

        return self.partition(0, target, nums)
