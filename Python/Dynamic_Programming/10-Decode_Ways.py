class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Approach: Using DP bottom-up
        """
        if s[0] == "0" or len(s) == 0:
            return 0

        n = len(s)
        dp = [0] * (n + 1)  # filled dp array with value 0
        dp[0] = 1  # for empty string
        dp[1] = 1  # for single digit at first position

        # treats "s" to be 1-indexed
        for i in range(2, n + 1):
            single_digit = int(s[i - 1 : i])  # extracts single char and converts to int
            double_digit = int(s[i - 2 : i])  # extracts 2 chars and converts to int

            # no. of ways single digit can be intrepreted + prev. combinations
            if single_digit >= 1 and single_digit <= 9:
                dp[i] += dp[i - 1]

            # no. of ways double digit can be intrepreted + prev. combinations
            if double_digit >= 10 and double_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
