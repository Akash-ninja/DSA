import math


class Solution:
    def binary_search(self, arr, key, flag):
        ans = -1
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = math.floor((start + end) / 2)

            if arr[mid] < key:
                start = mid + 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                ans = mid
                if flag == "left":
                    end = mid - 1
                else:
                    start = mid + 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Solution approach: if the target is found then the search doesn't stop instead it searches left and right once
        in both direction.
        """
        left = self.binary_search(nums, target, "left")
        right = self.binary_search(nums, target, "right")

        return [left, right]
