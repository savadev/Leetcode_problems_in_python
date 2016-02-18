'''
Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

Approach :
Worst case approach: 
Two for loops
Check set(a).intersection(b) == 0. If it is 0 then there is no common words between two words. get the length.
return the maximum length

code:
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
        else:
            # Bottom up approach
            final_list = [0]*len(words)
            for idx in xrange(len(words)):
                for idy in range(idx+1, len(words)):
                    # check if both words has any common letters
                    if len(set(words[idx]).intersection(set(words[idy]))) == 0 and final_list[idx] < (len(words[idx]) * len(words[idy])):
                        # they dont share any common words
                        final_list[idx] = len(words[idx]) * len(words[idy])
            return max(final_list)
            
Fast approach:
Change each word into a unqiue number and do and operation. If the number has same bit then it has a common word otherwise not.

Clear explanation:
Bit Manipulation.

1. Find the ascii value for each letter. 
    ord(each_letter) - ord('a')
2. Do bit wise left shift operation


example: abcwy - 1110000000000000000001010
What does it mean?
Basically an integer would have 32 bit. The number of characters are 26. You are going to set 1 in the respective bit for a character.
0th bit is for a
1st bit is for b
.
.
.
25th bit is for z
Getting the value to set 1 in that position is calculated using ascii. ord(each_letter) - ord('a')

Now the position is found to set it in a integer ?
And: Bit wise left shift operation

1 << (ord(each_char) - ord('a')).

How to do for all characters :
Ans: OR operation

bit |= 1 << (ord(each_char) - ord('a'))

So a 32 bit integer wil have 1's set in the position from 0 to 25. and rest are 0's

By this a unique number is generated for each word ( binary to decimal gives a number which will be unique for each number)

Now to check if two numbers have common characters do AND operation.
If result == 0 no common words

return the maximum.
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
        else:
            # Bottom up approach
            bits = [0]*len(words)
            for idx  in xrange(len(words)):
                each_word = words[idx]
                for each_letter in each_word:
                    bits[idx] |= 1<<ord(each_letter) - ord('a')
            max_value =  0
            for idx in xrange(len(bits)):
                for idy in xrange(idx+1, len(bits)):
                    if bits[idx] & bits[idy] == 0 and len(words[idx]) * len(words[idy]) > max_value:
                        max_value = len(words[idx]) * len(words[idy])
            return max_value
                        
