class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Manacher’s Algorithm
        '''
        '''
        i = 0
        i_mirror = 0
        c = 0
        r = 0
        # stuff "#" in between characters
        org = s
        s = list(s)
        count = 0
        for idx in xrange(len(s)+1):
            s.insert(count, "#")
            count += 2
        s = "".join(s)
        n = len(s)
        p = [0]*n
        for i in xrange(1, n):
            # calculate the mirror of which is 2*c-i
            i_mirror = 2*c-i
            # check if the mirror value is symmetry to i
            # how ? if p[i_mirror] <= r-i then p[i] = p[i_mirror] else p[i] = r-i + extra characters
            if i < r:
                if p[i_mirror] <= r-i:
                    p[i] = p[i_mirror]
                else:
                    p[i] = r-i
            else:
                p[i] = 0
            # Find the remaining palindrome for the center c
            right = i + 1 + p[i]
            left = i -1 - p[i]
            while left >= 0 and right <= n-1 and s[left] == s[right]:
                p[i] += 1
                right = i + 1 +p[i]
                left = i -1 - p[i]
            # Now check if the palindrome expanded than R's index
            if p[i] > r-i:
                # change the center to i
                # increment the R
                c = i
                r = i + p[i]
        # Find the max in the p
        center_index = 0
        max_len = 0
        for idx in xrange(len(p)):
            if p[idx] > max_len:
                max_len = p[idx]
                center_index = idx
        if max_len == 0:
            return org[center_index]
        final_str = ''
        for idx in range(center_index - max_len, center_index + max_len+1):
            if s[idx] != "#":
                final_str += s[idx]
        return final_str
        
            
        