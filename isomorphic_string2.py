'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.


Approach : 
This is the best approach. Time - O(n) and space O(1)

Use a 256 array for s and t.

Store the index of the words that u visit in the array

When u see the same word again check if the index of the character is same. If not return False

'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_dict = [0]*256
        t_dict = [0]*256
        for idx in range(len(s)):
            print ord(s[idx])
            if s_dict[ord(s[idx])] == 0:
                s_dict[ord(s[idx])] = idx+1
            if t_dict[ord(t[idx])] == 0:
                t_dict[ord(t[idx])] = idx+1
                
            if s_dict[ord(s[idx])] != t_dict[ord(t[idx])]:
                return False
        return True
