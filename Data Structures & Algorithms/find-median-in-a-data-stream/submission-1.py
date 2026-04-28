import heapq

class MedianFinder:

    def __init__(self):
        # small keeps the smaller half of numbers
        # we use negatives to make it act like a max heap
        self.small = []

        # large keeps the larger half of numbers
        # normal min heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1:
        # add to small first
        # since small is a max heap, we push negative num
        heapq.heappush(self.small, -num)

        # Step 2:
        # move the biggest value from small into large
        # this keeps every value in small <= every value in large
        biggest_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, biggest_small)

        # Step 3:
        # balance the heaps
        # small is allowed to have the same size as large
        # OR one more element than large
        if len(self.large) > len(self.small):
            smallest_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_large)

    def findMedian(self) -> float:
        # if small has more elements, median is the top of small
        if len(self.small) > len(self.large):
            return -self.small[0]

        # if both heaps are same size, median is average of both tops
        return (-self.small[0] + self.large[0]) / 2