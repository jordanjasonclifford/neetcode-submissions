class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # left and right pointers for binary search
        l = 0
        r = len(nums) - 1

        # standard binary search loop
        while l <= r:

            # find middle index
            m = (l + r) // 2

            # if we found the target, return its index
            if nums[m] == target:
                return m

            # -----------------------------
            # determine which side is sorted
            # -----------------------------

            # if left side is sorted
            # example: [4,5,6,7 | 0,1,2]
            # if m is in the left portion, nums[l] <= nums[m]
            if nums[m] >= nums[l]:

                # now check if target is OUTSIDE this sorted left range
                # if target is bigger than nums[m] OR smaller than nums[l],
                # it must be in the right half
                if target > nums[m] or target < nums[l]:
                    l = m + 1   # search right

                else:
                    r = m - 1   # search left

            # otherwise, right side must be sorted
            # example: [4,5,6 | 7,0,1,2]
            else:

                # check if target is OUTSIDE the sorted right range
                # if target is smaller than nums[m] OR bigger than nums[r],
                # it must be in the left half
                if target < nums[m] or target > nums[r]:
                    r = m - 1   # search left

                else:
                    l = m + 1   # search right

        # if we exit loop, target was not found
        return -1