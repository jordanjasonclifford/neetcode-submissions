class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:

            if nums[left] < nums[right]:
                res = min(res, nums[left])
                return res


            med = (left + right) // 2

            res = min(res, nums[med])

            if nums[med] >= nums[left]:
                left = med + 1

            else: 
                right = med - 1

        return res


            