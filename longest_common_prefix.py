'''
Longest common prefix

Write a function to find the longest common prefix string amongst an array of strings.

Approach:
Simple approach
Take the first word and compare with the rest of the words.
Take the common prefix characters that matches all elements in the array
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
            break
        #print max_str
        return max_str
