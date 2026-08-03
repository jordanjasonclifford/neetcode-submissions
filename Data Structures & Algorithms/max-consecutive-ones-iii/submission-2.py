class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            # Add the new value to the window.
            if nums[right] == 0:
                zero_count += 1

            # Shrink until the window has at most k zeros.
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Current window can be made entirely of 1s
            # by flipping at most k zeros.
            max_length = max(max_length, right - left + 1)

        return max_length