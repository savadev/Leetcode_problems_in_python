'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Approach: Space - O(1) and Time: O(n) 
Check inline comments.

Link: https://leetcode.com/problems/linked-list-cycle/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        elif head.next == None:
            return False
        else:
            # The algorithm is to find if the cycle exists with a single pointer
            # Credit goes to my Professor. 
            # If there is a cycle then it can be assumed as circle.
            # so the objective is look out for the circle.
            # How?
            # Remember the node after every 2^K steps. 
            # At one point of the time the current node will be node which we remembered which confirms there is a cycle.
            # This will take more number of iterations to find the cycle but it does it using a single pointer.
            # As usual, if there is no cycle then the last element of the linked list node will point to None ane the loop breaks.
            current = head
            # step function
            step = 1
            # the next step function
            new_step = step
            # node to be remembered
            node = None
            while current != None:
                if current == node:
                    # cycle found
                    return True
                if step == new_step:
                    # New 2^K step is reached
                    # Update the new step value and node
                    node = current
                    new_step = step*2 
                step += 1
                current = current.next
            return False
