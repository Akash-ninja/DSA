class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        this one is hash table implementation
        """
        check_dict = dict()

        for i, num in enumerate(nums):
            if num in check_dict:
                return True

            check_dict[num] = num

        return False
