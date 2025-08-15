class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        end = n - 1

        i = 0
        while i <= end:
            # move non-zeroes to left
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1

            else:
                i += 1
