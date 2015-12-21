class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_str = len(s)
        if len_str == 0:
            return 0
        cur_len = 1
        max_len = 1
        prev_index = 0
        visited = [-1]*256 # 256 characters
        # Take the first element of the string
        # mark it as visited and update it with its index
        visited[ord(s[0])] = 0
        # now traverse from 1 to len_str
        for each_char_index in xrange(1, len_str):
            # check if this character is already seen
            prev_index = visited[ord(s[each_char_index])]
            # If prev-index is -1 , it means the character is new one
            # Else any other value than -1, then the character is seen at the index
            
            # For new character
            if prev_index == -1:
                cur_len += 1
            else:
                # the character is already seen before at the index value which is stored in prev_index
                # Now 2 cases.
                # case 1: Does the character is in present curent longest subsequence ?
                # to check IT IS NOT present current longest sequence, 
                # get the difference between the index of this character - current_len > prev_index
                if each_char_index - cur_len > prev_index:
                    cur_len += 1
                else:
                    # the character is already in the current longest subsequence
                    # so update the cur_len 
                    # update it to the next string of prev_index
                    if cur_len > max_len:
                        max_len = cur_len
                    cur_len = each_char_index - prev_index
            # update the index in the visited array
            #print s[each_char_index], cur_len, max_len, prev_index
            visited[ord(s[each_char_index])] = each_char_index
        if cur_len > max_len:
            max_len = cur_len
        return max_len
        
                
        

        
                    
            
            
        