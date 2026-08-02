class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        minB = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minB)
            minB = min(minB, sell)

        return maxP