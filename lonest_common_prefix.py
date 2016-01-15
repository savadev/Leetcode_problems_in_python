'''
Write a function to find the longest common prefix string amongst an array of strings.
Example: 

["flower", "fair", "hello", "fleet"] returns "" (null) because all the strings in the list doesn't have a common prefix
["flower", "flair", "fleet"] returns "fl"


My approach:
Take the first string and compare it with all other strings. Inside the two loops while loop to get the common prefix
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        max_len = float('inf')
        max_str = ""
        for idx in range(len(strs)):
            first_word = strs[idx]
            for idy in range(idx+1, len(strs)):
                second_word = strs[idy]
                ids = 0
                idk = 0
                current_len = 0
                current_str = ""
                while ids <= len(first_word)-1 and idk <= len(second_word)-1:
                    if first_word[ids] == second_word[idk]:
                        current_len += 1
                        current_str += first_word[ids]
                    else:
                        break
                    ids += 1
                    idk += 1
                #print current_len
                if current_len == 0:
                    return ""
                if current_len < max_len:
                    max_len = current_len
                    max_str = current_str
                    first_word = max_str
            break # this will break the outer loop after the first string is picked. After that no need to process
        #print max_str
        return max_str
                        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        N = len(strs)

        if N == 0 :
            return ""

        strs.sort()
        first = strs[0]
        last = strs[N-1]

        for j in range(0, len(first)) :
            if first[j] != last[j] :
                return first[0:j]

        return first            
