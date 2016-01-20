'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    
Approach: Simple mathematical aproach. Mod and div of 26
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        final_str = ""
        while n != 0:
            final_str = chr((n-1)%26 + 65) + final_str 
            n = (n-1)/26
        return final_str
        
