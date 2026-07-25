class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
         
       # Create a min heap
        heap = []

        for num in nums:
            # Push current number into heap
            heapq.heappush(heap, num)

            # If heap size exceeds k, remove smallest element
            # This keeps only the k largest elements in the heap
            if len(heap) > k:
                heapq.heappop(heap)

        # The root of the heap is the kth largest element
        return heap[0]