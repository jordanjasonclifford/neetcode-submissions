class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        minB = prices[0]

        for price in prices:

            maxP = max(maxP, price - minB)
            minB = min(minB, price)

        return maxP