import math


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = len(nums)

        # just when mid becomes higher than target
        # that element can be potential answer
        while low <= high:
            mid = math.floor((low + high) / 2)

            if nums[mid] < target:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans
