'''
Question: You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Approach:

Go layer by layer (n/2)
Get an offset to find the top, left, bottom , right locations
Now do the swap

Time complexity - O(n^2)

Example:
Rotate this matrix: [[1,2,3,4],[3,4,5,5],[6,7,8,9],[6,7,8,9]]

After rotation : [[6,6,3,1],[7,7,4,2],[8,8,5,3],[9,9,5,4]]

How the offset, top, left, right, bottom are found? [Debugging statements of below code]
Go layer by layer and find the first and last layer
first & last are 0 3  [for a 4*4 matrix the first and last are 0 3]
  offeset is 0   [Offset is calculated as i-first look code]
     top is 0 0  [top is first,i]
     left is 3 0 [left is last-offset, first]
     bottom is 3 3 [bottom is last, last-offset]
     right is 0 3  [right is i,last]
  offeset is 1
     top is 0 1
     left is 2 0
     bottom is 3 2
     right is 1 3
  offeset is 2
     top is 0 2
     left is 1 0
     bottom is 3 1
     right is 2 3
first & last are 1 2  [The the first and last are 1 and 2]
  offeset is 0
     top is 1 1
     left is 2 1
     bottom is 2 2
     right is 1 2
     
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        # go layer by layer
        for j in range(len(matrix)/2):
            first = j
            last = len(matrix)-j-1
            print "first & last are", first, last
            for i in range(first, last):
                # offset
                offset = i-first
                print "  offeset is", offset
                # save top
                top = matrix[first][i]
                print "     top is", first,i
                # move left to top
                matrix[first][i] = matrix[last-offset][first]
                print "     left is", last-offset, first
                # move bottom to left
                matrix[last-offset][first] = matrix[last][last-offset]
                print "     bottom is", last, last-offset
                # move right to bottom
                matrix[last][last-offset] = matrix[i][last]
                print "     right is", i,last
                # top to right
                matrix[i][last] = top
