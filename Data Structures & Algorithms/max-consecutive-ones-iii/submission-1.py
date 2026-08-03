class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # Left boundary of the sliding window.
        start = 0

        # Stores the longest valid window found so far.
        maxOnes = 0

        # Right boundary of the sliding window.
        end = 0

        # Expand the window until the right pointer reaches the end.
        while end < len(nums):

            # If the new element is a 0, use one available flip.
            if nums[end] == 0:
                k -= 1

            # If k becomes negative, the window contains
            # more zeros than we are allowed to flip.
            while k < 0:

                # If the element leaving the window is a 0,
                # restore one available flip.
                if nums[start] == 0:
                    k += 1

                # Shrink the window from the left.
                start += 1

            # The current window is valid because it contains
            # at most the allowed number of zeros.
            current_length = end - start + 1

            # Update the longest valid window found so far.
            maxOnes = max(maxOnes, current_length)

            # Expand the window by moving the right pointer.
            end += 1

        # Return the maximum number of consecutive 1s obtainable
        # after flipping at most k zeros.
        return maxOnes