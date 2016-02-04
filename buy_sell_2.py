class Solution(object):
    '''
    Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    '''
    def max_profit(self,prices, low, high, number_of_stocks):
        # base case
        if low == high:
            if number_of_stocks != 0:
                return prices[high]
            else:
                return 0
        else:
            # More elements in the prices
            # If my max_value is 0 then I can buy the element or I'll skip the element
            # If my max value is >0 :
            # case 1: I can sell or I'll skip the day to sell it
            # If I sell, I can buy the stock on same day or I can skip the day to buy it
            # these are the possibilities
            if number_of_stocks == 0:
                # I can only buy the stock
                # either i can buy the stock or I can skip it
                return max(-prices[low] + self.max_profit(prices, low+1, high, number_of_stocks+1), self.max_profit(prices, low+1, high, number_of_stocks))
            else:
                # I can only sell the stock
                # either I can sell the stock or I can skip it
                return max(prices[low]+ self.max_profit(prices, low+1, high, number_of_stocks-1), self.max_profit(prices, low+1, high, number_of_stocks))
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0,1]:
            return 0
        else:
            return self.max_profit(prices, 0, len(prices)-1,  0)
            
