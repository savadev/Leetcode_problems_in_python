'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

Approach : 
Naive one:
Sort it 
and get all indexes and check if there is one
O(nlgn) and space O9n)

Best apprroach:
hash a K-length moving window of nums. When moving along, do not reconstruct the set, just add the new one, and remove the earliest element.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<=k:
            return len(nums) >  len(set(nums))

        hashSet=set(nums[:k])
        if len(hashSet) < k:
            return True

        for i in xrange(k,len(nums)):
            hashSet.add(nums[i])
            if len(hashSet)==k:
                return True
            else:
                hashSet.remove(nums[i-k])
        return False
        
So if any sliding window problem comes:

Do this:

1. Create a set with the size of the sliding window. The set will have the first K elements of the given array
2. Now traverse from k+1 to the end of the loop. And add the element to the hash set. If the hash set grows then remove the earliest element
otherwsie return True [For this problem]
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        new_list = nums[:]
        new_list.sort()
        #print new_list
        value = None
        for idx in range(len(new_list)-1):
            if new_list[idx] == new_list[idx+1]:
                value = new_list[idx]
                break
        if value == None:
            return False
        idx = 0
        indexes = []
        while idx <= len(nums)-1:
            if nums[idx] == value:
                indexes.append(idx)
            idx += 1
        for idx in range(len(indexes)-1):
            if indexes[idx+1] - indexes[idx] <= k:
                return True
        return False
