class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        # scans the list
        for i, num in enumerate(nums):

            # if number-1 present then ignore it
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # check the advance no. and then start sequencing and keep track of count
                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num += 1

                # stores count for longest sequence
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
