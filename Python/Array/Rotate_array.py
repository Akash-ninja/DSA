class Solution:
    def reverse(array, start, end):
        i = start
        j = end

        while i < j:
            # swap
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

            # increment
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Formula: 8th rotation is equal to 1st one
        k = k % n

        Solution.reverse(nums, 0, n - 1)  # reverse the whole array
        Solution.reverse(nums, 0, k - 1)  # reverse k times
        Solution.reverse(nums, k, n - 1)  # reverse remaining array
