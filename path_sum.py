# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Cases to be considered:
1. Empty Tree
2. Tree with no children
3. Tree with children in left or only in right
4. Tree with 2 children

[] - empty tree return false
[1] sum = 1 ; tree with no children but equals sum return false
[1,null,2] sum = 1; tree with right child but root itself equls sum return false
[1,2,null,3,null,4,null,5,null] sum = 6; Tree with left children alone . return false 

If there are negtive values in the tree
better add all the values in the path and compare it with the sum instead of subtracting the value from sum and sending it again
recursively.
'''

class Solution(object):
    def findpath(self, root, tree_sum, sum):
        if root == None:
            if sum == tree_sum:
                return True
            return False
        else:
            if root.left != None and root.right != None:
                return self.findpath(root.left, tree_sum+root.val, sum) or self.findpath(root.right, tree_sum+root.val, sum)
            elif root.left == None and root.right != None:
                return self.findpath(root.right, tree_sum+root.val, sum)
            else:
                return self.findpath(root.left, tree_sum+root.val, sum)
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        elif root.left == None and root.right == None and root.val == sum:
            return True
        else:
            if root.val == sum:
                return False
            else:
                return self.findpath(root, 0, sum)
