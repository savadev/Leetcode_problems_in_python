'''
Question: 
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

Approach:

Similar to DP (somwhat ! not exactly)

Create a result_list with 1 as values in the size of nums

1. traverse from backwards
2. traverse from front

Step 1: traverse from backwards

while traverseing store the product so far seen in a cell. let it be prod
at position i in the result_list, update the value of the result_list as result_list[i+1] * prod

step 2: traverse from front
while traversing store the product so far seen in a cell. let it be prod
at position i in the result list, upate the value of the result_list as result_list[i-1] * prod

After this, the reuslt_list will contian the exact multiplication at each cell.

'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums
        else:
            # The list has set of number
            idx = len(nums)-2
            idy = 1
            idx_prev = nums[idx+1]
            idy_prev = nums[idy-1]
            result = [1]*len(nums)
            while idx >= 0:
                current = nums[idx]
                result[idx] = idx_prev * result[idx+1]
                idx_prev = current
                idx -= 1
            while idy <= len(nums)-1:
                result[idy] = idy_prev * result[idy]
                idy_prev *= nums[idy]
                idy += 1
            return result
