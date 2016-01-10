class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        Bit manipulation
        
        do bitwise and operation for n and 1
        it means
        n = some binary value
        1 = 00000000000000001
        
        [both n and 1 are of same length]
        
        if this bit operation returns 1 increase the count by 1
        and do right shift of n by 1
        
        do this until n == 0
        '''
        count = 0
        while n != 0:
            count += n & 1
            n = n>>1
        return count
