'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Approach : simple to understand.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head.next == None or head.next.next == None:
            return head
        else:
            # More than two nodes in the list
            even_node = head.next
            odd = None
            even = None
            current = head
            while current.next != None:
                if odd == None:
                    odd = current
                else:
                    odd.next = current
                    odd = odd.next
                if even == None:
                    even = current.next
                else:
                    even.next = current.next
                    even = even.next
                if current.next.next != None:
                    current = current.next.next
                else:
                    current.next = None
                    current.next = even_node
                    break
            odd.next = current
            even.next = None
            current.next = even_node
            return head
                
