import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[math.floor(len(nums) / 2)]
