class Solution:
    def f(self, i, coins, dp):
        # base condition f(0) = 0 (if no amount, no coins needed)
        if i == 0:
            return 0

        # fetch from memoized value (if there is already)
        if dp[i] != 0:
            return dp[i]

        # result defaults to -1 when f(i) solution is not possible [e.g.- amount=2, coins=[3,5]]
        result = -1

        # traverse through each coin (denomination)
        for j in range(0, len(coins)):
            # denomination <= amount
            if coins[j] <= i:
                temp_coins_count = self.f(
                    i - coins[j], coins, dp
                )  # look for possible solutions

                # if f(i) has no valid solution then result stays -1
                # if f(i) got lesser temp_count then update the result
                if temp_coins_count != -1 and (
                    result == -1 or temp_coins_count + 1 < result
                ):
                    result = temp_coins_count + 1

        dp[i] = result  # memoizing dp

        return result

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Approach: minimising problem so used DP. Calculated f(amount) using top-down approach thats why recursive.
        """
        i = amount

        # filling dp[] with zereos (use in memoization)
        dp = [0] * (i + 1)

        # evaluating f(i)
        return self.f(i, coins, dp)
