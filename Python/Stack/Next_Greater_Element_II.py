class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:  # type: ignore
        """
        Solution using stack: Maintains index of the element for which NO greater element is found
        1. push() happens in the first loop and not in second
        2. pop() happens when the current element is greater than stack top indexed element
        """
        st = [0]  # stores index of the elements
        ans = [-1] * len(nums)

        # first loop
        for i in range(1, len(nums)):
            current = nums[i]

            # check if stack non-empty and compares element from the stack top indexed element with current element
            while len(st) > 0 and nums[st[-1]] < current:
                ans[st[-1]] = current
                st.pop(-1)

            # push index in stack
            st.append(i)

        # second loop
        for i, el in enumerate(nums):
            current = el

            # same as in first loop except no push() will be done here
            while len(st) > 0 and nums[st[-1]] < current:
                ans[st[-1]] = current
                st.pop(-1)

        return ans
