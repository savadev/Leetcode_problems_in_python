'''
Question: 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Approach: 
Dynamic programming.
Traverse from end to begin.

check whichever is max(nums[idx+1], nums[idx+2]+nums[idx]) store it in nums[idx]

'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0 
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            for idx in range(len(nums)-2, -1, -1):
                if idx+2 >= len(nums):
                    nums[idx] = max(nums[idx+1], nums[idx])
                else:
                    nums[idx] = max(nums[idx+1], nums[idx+2]+nums[idx])
                
            return nums[idx]
                
                
        
