'''
Count the number of prime numbers less than a non-negative number, n.

Approach : chinese remainder theorem
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        else:
            # more than 2
            count = 0
            array = [True]*n
            array[0] = False
            i = 2
            square = i*i
            value = int(math.sqrt(n))
            while i <= value:
                index = i*i
                while index <= n:
                    array[index-1] = False
                    index += i
                i = i+1
            return sum(array)
