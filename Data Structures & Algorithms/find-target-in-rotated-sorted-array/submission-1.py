class Solution:
    def search(self, nums: List[int], target: int) -> int:
         
        # keep track of the minimum value we’ve seen so far

        l = 0
        r = len(nums) - 1
        # binary search boundaries

        while l <= r:

            m = (l + r) // 2
            # middle index

            if nums[m] == target:
                return m
 

            # left sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
                  
            # right sorted portion
            else:

                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
 

        return -1  