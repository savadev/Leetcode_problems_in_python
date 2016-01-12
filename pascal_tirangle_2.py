'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,

This uses the following identity:

C(n,k+1) = C(n,k) * (n-k) / (k+1)
So you can start with C(n,0) = 1 and then calculate the rest of the line using this identity, each time multiplying the previous element by (n-k) / (k+1).
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        line = [1]
        n = rowIndex
        for k in range(n):
            #print line[k] * (n-k) , (k+1), 
            #print line[k] * (n-k) / (k+1)
            line.append((line[k] * (n-k)) / (k+1))
        return line
        
