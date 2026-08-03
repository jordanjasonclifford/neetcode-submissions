class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Left side of the current sliding window.
        left = 0

        # Maximum number of consecutive 1s found.
        res = 0

        # Expand the window using the right pointer.
        for right in range(len(nums)):

            # If we encounter a 0, the current sequence of 1s ends.
            # Move left to the position immediately after the zero.
            if nums[right] == 0:
                left = right + 1

            # The window from left to right now contains only 1s.
            current_length = right - left + 1

            # Update the longest sequence found so far.
            res = max(res, current_length)

        return res