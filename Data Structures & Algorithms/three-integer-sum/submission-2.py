class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        map = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    map.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return [list(i) for i in map]
        