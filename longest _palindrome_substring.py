class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # DP approach to solve the problem
        '''
        Base case:
        p[i,i] = True if si = si
        p[i, i+1] = True if si = si+1
        
        Recursive case:
        p[i,j] = True if p[i+1 , j-1] and si = sj
        else false
        
        So for single character and two characters the palindrome is already found
        From length 3 to n the palindrome is constructed in DP approach
        '''
        n = len(s)
        max_len = 0
        longest_seq = 0
        table = [[None for dummy_idy in xrange(n)]for dummy_idx in xrange(n)]
        for idx in xrange(n):
            table[idx][idx] = 1
            longest_seq = idx
            max_len = 1
            if idx+1 < n and s[idx] == s[idx+1]:
                table[idx][idx+1] = 1
                longest_seq = idx
                max_len = 2
        # Now check palindrome from len sequence 3 to n
        for length in xrange(3, n):
            # Need left and right boundary - a sliding window of len = length
            for left_boundary in range(0, n-length+1):
                right_boundary = left_boundary + length-1
                if s[left_boundary] == s[right_boundary] and table[left_boundary+1][right_boundary-1] == 1:
                    table[left_boundary][right_boundary] = 1
                    longest_seq = left_boundary
                    max_len = length
        # Get the substring from the index stored in the longest_seq variabe till the length stored in the max_len
        return s[longest_seq:longest_seq+max_len]

            
        