'''
Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Approach: BFS
Link :  https://leetcode.com/discuss/62229/short-python-solution-using-bfs [Nice vizualization]
'''
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        else:
            # Think it as a Tree problem. (Hey! Not a binary tree or binary search tree. a tree with many childrens is possible)
            # Apply BFS. The root node is given number n. BFS means go level by level
            # How to find the next level of nodes?
            # First get a list of perfect squares less than the given number. [sorted order]
            # Now get the positive difference of each number in the list with the given number
            # These numbers are the node of next level.
            # Hey! Again, don't think that u have to have a tree data structure with left, right, bla , bla
            # just store the difference in a set (to avoid duplicate numbers) and process the number again and get difference
            # Stop when the difference become 0 or the number is in the list/set of nodes.
            # Have a counter. The counter says how many level u have gone till the u get the value 0
            perfect_squares = list() # This list wont change. The list is used to generate the next level of nodes for BFS
            i = 1
            while i*i <= n:
                perfect_squares.append(i*i)
                i += 1
            nodes = set()
            nodes.add(n)# Now root node only. so the nodes has only one element
            counter = 1
            while len(nodes) != 0: # Runs for 
                # pick each element from the nodes list and get the difference from its parent
                new_nodes = set()
                for parent_node in nodes:
                    for each_node in perfect_squares:
                        if parent_node == each_node:
                            return counter
                        if each_node > parent_node:
                            # If the child number is greater than parent then u will get negative diff so avoid it
                            break
                        new_nodes.add(parent_node - each_node)
                counter += 1
                nodes = new_nodes
                        
