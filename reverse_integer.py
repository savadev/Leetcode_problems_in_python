class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        This is better then storing the values in the list and multiplying it with the power of 10
        """
        if x == 0:
            return 0
        flag = False
        if x < 0:
            flag = True
            x = x * -1
        reversed = ""
        while x != 0:
            num = x % 10
            x = x / 10
            reversed += str(num)
        if flag :
            reversed = int(reversed)*-1
        else:
            reversed = int(reversed)
        if -2147483647 >= reversed  or reversed >= 2147483647:
            return 0
        else:
            return reversed
            