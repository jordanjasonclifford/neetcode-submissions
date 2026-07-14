class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # left represents the day we buy
        left = 0

        # right represents the day we sell
        right = 1

        # maxP stores the best profit we have found so far
        maxP = 0

        # Keep moving the selling day through the array
        while right < len(prices):

            # If the buying price is less than the selling price,
            # then this is a valid profitable transaction.
            if prices[left] < prices[right]:

                # Calculate the profit if we buy at left and sell at right
                profit = prices[right] - prices[left]

                # Update maxP if this profit is better than what we had
                maxP = max(maxP, profit)

            # If prices[left] >= prices[right],
            # then we found a cheaper buying price.
            #
            # So we move left to right because buying at this lower price
            # gives us a better chance of making profit later.
            else:
                left = right

            # Always move the selling pointer forward
            right += 1

        # Return the maximum profit found.
        # If no profit was possible, this stays 0.
        return maxP