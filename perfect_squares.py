'''
Perfect Squares [same as Coin Change problem in leetcode]
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Approach: DP
Calculate the least number of perfect squares from 0 to n
And use it as memoization to find the count of next number
'''
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            # max_value is n+1 (it can be float('inf') too)
            min_list = [n+1]*n
            min_list.insert(0,0)
            for each_number in range(1, n+1):
                # find the count of perfect squares for each number upto to n
                sqrt_value = int(math.sqrt(each_number))
                if sqrt_value*sqrt_value == each_number:
                    min_list[each_number] = 1
                else:
                    counter = 1
                    while counter*counter <= n:
                        square = counter * counter
                        # Apply dp recurrence here
                        # Pick the minimum number of either min_list[each_number - square]+1, min_list[each_number]
                        min_list[each_number] = min(min_list[each_number - square]+1, min_list[each_number])
                        counter += 1
            return min_list[each_number]
