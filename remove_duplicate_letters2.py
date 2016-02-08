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

Slice the string from the index of the first occurance of the character till the end. check if the set(slice string) == set(given_string)
if yes, it means the character is found and the rest of the characters can be found from the sliced string. again follow the two steps
mentioned above for the sliced string.\

Example:
def removeDuplicateLetters(s):
    for c in sorted(set(s)):
        print "the character is", c
        suffix = s[s.index(c):]
        print "    the suffix and set is", suffix, set(s)
        if set(suffix) == set(s):
            print "    calling recursively"
            return c + removeDuplicateLetters(suffix.replace(c, ''))
    return ''


print removeDuplicateLetters("cbacdcbc")

output:
the character is a
    the suffix and set is acdcbc set(['c', 'b', 'a', 'd'])
    calling recursively
the character is b
    the suffix and set is bc set(['c', 'b', 'd'])
the character is c
    the suffix and set is cdcbc set(['c', 'b', 'd'])
    calling recursively
the character is b
    the suffix and set is b set(['b', 'd'])
the character is d
    the suffix and set is db set(['b', 'd'])
    calling recursively
the character is b
    the suffix and set is b set(['b'])
    calling recursively
acdb

Then follow the steps mentioned above.
'''
class Solution(object):
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''
            
        
