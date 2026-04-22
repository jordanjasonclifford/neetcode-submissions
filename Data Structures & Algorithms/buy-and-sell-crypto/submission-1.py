class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        if len(prices) < 2:
            return 0

        low = 0
        profit = 0

        for i in range(len(prices)):
            if prices[low] > prices[i]:
                low = i
            if profit < prices[i] - prices[low]:
                profit = prices[i] - prices[low]
 

        return profit


        