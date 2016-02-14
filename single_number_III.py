'''
Question: 
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Approach: Inline comments were given.
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0 or len(nums) == 2 :
            return nums
        else:
            # More than 2 numbers are there in the list
            # now do XOR of all numbers.
            # this will return the XOR of Two distinct numbers. 
            # All other numbers will be cancelled out
            result = 0
            for each_num in nums:
                result ^= each_num
            # The result is the XOR of two numbers
            # Wherever there are 1 in the result, it means those bits of the distinct numbers are
            # different. Either one is 1 and other is 0 or vice-versa
            # Now if I find the rightmost bit of the result which is 1 then
            # I can create two groups from the given list
            # And the two distinct numbers will fall in different groups (yeah always!)
            # so XORing on the two groups will give the two distinct numbers value
            
            
            # Find the right most bit:
            # This is challenging. 
            # One easiest way is finding the 2's complement and doing and operation with the result
            # 2's complement = 1's complement+ 1 . 
            # 1's complement = change 0 to 1 and 1 to 0
            # -result = 2's complement
            result = result & -result
            print result
            # Now find the the two groups
            # Do XOR operation.
            # the result list will have the distinct numbers
            result_list = [0, 0]
            for each_num in nums:
                if each_num & result == 0:
                    result_list[0] ^= each_num
                    print 
                else:
                    result_list[1] ^= each_num
            return result_list
