class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            # if we find target
            if nums[m] == target:
                return m

            # ---------------------------------
            # Example array:
            # nums = [4,5,6,7,0,1,2]
            # index   0 1 2 3 4 5 6
            # ---------------------------------

            # check if left half is sorted
            if nums[m] >= nums[l]:
                # left portion is sorted
                # example:
                # [4,5,6,7 | 0,1,2]
                #  l       m

                # say target = 6
                # 6 is between nums[l]=4 and nums[m]=7
                # so we go LEFT

                # say target = 1
                # 1 is NOT between 4 and 7
                # so we go RIGHT

                if target > nums[m] or target < nums[l]:
                    # target is outside left sorted range
                    l = m + 1   # search right side
                else:
                    # target is inside left sorted range
                    r = m - 1   # search left side

            else:
                # right portion is sorted
                # example:
                # [4,5,6 | 7,0,1,2]
                #         m       r

                # say target = 1
                # 1 is between nums[m]=0 and nums[r]=2
                # so we go RIGHT

                # say target = 6
                # 6 is NOT between 0 and 2
                # so we go LEFT

                if target < nums[m] or target > nums[r]:
                    # target is outside right sorted range
                    r = m - 1   # search left side
                else:
                    # target is inside right sorted range
                    l = m + 1   # search right side

        return -1