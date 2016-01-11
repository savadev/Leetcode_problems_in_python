import math
'''
This problem can be generalized to find all the prime factors of a number.

First step: In a while loop repeatedly divide the number by 2
Second step: After that the number would odd. From i - > 3 to the sqrt(n) increment by 2 (i+2 because to remain in odd all time)
find all the factors inside a while loop

After this the number would be 1 or prime number
return the number.

'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n= num
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            # Get the prime factors and check if it in 2.3.5
            while n%2 == 0:
                n = n/2
            for i in range(3, 7, 2):
                while n%i == 0:
                    n = n/i
            if n!= 1:
                return False
            return True
