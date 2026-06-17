class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Edge case:
        # If nums is empty, there are no triplets.
        #
        # Small correction:
        # This should return [] instead of [[]].
        if not nums:
            return []

        # Sort the array so we can use the two-pointer technique.
        # Sorting also helps us easily skip duplicates.
        nums.sort()

        # This will store all valid triplets.
        res = []

        # Loop through each number.
        # This number will be the first value in the triplet.
        for i, a in enumerate(nums):

            # Since the array is sorted, if the current number is greater than 0,
            # then every number after it is also greater than 0.
            # So the sum can never be 0.
            if a > 0:
                break

            # Skip duplicate values for the first number.
            # This prevents duplicate triplets in the result.
            #
            # Example:
            # nums = [-1, -1, 0, 1]
            # We only want to process the first -1.
            if i > 0 and a == nums[i - 1]:
                continue

            # Left pointer starts right after i.
            l = i + 1

            # Right pointer starts at the end of the array.
            r = len(nums) - 1

            # Move the two pointers toward each other.
            while l < r:

                # Current sum of the three selected numbers.
                threeSum = a + nums[l] + nums[r]

                # If the sum is too large, move the right pointer left
                # to try a smaller number.
                if threeSum > 0:
                    r -= 1

                # If the sum is too small, move the left pointer right
                # to try a larger number.
                elif threeSum < 0:
                    l += 1

                # If the sum is exactly 0, we found a valid triplet.
                else:
                    res.append([a, nums[l], nums[r]])

                    # Move both pointers inward to keep searching.
                    l += 1
                    r -= 1

                    # Skip duplicate values on the left side.
                    # This prevents repeating the same triplet.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate values on the right side.
                    # nums[r + 1] is safe here because we already did r -= 1 above.
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res