class Solution:
    def f(self, i, required_sum, nums, dp):
        n = len(nums) - 1

        # if i is in last index (base condition)
        if i == n:
            if required_sum == 0 and nums[i] == 0:
                # achieving target of 0 by +0 or -0
                return 2
            elif required_sum != 0 and abs(nums[i]) == abs(required_sum):
                return 1
            else:
                return 0
        else:
            key = f"{i}-{required_sum}"

            if key not in dp:
                ans = self.f(i + 1, required_sum - nums[i], nums, dp) + self.f(
                    i + 1, required_sum + nums[i], nums, dp
                )
                dp[key] = ans
            else:
                ans = dp.get(key)

            return ans

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Approach:
            1. Recursive approach using dp, calculate f(i, target)
            2. f(i, target) = No. of ways of achieving target from index i onwards
        """
        dp = dict()

        return self.f(0, target, nums, dp)
