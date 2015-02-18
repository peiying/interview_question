class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        res = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i - 1] > 0:
                res += prices[i] - prices[i - 1]
        return res
