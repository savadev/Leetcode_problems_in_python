'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


Approach: time complexity = O(N) and space is O(1) [ 26 size array and very very less dict is used]

The problem is solved in the same way how isomorphic strings are solved
The pattern array carries the index of the first occurance of the character.
And dict carries the index of the first occurance of the word.

whenever a character and word are encountered, the values (indexes) of it are cross-checked.

If it is not same then it returns False
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()):
            return False
        pattern_array = [-1]*26
        word_dict = dict()
        count = 0
        idx = 0 
        for idx in range(len(pattern)):
            char = pattern[idx]
            index = ord(char) - ord('a')
            if pattern_array[index] == -1:
                pattern_array[index] = idx
        for each_word in str.split():
            if each_word not in word_dict:
                word_dict[each_word] = count
            if word_dict[each_word] != pattern_array[ord(pattern[count]) - ord('a')]:
                return False
            count += 1
        return True
