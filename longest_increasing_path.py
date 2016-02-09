
'''
Longest Increasing Path in a Matrix

Question:

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


Approach: Backtracking and Dynamic Programming.

First the longest increasing path can start at any cell from the matrix. Therefore, the entire matrix has to be iterated.
so two for loops are needed.

Now for each cell you can go left, right, up and down. But except the first cell all other cells in the matrix 
can go only 3 directions.

Why ?
If your moving in right direction from cell1 to cell2 in the matrix.
Then at cell2 you should not go to cell1. That is you should not go to left of cell2 which is cell1. Same goes for up and down.

A memo table is also used to store the values of each cell's longest possible path count so that if the same cell is to 
be seen then from memo table u can get the value.

Complexity : I don't know.
'''
class Solution(object):
    def get_longest_path(self, matrix, ridx, cidy, previous_value, direction, memo):
        # base case
        if previous_value != None and matrix[ridx][cidy] <= previous_value:
            return 0
        elif memo[ridx][cidy] != None:
            return memo[ridx][cidy]
        else:
            # The value can be taken into the count
            current_value = matrix[ridx][cidy]
            # 4 recursive cases
            left = 0
            right = 0
            up = 0
            down = 0
            # if the last direction is right don't go left
            if cidy-1 >= 0 and direction != "right":
                left = self.get_longest_path(matrix, ridx, cidy-1, current_value, "left", memo)
            # if the last direction is left don't go right
            if cidy+1 <= len(matrix[0])-1 and direction != "left":
                right = self.get_longest_path(matrix, ridx, cidy+1, current_value, "right", memo)
            # if the last direction is up don't go down
            if ridx+1 <= len(matrix)-1 and direction != "up":
                down = self.get_longest_path(matrix, ridx+1, cidy, current_value, "down", memo)
            # if the last direction is down don't go up
            if ridx-1 >= 0 and direction != "down":
                up = self.get_longest_path(matrix, ridx-1, cidy, current_value, "up", memo)
            memo[ridx][cidy] = 1+max(left, right, down, up)
            return 1+max(left, right, down, up)
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        else:
            # The matrix is of rows and columns
            r_len = len(matrix)
            c_len = len(matrix[0])
            max_len = float('-inf')
            memo = [[None for _ in range(c_len)] for _ in range(r_len)]
            for idx in range(r_len):
                each_row = matrix[idx]
                for idy in range(len(each_row)):
                    each_col = each_row[idy]
                    rv = self.get_longest_path(matrix, idx, idy, None, None, memo)
                    if max_len < rv:
                        max_len = rv
            return max_len
