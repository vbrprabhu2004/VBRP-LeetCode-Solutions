class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(max_profit, i - min_price)
        return max_profit