class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_ones_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current_count += 1
                max_ones_count = max(current_count, max_ones_count)
            else:
                current_count = 0

        return max_ones_count
