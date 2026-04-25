class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # put all numbers in a set so we can check if a number exists quickly
        store = set(nums)

        # this will hold the longest streak we find
        res = 0

        # go through each unique number
        for num in store:

            # only start counting if this number is the beginning of a sequence
            # example: for 2,3,4,5, only start at 2 because 1 is not in the set
            if num - 1 not in store:

                # start the current streak at this number
                curr = num
                streak = 1

                # keep moving forward while the next number exists
                while curr + 1 in store:
                    curr += 1
                    streak += 1

                # update the longest streak found so far
                res = max(res, streak)

        return res