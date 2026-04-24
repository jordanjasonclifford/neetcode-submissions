class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # result array, initialized with 1s
        # we will build the answer in-place using prefix and postfix products
        res = [1] * (len(nums))

        prefix = 1  # stores product of all elements to the LEFT

        # first pass: fill res with prefix products
        for i in range(len(nums)):
            res[i] = prefix      # at index i, store product of everything before it
            prefix *= nums[i]    # update prefix to include current number

        postfix = 1  # stores product of all elements to the RIGHT

        # second pass (right to left): multiply with postfix products
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix    # multiply current prefix result with postfix
            postfix *= nums[i]   # update postfix to include current number

        return res