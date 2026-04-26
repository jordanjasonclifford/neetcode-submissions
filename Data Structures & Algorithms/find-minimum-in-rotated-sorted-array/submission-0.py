class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        # keep track of the minimum value we’ve seen so far

        l = 0
        r = len(nums) - 1
        # binary search boundaries

        while l <= r:

            # if current window is already sorted
            # then leftmost value is the smallest in this window
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            # middle index

            res = min(res, nums[m])
            # update result with middle value

            # check which side is sorted
            if nums[m] >= nums[l]:
                # left side is sorted
                # so minimum must be on the right side
                l = m + 1

            else:
                # right side is sorted
                # so minimum is on the left side (including mid)
                r = m - 1

        return res