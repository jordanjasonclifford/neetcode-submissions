class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Start of the current search range
        left = 0

        # End of the current search range
        right = len(nums) - 1

        # Continue while the search range is valid
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # If the middle value is the target, return its index
            if nums[mid] == target:
                return mid

            # Check whether the left half is sorted
            if nums[left] <= nums[mid]:

                # If the target is outside the sorted left half:
                # target > nums[mid] means it is too large for the left half
                # target < nums[left] means it is too small for the left half
                if target > nums[mid] or target < nums[left]:
                    # Discard the left half and search right
                    left = mid + 1

                else:
                    # Target must be inside the sorted left half
                    right = mid - 1

            # Otherwise, the right half must be sorted
            else:

                # If the target is outside the sorted right half:
                # target < nums[mid] means it is too small
                # target > nums[right] means it is too large
                if target < nums[mid] or target > nums[right]:
                    # Discard the right half and search left
                    right = mid - 1

                else:
                    # Target must be inside the sorted right half
                    left = mid + 1

        # Target was not found
        return -1