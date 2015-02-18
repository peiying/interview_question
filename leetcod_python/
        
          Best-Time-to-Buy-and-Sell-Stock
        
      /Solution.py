class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        res = 0 
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_price)
            min_price = min(prices[i], min_price)
        return res
            
        
