class Solution:
    def maxProfit(self, prices: List[int]) -> int:


# need at least 2 prices to make a buy + sell
        if len(prices) < 2:
            return 0

        # index of the lowest price seen so far (best buy day)
        low = 0

        # track the maximum profit we can get
        profit = 0

        # iterate through each day
        for i in range(len(prices)):

            # if current price is lower than our lowest so far,
            # update the buy day
            if prices[low] > prices[i]:
                low = i

            # calculate profit if we sell today
            # (current price - lowest price so far)
            newProfit = prices[i] - prices[low]
            if profit < newProfit:
                profit = newProfit

        return profit

        