# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def height(self, root):
        if root == None:
            return -1
        else:
            #print "root val is", root.val
            return max(self.height(root.left), self.height(root.right))+1
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str

        It serializes a tree into : node,node,node,node,#,#,node,#,
        It ends with a ',' at the end.
        """
        if root == None:
            return ""
        elif root.left == None and root.right == None:
            return str(root.val) + str(",")
        else:
            # Find the height of the tree
            height = self.height(root)
            #print height
            # Queue to do level by level processing
            q = []
            q.append(root)
            q.append(None)
            final_list = ""
            while len(q) != 0 and height > 0:
                # pop the element
                element = q.pop(0)
                if element == None:
                    height = height - 1
                    q.append(None)
                elif element == "#":
                    final_list += "#"
                    final_list += ","
                else:
                    final_list += str(element.val)
                    final_list += ","
                    if element.left != None:
                        q.append(element.left)
                    else:
                        q.append("#")
                    if element.right != None:
                        q.append(element.right)
                    else:
                        q.append("#")
            for each_element in q:
                if each_element != None:
                    if each_element != "#":
                        final_list += str(each_element.val)
                        final_list += ","
                    else:
                        final_list += "#"
                        final_list += ","
            return final_list
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode

        deserialize is done in similar way to serialize
        A queue is maintained to track the nodes.

        """
        data = data.split(",")
        d_len = len(data)-1 # Since the data has "," at the end the len of data is decremented by 1
        if d_len == 0:
            return 
        else:
            # Get the root element
            root = TreeNode(data[0])
            q = []
            q.append(root)
            idx = 1
            while len(q) != 0 and idx < d_len-1:
                # pop the element
                node = q.pop(0)
                # set its left and right
                if data[idx] != "#":
                    node.left = TreeNode(data[idx])
                    q.append(node.left)
                if data[idx+1] != "#":
                    node.right = TreeNode(data[idx+1])
                    q.append(node.right)
                idx += 2
            return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))