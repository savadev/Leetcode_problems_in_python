'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Approach : A pattern is forming everytime when I'm calculating the factorial of a number

For 5 it is 1
10 it is 2
25 it is 6 [ 25/5 = 5 ; 5/5 = 1 ; so 5+1 =6]

This runs in logn complexity
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            n = n/5
            count += n
        return count
