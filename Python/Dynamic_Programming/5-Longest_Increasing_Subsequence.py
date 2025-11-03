class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Approach: using iterative (bottom-up) DP
        1. Solves smaller sub-problems first
        2. init: dp[0] = 1
        3. calculate: dp[i] = max(dp[i], dp[j]+1)
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        ans = 1

        for i in range(0, n):
            dp[i] = 1

            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

            ans = max(ans, dp[i])

        return ans
