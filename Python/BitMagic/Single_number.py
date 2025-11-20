class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Approach: using bitwise operator XOR
        Properties of XOR:
        1. a^0 = a
        2. a^a = 0
        3. a^b = b^a
        """
        ans = 0
        n = len(nums)
        for i in range(n):
            ans ^= nums[i]

        return ans
