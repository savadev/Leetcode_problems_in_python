'''
This paves way for a generalized problem
find if X is an integer power of Y

approach:
return x == y ** log(x)/log(y)

or 
power = log(x)/log(y)
return floor(power) == power

Here log is of base 10
'''
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        #print math.log(n)
        #print math.log(3)
        return n == 3 ** round(math.log(n) / math.log(3))
