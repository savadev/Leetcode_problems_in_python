# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        Return a mirror image of a binary tree
        """
        if root == None:
            return []
        else:
            # Level wise swap the branches of the tree
            # Level wise nothing but BFS, queue
            queue = []
            queue.append(root)
            while len(queue) != 0:
                # pop the element
                element = queue.pop()
                if element.right != None:
                    queue.append(element.right)
                if element.left != None:
                    queue.append(element.left)
                # swap the branches of the elements
                temp  = element.left 
                element.left = element.right
                element.right = temp
        return root