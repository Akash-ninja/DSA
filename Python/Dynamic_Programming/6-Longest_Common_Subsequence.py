class Solution:
    def __init__(self):
        self.dp = dict()

    def lcs(self, text1, text2, i, j):
        if i == -1 or j == -1:
            return 0

        key = f"{i}-{j}"

        if key not in self.dp:
            if text1[i] == text2[j]:
                ans = 1 + self.lcs(text1, text2, i - 1, j - 1)
                self.dp[key] = ans
            else:
                ans = max(
                    self.lcs(text1, text2, i - 1, j),
                    self.lcs(text1, text2, i, j - 1),
                )
                self.dp[key] = ans
        else:
            ans = self.dp[key]

        return ans

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Approach: using DP recursion and calculating lcs of substrings.
        """
        n = len(text1)
        m = len(text2)

        return self.lcs(text1, text2, n - 1, m - 1)
