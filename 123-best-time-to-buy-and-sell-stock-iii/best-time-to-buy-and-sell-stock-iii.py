class Solution(object):
    def maxProfit(self, prices):
        buy1 = float('-inf')   # best "buy" for 1st transaction
        sell1 = 0              # best "sell" for 1st transaction
        buy2 = float('-inf')   # best "buy" for 2nd transaction
        sell2 = 0              # best "sell" for 2nd transaction

        for price in prices:
            buy1 = max(buy1, -price)            # spend money to buy first stock
            sell1 = max(sell1, buy1 + price)    # sell first stock
            buy2 = max(buy2, sell1 - price)     # reinvest profit to buy second stock
            sell2 = max(sell2, buy2 + price)    # sell second stock

        return sell2
