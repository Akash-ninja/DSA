class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: using sliding window and deque (deck) operations
        1. window := j - k + 1

        2. removal from deck => 2 scenarios
            a. (left) when window slides (then some index inside deck goes out of window)
            b. (right) when greater current element encountered than present in deck

        3. after removal only(ie., check completed) and now insert current index into deck

        4. answer stored in leftmost element of deck (nums[de[0]])
        """

        # init
        de = deque([])  # stores index as we move forward
        n = len(nums)
        ans = []

        # for the first window
        de.append(0)
        for i in range(1, k):
            while len(de) > 0 and nums[de[-1]] < nums[i]:
                de.pop()
            de.append(i)

        ans_index = de[0]
        ans.append(nums[ans_index])

        # for the subsequent windows
        for j in range(k, n):
            starting_point = j - k + 1

            # window slided => remove the index outside of it
            while len(de) > 0 and de[0] < j - k + 1:
                de.popleft()

            while len(de) > 0 and nums[de[-1]] < nums[j]:
                de.pop()

            de.append(j)
            ans_index = de[0]
            ans.append(nums[ans_index])

        return ans
