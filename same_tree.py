# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            # Both the trees aren't empty
            # Can check if they are same using BFS or DFS
            # q1 for tree p
            # q2 for tree Q
            # insert root's of P and Q in the two queues
            q1 = []
            q2 = []
            q1.append(p)
            q2.append(q)
            #print q1 , q2
            while len(q1) != 0 and len(q2) != 0:
                # pop the elements and check if it is same
                p_element = q1.pop()
                q_element = q2.pop()
                if p_element.val != q_element.val:
                    return False
                else:
                    # They are same
                    # Add the left and right elements
                    if (p_element.left != None and q_element.left == None) or (p_element.left == None and q_element.left != None):
                        return False
                    elif p_element.left != None and q_element.left != None:
                        q1.append(p_element.left)
                        q2.append(q_element.left)
                    if (p_element.right != None and q_element.right == None) or (p_element.right == None and q_element.right != None):
                        return False
                    elif p_element.right != None and q_element.right != None:
                        q1.append(p_element.right)
                        q2.append(q_element.right)
            if len(q1) != 0 or  len(q2) != 0:
                return False
            else:
                return True