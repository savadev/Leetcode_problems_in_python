'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Approach : Space complexity : O(1) and time complexity : O(n)

1. Reverse n-k elements
2. Reverse last K elements
3. Revese all the elements

example: [1,2,3,4,5,6,7,8] k = 4

After n-k reversal: [4, 3, 2, 1, 5, 6, 7, 8]
After last k elements reversal: [4, 3, 2, 1, 8, 7, 6, 5]
After reversal of all the elements: [5, 6, 7, 8, 1, 2, 3, 4]

Result: [5, 6, 7, 8, 1, 2, 3, 4]
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > 0 and len(nums) > 1:
            n = nums
            k = k%len(n)
            # reverse n-k elements
            idk = len(n)-1-k
            idx = 0
            while idx < idk:
                nums[idx], nums[idk] = nums[idk], nums[idx]
                idx += 1
                idk -= 1
            print nums
            # reverse the last k elements
            idk = len(n)-1-k+1
            idy = len(n)-1
            while idk < idy:
                nums[idk], nums[idy] = nums[idy], nums[idk]
                idk += 1
                idy -= 1
            print nums
            # now revese eveything
            idx = 0
            idy = len(n)-1
            while idx < idy:
                nums[idx], nums[idy] = nums[idy], nums[idx]
                idx += 1
                idy -= 1
            print nums
                
