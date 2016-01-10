'''
Approach:Divie and Conquer approach
The resultant list contians all the elements with count in it.
'''
class Solution(object):
    def merge(self, left_list, right_list):
        #print left_list, right_list
        left_len = len(left_list)
        right_len = len(right_list)
        idx = 0
        idy = 0
        final_list = list()
        while idx< left_len or idy < right_len:
            if idx == left_len:
                # no more idx
                final_list.append(right_list[idy])
                idy += 1
            elif idy == right_len:
                # no more idy
                final_list.append(left_list[idx])
                idx += 1
            else:
                if left_list[idx][0] == right_list[idy][0]:
                    #print "here", left_list[idx], right_list[idy], right_list[idy][0], left_list[idx][1] + right_list[idy][1]
                    final_list.append((right_list[idy][0], left_list[idx][1] + right_list[idy][1]))
                    idx += 1
                    idy += 1
                elif left_list[idx][0] > right_list[idy][0]:
                    final_list.append(right_list[idy])
                    idy += 1
                elif left_list[idx][0] <= right_list[idy][0]:
                    final_list.append(left_list[idx])
                    idx += 1
        # final_list
        return final_list
    def  majority(self, nums , low, high):
        # Base condition
        if low > high:
            return #?
        elif low == high:
            return [(nums[low], 1)]
        else:
            # Recursive case
            mid = (low + high)/2
            left_list = self.majority(nums, low, mid)
            right_list = self.majority(nums, mid+1, high)
            # Merge left and right
            return self.merge(left_list, right_list)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        else:
            final_list = list()
            final_list = self.majority(nums, 0, nums_len-1)
            #print final_list
            # From the final_list pick one
            max_element = float('-inf')
            max_count = float('-inf')
            for idx in range(len(final_list)):
                element = final_list[idx]
                if max_count < element[1]:
                    max_count = element[1]
                    max_element = element[0]
            return max_element
