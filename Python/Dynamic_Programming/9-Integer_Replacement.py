class Solution:
    def f(self, i, ht):
        if i == 1:
            return 0
        else:
            ans = -1

            if i in ht:
                return ht.get(i)
            else:
                if i % 2 == 0:
                    # if divided by 2, then already 1 step is counted thats why +1
                    ans = self.f(i / 2, ht) + 1
                else:
                    ans = min(self.f(i - 1, ht), self.f(i + 1, ht)) + 1

                ht[i] = ans
                return ans

    def integerReplacement(self, n: int) -> int:
        """
        Approach: Using DP to find, f(i) = Min. no. of ways to reach i to 1
        """
        ht = dict()
        return self.f(n, ht)
