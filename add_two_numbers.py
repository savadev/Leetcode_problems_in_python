# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insert(self, val):
        if self.result == None:
            # New list
            self.result = ListNode(val)
        else:
            # List has values
            # Go till last element
            # temp ptr is created
            ptr = self.result
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = ListNode(val)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNod
        """
        '''
        Cases to be handled:
        1. When l1 and l2 are empty
        2. When l1 is empty but not l2
        3. When l2 is empty but not l1
        4. When both l1 and l2 aren't empty
        '''
        if l1 == None and l2 == None:
            return l1 or l2
        elif l1 == None or l2 == None:
            return l1 or l2
        else:
            # Both aren't empty
            result = ListNode(0)
            ptr = result
            carry_forward = 0
            while l1 != None or l2!= None:
                if l1 == None:
                    # l1 list is empty
                    val = l2.val + carry_forward
                    l2 = l2.next
                elif l2 == None:
                    # l2 list is empty
                    val = l1.val + carry_forward
                    l1 = l1.next
                else:
                    val = l1.val + l2.val + carry_forward
                    l1 = l1.next
                    l2 = l2.next
                carry_forward = 0
                if val >= 10:
                    carry_forward = 1
                    val = val-10
                temp = ListNode(val)
                ptr.next = temp
                ptr = ptr.next
            if carry_forward == 1:
                temp = ListNode(carry_forward)
                ptr.next = temp
                ptr = ptr.next
            # reverse the resultant list
            print result
            return result.next