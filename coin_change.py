'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Approach: DP
Find the minimum number of coins for each number from 1 to amount.
use it as a memoization to find the minimum number for next amount.
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        else:
            # max value is amount+1 it can be float('inf')
            min_list = [amount+1]*amount
            min_list.insert(0, 0)
            for each_amount in range(1, amount+1):
                for each_coin in coins:
                    # either the coin itself match the exact amount
                    if each_coin <= each_amount:
                        min_list[each_amount] = min(min_list[each_amount-each_coin]+ 1, min_list[each_amount])
            return min_list[amount] if min_list[amount] < amount+1 else -1
                            
