'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Approach : Deque O(N)

Condition :
The largest element in the Deque should always be first element. 

How to add the elements in the Deque to satisfy the above condition ?
If the element to be added is greater than the last element in the deque then
    remove the element from right in the deque iteratively till the element in deque is greater than the current element
Add the element into the dequeu at right side (back of deque)

Now when to remove the element from deque ?

When the size of the deque is greater than or equal to the window size OR the index of the first element in deque - curent element idx
is greater than the window size then
    remove the element in the left end of the deque iteratively
'''
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        else:
            queue = deque()
            idx = 0
            final_list = list()
            # First K elements are processed and added to the deque
            while idx < k:
                '''If the element to be added is greater than the last element in the deque then
                remove the element from right in the deque iteratively till the element in deque is greater than the current element
                Add the element into the dequeu at right side (back of deque)'''
                while len(queue) != 0  and queue[-1][1] < nums[idx]:
                    queue.pop()
                queue.append((idx,nums[idx]))
                idx += 1
            # first maximum element is taken from the queue's first element
            final_list.append(queue[0][1])
            # rest of the elements are procesed 
            while idx <= len(nums)-1:
                '''
                When the size of the deque is greater than or equal to the window size OR the index of the first element in deque - curent element idx is greater than the window size then     remove the element in the left end of the deque iteratively
                '''
                while len(queue) == k or len(queue) != 0  and abs(queue[0][0] - idx) >= k:
                    queue.popleft()
                while len(queue) != 0  and queue[-1][1] < nums[idx]:
                    queue.pop()
                queue.append((idx,nums[idx]))
                final_list.append(queue[0][1])
                idx += 1
            return final_list
