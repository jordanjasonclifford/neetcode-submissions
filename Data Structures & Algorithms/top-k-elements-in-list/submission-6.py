class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Dictionary to store the frequency of each number
        # Example: nums = [1,1,1,2,2,3]
        # count = {1: 3, 2: 2, 3: 1}
        count = {}

        for n in nums:
            # If n is already in count, increment it
            # Otherwise, start it at 0, then add 1
            count[n] = 1 + count.get(n, 0)

        # Min-heap that will store pairs of:
        # (frequency, number)
        #
        # Python heaps are min-heaps by default,
        # so the smallest frequency stays at the top.
        heap = []

        for n in count:
            # Push the current number and its frequency into the heap
            heapq.heappush(heap, (count[n], n))

            # If heap size becomes bigger than k,
            # remove the element with the smallest frequency.
            #
            # This keeps only the k most frequent elements in the heap.
            if len(heap) > k:
                heapq.heappop(heap)

        # Result list to store the k most frequent numbers
        res = []

        # Pop all remaining elements from the heap
        # These are the top k frequent elements
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res