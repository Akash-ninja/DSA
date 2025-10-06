class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # 1. adds new number in max heap
        heappush(self.maxHeap, -num)

        # 2. Take the max no. from max. heap and put it into min. heap
        heappush(self.minHeap, -heappop(self.maxHeap))

        # 3.
        if len(self.minHeap) > len(self.maxHeap):
            # 4. take the min. no. from min. heap and put it in max. heap
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        # the stream list is odd
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        # the stream list is even
        return (-self.maxHeap[0] + self.minHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
