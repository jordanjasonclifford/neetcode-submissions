class KthLargest:
    # use a min heap where we only have to store k items bc if we need the kth largest, it's
    # just the min of the k largest elems, and then once the heap is at capacity,
    # if we need to add an element larger than the min, we can pop the min and then add the
    # new elem bc the old min will never be the kth largest again, and if we need to add
    # an element smaller than or eqal to the min, can just ignore it

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        # heapq.heapify(self.minHeap)
        for num in nums:
            if len(self.minHeap) < self.k:
                heapq.heappush(self.minHeap, num)
            elif num > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, num)
        

    def add(self, val: int) -> int:
        # note that we're guaranteed that there will always be at least k integers in the
        # stream when you search for the kth integer
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)

        return self.minHeap[0]

        
