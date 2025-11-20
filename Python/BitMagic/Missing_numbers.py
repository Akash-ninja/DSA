class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Approach: using bitwise XOR
        1. a ^ a = 0
        """
        n = len(nums)
        x = 0
        y = 0

        for i in range(0, n + 1):
            x = x ^ i

        for i in range(0, n):
            y = y ^ nums[i]

        return x ^ y
