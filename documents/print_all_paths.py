# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]

        Recursive approach
        Call left first and right second
        """
        def all_paths(root, paths, path_list):
            # Base condition
            if root == None:
                return
            else:
                # Recursive condition
                paths += str(root.val)
                if root.left == None and root.right == None:
                    path_list.append(paths)
                else:
                    all_paths(root.left, paths+"->", path_list)
                    all_paths(root.right, paths+"->", path_list)
        path_list = []
        all_paths(root, "", path_list)
        return path_list
    
        