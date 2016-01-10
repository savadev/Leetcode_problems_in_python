'''
Moore’s Voting Algorithm

findCandidate(a[], size)
1.  Initialize index and count of majority element
     maj_index = 0, count = 1
2.  Loop for i = 1 to size – 1
    (a)If a[maj_index] == a[i]
        count++
    (b)Else
        count--;
    (c)If count == 0
        maj_index = i;
        count = 1
3.  Return a[maj_index]

'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = 0
        count = 1
        for idx in range(1, len(nums)):
            if nums[max_index] == nums[idx]:
                count += 1
            else:
                count -= 1
            if count == 0:
                max_index = idx
                count = 1
        return nums[max_index]
