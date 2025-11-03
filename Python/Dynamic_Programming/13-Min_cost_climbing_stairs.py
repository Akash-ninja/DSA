class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Approach: using DP tabular method
        """
        n = len(cost)
        dp = [0] * (n + 1)

        # user can either start from 0 or 1 without any cost
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            # 1 step or 2 step can be climbed
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]
