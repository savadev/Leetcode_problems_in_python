'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find
the maximum profit.

Approach : 
Go from back wards,
While going traversing, track the maximum value.
Check when to buy a stock.
When ?
When the last seen value is greater than the current value then u have buy the current value stock
3 1 2 13 3 2 20 21
You will traverse from backwards and also store the maximum value in a variable max_sell_price
so 21 [max_sell_price = 21]
then 20 20 < 21 so buy 20 and find profit = max_sell_price - 20  = 1
go like that.
'''
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) in [0,1]:
        return 0
    else:
        max_sell_price = prices[-1]
        next_price = prices[-1]
        max_profit = 0
        for idx in xrange(len(prices)-2, -1, -1):
            current_price = prices[idx]
            # if current price is lesser than the previous price then
            # buy the stock.
            if current_price < next_price:
                if max_profit < max_sell_price - current_price :
                    max_profit = max_sell_price - current_price 
            if current_price > max_sell_price:
                max_sell_price = current_price
            next_price = current_price
        return max_profit
