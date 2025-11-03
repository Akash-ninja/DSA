class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach: using DP bottom-up

        Tabulation method: see how the memoization table dp fills up then formulate
        fills the 2D array with =
        1. False values for diagonal values (i,i) => always true (single char)
        2. checks for string size 2 (i, i+1)th => true when char(i) == char(i+1) (double char)
        3. checks for string size 3 and onwards
            a. if first and last char equals => str[i] == str[j]
            b. then, check middle between (first, last) => str[i+1] == str[j-1]
            c. update the answer
        4. Return the answer string
        """
        ans = ""  # stores the answer

        n = len(s)
        row = n
        col = n
        # filling up dp[][] initially with false
        dp = [[False] * col for _ in range(row)]

        # 1.
        for i in range(0, n):
            dp[i][i] = True
            # update the answer
            ans = s[i : i + 1]

        # 2.
        for i in range(0, n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                # update the answer
                ans = s[i : i + 2]

        # 3. size refers to string length (1-indexed)
        # loop runs diagonal of dp[][]
        for size in range(3, n + 1):  ### difficult to catch
            for i in range(0, n):
                start = i
                end = i + size - 1  # sliding with size

                if end >= n:
                    continue

                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1]  # memoization
                    if dp[start][end]:
                        # update the answer
                        ans = s[start : end + 1]

        return ans
