class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # res array
        res = [1] * (len(nums))

        prefix = 1

        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n

        postfix = 1
        for i, n in reversed(list(enumerate(nums))):
            res[i] *= postfix
            postfix *= n

        return res


