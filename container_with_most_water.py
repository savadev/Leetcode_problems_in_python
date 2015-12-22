class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        The code is to find the area of the rectangle thats it!
        The code works perfectly for any input
        But time limit is exceeded all the time
        complexityy is 0(n^2)
        """
        h_len = len(height)
        #table = [[None for idx in range(h_len)] for idy in range(h_len)]
        max_area = float('-inf')
        # For 2 points
        for idx in range(h_len-1):
            # find area between these two points
            area = min(height[idx], heigeht[idx+1])
            if max_area < area:
                max_area = area
        # For more than 2 points
        for lent in range(3, h_len+1):
            for idx in range(h_len-lent+1):
                idy = idx+lent-1
                area = min(height[idx],height[idy]) * (idy-idx)
                # print height[idx:idy+1], area, idy, idx
                if area > max_area:
                    max_area = area
        return max_area
                