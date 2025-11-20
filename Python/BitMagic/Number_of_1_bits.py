class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Approach: using bitwise operator
        checking set bits for the given number using (1<<i)
        """
        count_1s = 0

        for i in range(0, 32):
            if n & (1 << i) > 0:
                count_1s += 1

        return count_1s
