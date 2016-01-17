'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Ways to solve this problem:
1. Naive approach
2. KMP algorithm - Returns all the occurance of the pattern
3. Boyd-Moore Algorithm - Returns only the first occurance
4. Karp-rabin algorithm


Implemented here is KMP algorithm

Look at this to understand what I did: [Simple steps are given]
https://web.stanford.edu/class/cs97si/10-string-algorithms.pdf

Steps:
1. compute the pi array  - contains the longest suffix index (something like that - it is well explained in the standford PDF)
2. Use it to find the pattern. 
'''
class Solution(object):
    def strStr(self, haystack, needle):
        T = haystack
        P = needle
        pi = [-1]*(len(P)+1)
        idx = 0
        pi[0] = -1
        k = -1
        while idx <= len(P)-1:
            # find all the prefixes for this index
            #print k
            while k >= 0 and P[k] != P[idx]:
                k = pi[k-1]
            k = k+1
            pi[idx+1] = k 
            idx += 1
        #print pi
        # apply KMP algorithm
        idx = 0
        match_found = True
        text_count = 0
        starting_index = 0
        shift = 0
        matched = 0
        while idx <= len(P)-1:
            #print idx, text_count, len(T)
            if text_count >= len(T):
                match_found = False
                break
            if P[idx] != T[text_count]:
                #print "mismatch", matched
                # no match
                match_found = True
                shift = matched - pi[matched]
                #print "shift is", shift
                starting_index += shift
                text_count = starting_index
                idx = 0
                matched = 0
            else:
                matched += 1
                idx += 1
                text_count += 1
        if match_found:
            return starting_index
        else:
            return -1

