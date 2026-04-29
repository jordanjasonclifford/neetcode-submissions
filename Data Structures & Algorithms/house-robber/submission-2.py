class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Edge case:
        # If the list is empty, there are no houses to rob
        if not nums:
            return 0

        # Edge case:
        # If there's only one house, we can only rob that one
        if len(nums) == 1:
            return nums[0]

        # DP array:
        # cache[i] = maximum money we can rob from houses [0 → i]
        cache = [0] * len(nums)

        # Base case:
        # If we only consider the first house,
        # the best we can do is rob it
        cache[0] = nums[0]

        # Base case:
        # For the second house, we have two options:
        # - rob house 0
        # - rob house 1
        # We choose the maximum of the two
        cache[1] = max(nums[0], nums[1])

        # Start building the solution from house index 2 onward
        for i in range(2, len(nums)):

            # At each house, we have TWO choices:
            
            # 1. Skip the current house:
            #    → then our profit stays as cache[i - 1]
            
            # 2. Rob the current house:
            #    → we add nums[i] (current house money)
            #    → but we MUST skip the previous house
            #    → so we add cache[i - 2]
            
            # Take the better of the two choices
            cache[i] = max(
                cache[i - 1],              # skip current house
                nums[i] + cache[i - 2]    # rob current house
            )

        # The last element contains the answer:
        # max money we can rob from ALL houses
        return cache[-1]