'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Naive approach: Using Two stacks One is a normal stack that stores values in it. Another is a stack that stores the min value elements


Efficient approach: Using only one stack and one extra variable. The extra variable stores the minimum element. The stack stores the gap between the given value and minimum value. It doesn't store the original value as it is.
'''
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.stack) == 0:
            self.min = x
            self.stack.insert(0, x-self.min)
        else:
            self.stack.insert(0, x-self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: nothing
        """
        pop = self.stack.pop(0)
        if pop < 0:
            self.min = self.min - pop

    def top(self):
        """
        :rtype: int
        """
        if self.stack[0] < 0:
            return self.min
        else:
            return self.stack[0]+self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
