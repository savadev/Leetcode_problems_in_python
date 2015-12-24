# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def symmetry(self, left_element, right_element):
        # Base condition
        if left_element == None and right_element == None:
            return True
        elif (left_element == None and right_element != None) or (left_element != None and right_element == None):
            return False
        elif left_element.val != right_element.val:
            return False
        else:
            return self.symmetry(left_element.left, right_element.right) and self.symmetry(left_element.right, right_element.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif (root.left == None and root.right != None) and (root.left != None and root.right == None):
            return False
        else:
            # Both the sides aren't empty
            return self.symmetry(root.left, root.right)
            