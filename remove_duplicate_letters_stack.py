'''
Question:
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make
sure your result is the smallest in lexicographical order among all possible results.

Approach:
Stack. simple

Remove the element from stack
when :
1. the top of the stack is greater than current char
2. Top of stack count/freq is not 0
do it in while loop

Inline comments are given
'''
from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        # use stack
        if len(s) == 0:
            return s
        else:
            freq = Counter(s)
            stack = list()
            visited = [False]*26 # To track if the character is in stack or not.
            #print "S is", s
            for each_char in s:
                #print "each char", each_char
                freq[each_char] -= 1 # decrementing the character count
                if each_char in stack:
                    # The character is already in the stack.
                    # Do not disturb 
                    continue
                else:
                    # Check if the top of the character is greater than the current character
                    # If yes check if the count of the top character is not zero
                    # if it is zero then u can't remove the element from the stack so come out
                    # Now the top of character is not equal to zero
                    # which means it is occurring some where in the later part of the string
                    # so you can remove the characer. Do it in a while loop until the stack is empty of the top of stack is
                    # lesser than the current character
                    while len(stack) !=0  and stack[0] > each_char and freq[stack[0]] != 0:
                        # remove the top of stack and change its index in the visited array to False
                        top = stack[0]
                        stack.pop(0)
                        visited[ord(top)-ord('a')] = False
                        #print stack
                    # push the character into the stack
                    stack.insert(0, each_char)
                    visited[ord(each_char)-ord('a')] = True
                    #print stack
            stack.reverse()
            return "".join(stack)
                    
            
        
