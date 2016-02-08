'''
Question:
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make
sure your result is the smallest in lexicographical order among all possible results.

Approach:
1. Greedy Method
Fix the first character of the output string and recursively call the function to fix the remaining character.

NOTE: if the character that u have found to be fixed has occurred in the index i
then :
1. Remove all the occurances of the characeter in the rest of the string
2. Remove all the characters that are left to the index i.

Now send this new string to the recursive function.

How to fix a character ? what is the logic?

Two cases to te checked here to fix the character.
1. Has the character is the smallest character in the string ?
2. Has the character's counter becomes 0 which means it doesn't occur any more in the given string ? 

If the second case is passed then the smallest character found from case 1 is fixed. The first case is to chose the smallest character.

Example:
fabcdbca
Here the character to be fixed is F
cbadcbac
Here the character has to be fixed if A

Then follow the steps mentioned above.
'''
from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) ==0 :
            return ""
        else:
            # Apply greedy algorithm
            # Fix the first letter and recursively fix the next letters
            # After fixing the first letter remove the letter from the rest of the array
            freq = Counter(s)
            idx = 0
            index = 0
            character = s[0]
            while idx <= len(s)-1:
                if s[idx] < character:
                    character = s[idx]
                    index = idx
                freq[s[idx]] -= 1
                print s[idx], freq[s[idx]]
                if freq[s[idx]] == 0:
                    # character found
                    break
                idx += 1
            # now remove the character from all the place in the list
            s = s.replace(character, "")
            # send only the string S from index to the end
            return character + self.removeDuplicateLetters(s[index:])
            
        
