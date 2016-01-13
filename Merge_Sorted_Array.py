'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Approach: [RAJ's idea]

Go from the last. Whichever is the biggest copy it to the end of the array nums1

Repeat it till the start of the array is reached.

Time complexity: m+n

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        idx = m-1
        idy = n-1
        #print nums1, m, nums2, n
        while index >=0 :
            if idx < 0:
                # no elements in in the array nums1
                nums1[index] = nums2[idy]
                idy -= 1
                index -= 1
            elif idy < 0:
                # no elements inthe array  nums2
                break
            elif nums1[idx] >= nums2[idy]:
                # copy the element to the index
                nums1[index] = nums1[idx]
                index -= 1
                idx -= 1
            elif nums1[idx] <= nums2[idy]:
                nums1[index] = nums2[idy]
                index -= 1
                idy -= 1
            #print nums1, idx, idy, index
        #print nums1
        
                
