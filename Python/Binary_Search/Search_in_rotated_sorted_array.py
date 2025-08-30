import math


class Solution:
    def find_point_of_rotation(self, nums):
        """
        Returns place before which the rotation has taken place
        """
        start = 0
        end = len(nums) - 1
        point_of_rotation = 0

        while start <= end:
            mid = math.floor((start + end) / 2)
            # compares mid value to the last element of array
            if nums[mid] <= nums[-1]:
                point_of_rotation = mid
                end = mid - 1
            else:
                start = mid + 1

        return point_of_rotation

    def bsearch(self, nums, start, end, search_key):
        """
        Standard binary search
        """
        position_found = -1

        while start <= end:
            mid = math.floor((start + end) / 2)
            if nums[mid] < search_key:
                start = mid + 1
            elif nums[mid] > search_key:
                end = mid - 1
            else:
                position_found = mid
                break

        return position_found

    def search(self, nums: List[int], target: int) -> int:
        """
        Solution approach: search in left(rotated) or right(original) region based upon observation
        """
        rotation_point = self.find_point_of_rotation(nums)
        print(rotation_point)
        ans = -1

        if rotation_point == 0:
            ans = self.bsearch(nums, 0, len(nums) - 1, target)
        elif target >= nums[0]:
            ans = self.bsearch(nums, 0, rotation_point - 1, target)
        else:
            ans = self.bsearch(nums, rotation_point, len(nums) - 1, target)

        return ans
