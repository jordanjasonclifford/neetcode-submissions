class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # Number of actual stairs
        n = len(cost)

        # dp[i] stores the minimum cost needed
        # to reach step i
        #
        # We use n + 1 because dp[n] represents
        # reaching the top, which is just beyond the last stair
        dp = [0] * (n + 1)

        # Start from step 2 because:
        # dp[0] = 0 and dp[1] = 0
        #
        # You are allowed to start at either step 0 or step 1
        for i in range(2, n + 1):

            # Option 1:
            # come from step i - 1
            # and pay the cost of stepping on i - 1
            one_step = dp[i - 1] + cost[i - 1]

            # Option 2:
            # come from step i - 2
            # and pay the cost of stepping on i - 2
            two_steps = dp[i - 2] + cost[i - 2]

            # Store the cheaper way to reach step i
            dp[i] = min(one_step, two_steps)

        # dp[n] is the minimum cost needed
        # to reach the top of the staircase
        return dp[n]