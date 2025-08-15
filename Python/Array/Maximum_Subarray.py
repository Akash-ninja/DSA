class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_so_far = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum < 0:
                current_sum = 0

            current_sum += nums[i]
            max_sum_so_far = max(current_sum, max_sum_so_far)

        return max_sum_so_far
