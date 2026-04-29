class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]

        nums.sort()
        res = []

        # Step 2: iterate through each number, treating it as the first number in the triplet
        for i, a in enumerate(nums):

            # if the current number is > 0, we can break early
            # because all numbers after are also >= a (sorted),
            # so the sum can never be 0
            if a > 0:
                break

            # skip duplicate values for 'a' to avoid duplicate triplets
            # example: if nums[i] == nums[i-1], we've already processed this value
            if i > 0 and a == nums[i - 1]:
                continue

            # Step 3: use two pointers to find the other two numbers
            l, r = i + 1, len(nums) - 1

            while l < r:
                
                # current sum of the triplet
                threeSum = a + nums[l] + nums[r]

                # if sum is too large, move right pointer left
                # because we need a smaller number
                if threeSum > 0:
                    r -= 1

                # if sum is too small, move left pointer right
                # because we need a larger number
                elif threeSum < 0:
                    l += 1

                else:
                    # found a valid triplet that sums to 0
                    res.append([a, nums[l], nums[r]])

                    # move both pointers inward to look for next pair
                    l += 1
                    r -= 1

                    # skip duplicate values for nums[l]
                    # this avoids adding duplicate triplets
                    # (we already used this value for l)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        # return all unique triplets
        return res
