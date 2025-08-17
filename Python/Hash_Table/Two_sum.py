class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hash Table implementation to find the solution
        """
        result_index = [-1, -1]
        ht = dict()  # Hash table in python is implemented as Dictionary

        for i in range(len(nums)):

            complement = (
                target - nums[i]
            )  # calculates complement of the incoming number
            # if the complement found then store the index in resultant array
            if complement in ht:
                result_index[0] = ht.get(complement)
                result_index[1] = i
                break

            ht[nums[i]] = i  # stores value in dict if the key not present

        return result_index
