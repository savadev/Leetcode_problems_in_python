'''
Question: 
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.


Approach:
1. First sort the string. This will give the strings in lexicographic order. so one big problem is solved.
2. Now each word is sorted and tupled and store their indexes as value and the tuple as key in a dict.
Example: 
["eat", "tea", "tan", "ate", "nat", "bat"]


sorted to : [u'ate', u'bat', u'eat', u'nat', u'tan', u'tea']
defaultdict(<type 'list'>, {(u'a', u'b', u't'): [1], (u'a', u'e', u't'): [0, 2, 5], (u'a', u'n', u't'): [3, 4]})
Each word is sorted and changed into a tuple. so eat, tea, ate all becomes ('a','e','t') and their respective indexes are 0,2,5

3. Now in a loop form a list of words picked from the indexes. 
'''
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return [[]]
        else:
            freq_index_dict = defaultdict(list)
            strs.sort()
            print strs
            for idx in range(len(strs)):
                freq_index_dict[tuple(sorted(strs[idx]))].append(idx)
            print freq_index_dict
            final_list = list()
            for key, value in freq_index_dict.items():
                final_list.append(map(lambda x : strs[x], value))
            return final_list
