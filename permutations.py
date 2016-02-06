'''
Return all permutations for distinct numbers

Approach : Knuth Algorithm (Linear time)

Steps:
1. Find X index
2. Find Y index
3. Swap X_index value and Y_index value
4. Reverse from X_index +1 to end of the list

How to find X_index:
X_index is the index of a value which is lesser than its next value.
Traverse from the last to first. Check if idx is greater than idx-1 if not break. x_index is idx-1

How to find Y_index:
Y_index is the index of a value which is last value which is greater than the value present in the x_index
Traverse from x_index+1 to end of the list. Compare the x_index value with the values from x_index+1 till the end.
If nums[x-index] > nums[idx] then  idx-1 is the y_index

example:

nums = [5,1,7,6,3,9,8,4,2]
index= [0,1,2,3,4,5,6,7,8]
Here x_index is 4 and the value at index 4 is 3
Now to find the y_index
compare 3 with x_index+1 to end
3 < 9
3 < 8
3 < 4
3 < 2 [fails here] so y_index is index value of 4.

Now swap the x_index and y_index 

Reverse from x_index+1 till the end of the list

The result is next lexicographic order of the given number
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return nums
        else:
            nums.sort()
            final_list = list()
            final_list.append(nums[:])
            while True:
                idx = len(nums)-1
                x_index = -1
                while idx >= 0:
                    current = nums[idx]
                    next = nums[idx-1]
                    if next < current:
                        x_index = idx-1
                        break
                    idx -= 1
                if x_index == -1:
                    break
                idx = x_index+1
                x_value = nums[x_index]
                while idx <= len(nums)-1:
                    current = nums[idx]
                    if x_value > current:
                        break
                    y_index = idx
                    idx += 1
                # now swap x and y
                nums[x_index], nums[y_index] = nums[y_index], nums[x_index]
                # reverse from x+1 to end
                idx = x_index+1
                idy = len(nums)-1
                while idx <= idy:
                    nums[idx], nums[idy] = nums[idy], nums[idx]
                    idx += 1
                    idy -= 1
                final_list.append(nums[:])
            return final_list
