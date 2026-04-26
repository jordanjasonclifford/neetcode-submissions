class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = []  
        # stack will store pairs: [temperature, index]
        # it's a "monotonic decreasing stack"
        # meaning temps in stack go from high -> low
        
        res = [0] * n  
        # result array, default 0 since some days never get warmer

        for i, t in enumerate(temperatures):
            # i = current index
            # t = current temperature

            # while current temp is warmer than the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # we found a warmer day for stackInd

                res[stackInd] = (i - stackInd)
                # number of days we had to wait

            # push current temp + index onto stack
            stack.append([t, i])

        return res
        