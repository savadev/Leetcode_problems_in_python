'''
Question : Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

Approach : Use two stacks. One stack is the take the elements and another stack is to have the count of the children 
stack = list() takes the element from preorder
count = list() keeps track of how many children processed for a parent

Whenever you insert an element in to the stack , insert 2 into the counter and decrement the top of the stack by 1 before inserting the element.
Whenever you see # decrement the counter by 1

Take care of the edge cases. that's it ! 

But this is not a good approach

Approach 2: Solve this problem without using stacks. Just with a variable.

We just need to remember how many empty slots we have during the process.

Initially we have one ( for the root ).

for each node we check if we still have empty slots to put it in.

a null node occupies one slot.
a non-null node occupies one slot before he creates two more. the net gain is one.

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot

        p = preorder.split(',')

        #initially we have one empty slot to put the root in it
        slot = 1
        for node in p:

            # no empty slot to put the current node
            if slot == 0:
                return False

            # a null node?
            if node == '#':
                # ocuppy slot
                slot -= 1
            else:
                # create new slot
                slot += 1

        #we don't allow empty slots at the end
        return slot==0
        
Very simple. easy to understand.
'''
class Solution(object):
    def check_stack(self, stack, counter):
        # atmost only 2 elements should be there in the stack
        if len(stack) > 2:
            return False
        idx = 0
        while idx <= len(stack)-1:
            if counter[idx] != 0:
                return False
            idx += 1
        return True
    def check_decrement(self, counter, stack):
        # if top of the stack is empty return False
        # if the count of the top of the stack is 0 return False
        # else decrement the count and return True
        if len(counter) == 0:
            return False
        counter[0] -= 1
        # after decrementing the counter if the value becomes zero then the element has to be
        # popped out from the counter and stack
        idx = 0
        while True:
            #print stack, counter
            if len(counter) != 0 and counter[0] == 0:
                counter.pop(0)
                stack.pop(0)
            else:
                break
            idx += 1
        return True
    def check_increment(self, counter, stack, element):
        # if the top of the stack is empty return False
        # if the count of the top of the stack is 0 return False
        # else decrement the counter and insert the new element into the stack and 
        # insert 2 in the counter too
        if len(counter) == 0:
            return False
        if counter[0] == 0:
            stack.pop(0)
            counter.pop(0)
        if len(counter) != 0:
            counter[0] -= 1
            counter.insert(0,2)
            stack.insert(0, element)
            return True
        return False
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if len(preorder) == 0:
            return False
        # iterate through the preorder and store it in the stack
        preorder = preorder.split(",")
        if len(preorder) == 1 and preorder[0] == "#":
            return True
        #print preorder
        stack = list()
        # each element in the stack as counter initialized to 2. This will be decremented when an element is added to the 
        # the stack or the next element is #
        # keep an another stack for maintaining the count of each element
        counter = list()
        # add the root element before processing rest of the elements in the preorder list
        if preorder[0] == "#":
            return False
        stack.insert(0, preorder[0])
        counter.insert(0, 2)
        for idx in xrange(1, len(preorder)):
            element = preorder[idx]
            #print stack, counter, element
            if element.strip() == "#":
                # decrement the counter of the top of the stack 
                if self.check_decrement(counter, stack) == False:
                    return False
            else:
                # the element is not #. Its a numerical value
                # insert the element into the stack
                if self.check_increment(counter, stack, element) == False:
                    return False
        if self.check_stack(stack, counter):
            return True
        return False
