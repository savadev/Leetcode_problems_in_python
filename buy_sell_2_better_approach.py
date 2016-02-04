'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Approach:
Just a for loop.
When to buy the stock ? 
When the rate is low
so check for the decreasing growth
When to sell a stock?
When the rate is high
so check for the increasing growth
When the increasing/decreasing growth is changes, then that point is best price to buy or sell the stock
so safer case, add a sentinel (some random value like -1) to avoid the last buy or sell stock (MUST other wise it wont work) 
- This is IRK [satya dev's idea]
'''
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) in [0,1]:
        return 0
    else:
        # Buy the stock only when the rate is low
        # sell the stock only when the rate is high
        # How to find the rate is low ? Check the (decreasing growth). If the growth increases then the previous point is the best
        # day to buy the stock
        # same goes for selling the stop (increasing growth)
        prices.append(-1)
        prev = prices[0]
        # True = buy, False = Sell
        flag = True
        max_profit = 0
        for idx in xrange(1, len(prices)):
            each_price = prices[idx]
            if prev < each_price:
                # Increasing order/growth
                # check if I have to buy here
                if flag == True:
                    # buy the previous element
                    max_profit -= prev
                    flag = False
            else:
                # decreasing order/growth
                # check if I have to sell here
                if flag == False:
                    max_profit += prev
                    flag = True
            prev = each_price
        return max_profit
