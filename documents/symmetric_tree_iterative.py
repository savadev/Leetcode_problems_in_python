# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
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
            # Two queues for the two branches of the binary tree
            left_queue = []
            right_queue = []
            # insert the left element in the left q
            if root.left != None:
                left_queue.append(root.left)
            # insert the right element in the right q
            if root.right != None:
                right_queue.append(root.right)
            while len(left_queue) != 0 and len(right_queue) != 0:
                # pop the left element
                left_node = left_queue.pop(0)
                # pop the right element
                right_node = right_queue.pop(0)
                if left_node.val != right_node.val:
                    return False
                # Now insert the left , right in left queue
                if (left_node.left == None and right_node.right != None) or (left_node.left != None and right_node.right == None):
                    return False
                elif (left_node.right == None and right_node.left != None) or (left_node.right != None and right_node.left == None):
                    return False
                if left_node.right != None:
                    left_queue.append(left_node.right)
                if left_node.left != None:
                    left_queue.append(left_node.left)
                # Now insert the right, left in right queue
                if right_node.left != None:
                    right_queue.append(right_node.left)
                if right_node.right != None:
                    right_queue.append(right_node.right)
            if len(left_queue) != 0 or len(right_queue) != 0:
                return False
            return True
            
            