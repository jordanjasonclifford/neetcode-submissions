class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Initialize the result array with 1s.
        # Each position will eventually contain:
        # product of everything to the left * product of everything to the right
        res = [1] * len(nums)

        # Running product of all numbers to the left
        prefix = 1

        # First pass: store the product of everything to the left of each index
        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n

        # Running product of all numbers to the right
        postfix = 1

        # Second pass: multiply each position by the product
        # of everything to its right
        for i, n in reversed(list(enumerate(nums))):
            res[i] *= postfix
            postfix *= n

        return res