'''
Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Approach : Bottom up approach DP - O(n^2)

Best approach: O(N) time complexity O(1) space complexity

Initialization : 
First = first element of list
second = float('inf')

Iteration:
1. Break the sequence only when the current number is less than the second number.
2. Change the first number when the current number is less than to it.
3. Else True

Example:
[1,2,-1,3]
Here the sequence 1,2 is not broken when -1 is processed. 
[1,2,-3,-2,-1]
Here the sequence 1,2 is broken and a new sequence -3, -2 is found.
[1,3,2,3]
Here the sequence 1,3 is broken to 1,2 when 2 is processed.

Try to understand on your own if the explanation isnt understandable.
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) < 3:
            return False
        else:
            first = nums[0]
            second = float('inf')
            for idx in xrange(1, len(nums)):
                current = nums[idx]
                if current <= first:
                    first = current
                elif current <= second:
                    second = current
                else:
                    return True
            return False
