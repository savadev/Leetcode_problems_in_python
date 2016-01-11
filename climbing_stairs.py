'''
Climbing Stairs:

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

This is nothing but fibonacci series

'''
fib = dict()
fib[0] = 1
fib [1] = 1
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global fib
        if n in fib:
            return fib[n]
        if n == 0 or n == 1:
            return 1
        else:
            value =  self.climbStairs(n-1)+self.climbStairs(n-2)
            if n not in fib:
                fib[n] = value
            return value
            
            
