class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        Same as add two numbers == target concept
        here no target is given. find the max area
        '''
        left_boundary = 0
        right_boundary = len(height)-1
        max_area = float('-inf')
        while left_boundary < right_boundary:
            current_area = min(height[right_boundary], height[left_boundary]) * (right_boundary-left_boundary)
            if current_area > max_area:
                max_area = current_area
            if height[left_boundary] < height[right_boundary]:
                left_boundary += 1
            elif height[left_boundary] > height[right_boundary]:
                right_boundary -= 1
            else:
                left_boundary += 1
                right_boundary -= 1
        return max_area
                