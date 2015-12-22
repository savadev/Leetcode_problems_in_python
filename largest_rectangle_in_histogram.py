class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        The problem requires the largest area of a rectangle.
        Stack is used for this.
        When u pop and element the element's area should be calculated.
        To calculate an area, the left boundary and right boundary should be known.
        Left boundary is the index of the previous element (previous element of one that is popped) in stack
        Right boundary is the index of the current element which is being processed
        Width = right boundary - left boundary - 1
        height = height of the element that is popped
        
        How the stack is built ?
        
        The stack maintains the indexes of the element. 
        The stack is pushed with an index only when an element is bigger than the top of the stack.
        
        If the current element is not bigger than the top of the stack then 
        area of all the elements which are bigger than the current element must be found and popped before the current
        element is pushed to the stack.
        
        By this way, what is inferred ?
        
        The stack has elements in increasing order. (stack maintains the indexes)
        An element is between two things:
        
        In stack:
        prev_element - element - next element 
        
        prev_element = left boundary which cant be considered for the area
        next_element = element that can be considered for the area (but this is not the right boundary)
        
        To simplify everything, the given input list is appended with 0 at last
        and stack is initialized with -1 value
        
        By this all elements are processed and the areas are found.
        '''
        height.append(0)
        stack = [-1]
        max_area = 0
        h_len = len(height)
        for idx in range(h_len):
            current_element = height[idx]
            # Get the top of the element. The element is not removed from the stack.
            top_of_stack = height[stack[-1]] # Top of the element
            # check if the current element is bigger than top of stack
            # If yes add it to the stack
            # Else remove all the elements that are bigger than the current element and find its area. 
            # Keep only the area with max value.
            if current_element > top_of_stack:
                stack.append(idx) # Add the index of the current element to the stack
            else:
                # while loop 
                while current_element < top_of_stack:
                    # remove the top of stack element
                    popped_element = height[stack.pop()] # top element is popped
                    # Find the area of the popped element
                    # left boundary is the previous element index of the popped element 
                    # which is nothing but the top of the stack now.
                    left_boundary = stack[-1]
                    # right boundary is the index of the current element which is stored in idx variable
                    right_boundary = idx
                    width_value = right_boundary - left_boundary - 1
                    # Height is the popped element value
                    height_value = popped_element
                    current_area = height_value * width_value
                    if current_area > max_area:
                        max_area = current_area
                    # Now update the top_of_stack variable with the current top most element of the stack
                    top_of_stack = height[stack[-1]]
                # Once the while is over
                # add the current element's idx to the stack
                stack.append(idx)
        return max_area
                
            
        