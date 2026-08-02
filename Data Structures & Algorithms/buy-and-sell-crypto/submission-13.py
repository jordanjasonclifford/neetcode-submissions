class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        minB = prices[0]

        for price in prices:

            if (price - minB) > maxP:
                maxP = price - minB

            if minB > price:
                minB = price
                 

        return maxP