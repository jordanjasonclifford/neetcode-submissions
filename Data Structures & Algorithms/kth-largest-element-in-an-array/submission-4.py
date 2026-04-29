class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Convert "kth largest" → "kth smallest index"
        # Example:
        # nums = [3,2,1,5,6,4], k = 2 (2nd largest = 5)
        # Sorted = [1,2,3,4,5,6]
        # Index of 2nd largest = len(nums) - k = 6 - 2 = 4
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