class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # store all valid combinations
        res = []

        def dfs(i, curr, total):
            # i     = current index in nums
            # curr  = current combination being built
            # total = sum of elements in curr

            # if we hit the target exactly, store a copy of the combination
            if total == target:
                res.append(curr.copy())
                return

            # stop if we go out of bounds or exceed the target
            if i >= len(nums) or total > target:
                return

            # take nums[i]
            # add it to current combination
            curr.append(nums[i])

            # stay at same index since we can reuse the same number
            dfs(i, curr, total + nums[i])

            # backtrack (remove last element before exploring next option)
            curr.pop()

            # skip nums[i] and move to next index
            dfs(i + 1, curr, total)

        # start recursion
        dfs(0, [], 0)

        return res