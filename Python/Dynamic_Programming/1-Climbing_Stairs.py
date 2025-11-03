class Solution:
    def count_climb(self, i, n, mem_obj):
        # person already crossed top, can't come back
        if i > n:
            return 0

        # person at the top
        if i == n:
            return 1
        else:
            if i in mem_obj:
                # memoization
                return mem_obj.get(i)
            else:
                # formula
                ans = self.count_climb(i + 1, n, mem_obj) + self.count_climb(
                    i + 2, n, mem_obj
                )

                # setting values for memoization
                mem_obj[i] = ans

                return ans

    def climbStairs(self, n: int) -> int:
        """
        Approach: Using dynamic programming, using the formula dp[i] = dp[i+1] + dp[i+2]
        """
        i = standing_position = 0
        memoized_obj = dict()

        return self.count_climb(i, n, memoized_obj)
