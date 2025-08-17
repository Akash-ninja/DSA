class Solution:
    def find_pairs(self, arr, start, end, target):
        pairs = []
        f = start
        s = end

        while f < s:
            # if while finding the pair in right side array,
            # this skips the previous element if duplicate is found
            # reason - we dont need to find the same pair again
            if f - 1 >= start and arr[f - 1] == arr[f]:
                f += 1
                continue

            # same as above but for end val
            if s + 1 <= end and arr[s + 1] == arr[s]:
                s -= 1
                continue

            # simple two sum approach applied
            if arr[f] + arr[s] < target:
                f += 1
            elif arr[f] + arr[s] > target:
                s -= 1
            else:
                pairs.append([arr[f], arr[s]])
                f += 1

        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)

        # sort the array to apply two_sum method
        nums.sort()

        for i in range(n):

            # either select first element OR ignores the element if duplicate found in previous one
            if (i == 0) or (i - 1 >= 0 and nums[i - 1] != nums[i]):
                selected_element = nums[i]
                target = -selected_element  # sets the target

                # finding pair by two pointer method (like in two sum)
                pairs = self.find_pairs(nums, i + 1, n - 1, target)

                # traversing the 2D pairs list and forms the resultant triplet
                for j in range(len(pairs)):
                    triplet = [selected_element, pairs[j][0], pairs[j][1]]
                    triplets.append(triplet)

        return triplets
