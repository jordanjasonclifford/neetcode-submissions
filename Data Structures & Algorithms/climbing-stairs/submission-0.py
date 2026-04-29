class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [0] * (n + 1)

        # Base cases:
        # 1 way to stay at step 0 (do nothing)
        cache[0] = 1

        # 1 way to reach step 1 (one single step)
        cache[1] = 1

        # Build up the solution
        for i in range(2, n + 1):
            # To reach step i:
            # either come from i-1 (1 step)
            # or from i-2 (2 steps)
            cache[i] = cache[i - 1] + cache[i - 2]

        # Final answer: number of ways to reach step n
        return cache[n]

