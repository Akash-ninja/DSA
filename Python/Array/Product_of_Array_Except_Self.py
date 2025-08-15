class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## this solution is without extra space
        output = [1] * len(nums)

        left = 1
        # left of product[i] array formation
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        right = 1
        # right of product[i] array formation
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
