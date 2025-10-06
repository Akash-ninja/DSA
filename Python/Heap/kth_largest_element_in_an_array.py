class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach:
        1. Create min. heap of 'k' elements
           on Iteration -
        2. insert next element in heap
        3. pop the element from heap
        """
        pq = []
        # min heap creation
        for i in range(k):
            heappush(pq, nums[i])

        # insert and pop from heap
        n = len(nums)
        for i in range(k, n):
            if nums[i] >= pq[0]:
                heappush(pq, nums[i])
                heappop(pq)

        return pq[0]
