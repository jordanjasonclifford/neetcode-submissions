class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}   # dictionary to store value -> index of elements we've already seen

        # iterate through the list
        for i in range(len(nums)):
            complement = target - nums[i]   # the number we need to find to reach target

            # check if the complement has already been seen
            if complement in seen:
                # if yes, return indices of complement and current number
                return [seen[complement], i]

            # store the current number and its index for future lookups
            seen[nums[i]] = i