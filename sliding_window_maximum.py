'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Approach: O(nk)
Just move the sliding window every time and find the maximum. no tricky!
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0 or k > len(nums):
            return []
        else:
            # build a queue
            queue = list()
            idx = 0
            while True:
                queue.append(nums[idx])
                if idx+1 == k:
                    break
                idx += 1
            final_list = list()
            final_list.append(max(queue))
            idx += 1
            while idx <= len(nums)-1:
                # remove an element from queue
                queue.pop(0)
                # add an element into queue
                queue.append(nums[idx])
                final_list.append(max(queue))
                idx += 1
            print final_list
            return final_list
