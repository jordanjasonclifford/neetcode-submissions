class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array so we can use two pointers + handle duplicates easily
        nums.sort()
        combination = []

        # iterate through each number as the "anchor"
        for i in range(len(nums) - 2):

            # skip duplicate anchors to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two pointer setup
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                # sum too small → move left pointer up
                if total < 0:
                    l += 1

                # sum too large → move right pointer down
                elif total > 0:
                    r -= 1

                # valid triplet found
                else:
                    combination.append([nums[i], nums[l], nums[r]])

                    # move left pointer and skip duplicates
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # move right pointer and skip duplicates
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return combination