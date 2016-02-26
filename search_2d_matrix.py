'''
Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Approach : Binary Search
Find the mid point of the matrix. rmid, cmid

Now the target can be top left or top right or bottom left or bottom right with respect to mid point of the matrix
So 4 independent If conditions has to be written and also check if rmid+1 and cmid+1 are within the lenth of matrix.

NOTE: This is the worst algorithm ever written in this world !!! 

why ? You are searching the whole matrix by going top left, top right , bottom left, bottom right which is equal to O(n^2)
This is can be done using two for loops instead of having 4 recursion calls.

IRK aka satya dev embarassed me by finding this on Feb 25th at 8 PM
'''
class Solution(object):
    def find_target(self, matrix, rlow, rhigh, clow, chigh, target):
        # base case
        if rlow == rhigh == clow == chigh:
            return target == matrix[rlow][chigh]
        else:
            # recursive case
            # find mid w r t to col
            cmid = (clow + chigh)/2
            # find mid w r t to row
            rmid = (rlow + rhigh)/2
            if matrix[rmid][cmid] == target:
                return True
            else:
                tl = False
                tr = False
                bl = False
                br = False
                if matrix[rlow][clow] <= target <= matrix[rmid][cmid]:
                    # go top left
                    tl =  self.find_target(matrix, rlow, rmid, clow, cmid, target)
                if cmid+1 <= chigh and matrix[rlow][cmid+1] <= target <= matrix[rmid][chigh]:
                    # go top right
                    tr = self.find_target(matrix, rlow, rmid, cmid+1, chigh, target)
                if rmid+1 <= rhigh and matrix[rmid+1][clow] <= target <= matrix[rhigh][cmid]:
                    # go to bottom left
                    bl = self.find_target(matrix, rmid+1, rhigh, clow, cmid, target)
                if rmid+1 <= rhigh and cmid+1 <= chigh and matrix[rmid+1][cmid+1] <= target <= matrix[rhigh][chigh]:
                    # go to bottom right
                    br = self.find_target(matrix, rmid+1, rhigh, cmid+1, chigh, target)
                return tl or tr or bl or br
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        else:
            # the matrix contains rows and columns
            return self.find_target(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, target) 
