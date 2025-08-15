class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
        current_product = 1

        if len(nums) == 1:
            return nums[0]

        # calculating prefix product of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                current_product *= nums[i]
                max_product = max(current_product, max_product)
            else:
                current_product = 1

        current_product = 1
        # calculating suffix product of the array
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                current_product *= nums[i]
                max_product = max(current_product, max_product)
            else:
                current_product = 1

        return max_product
