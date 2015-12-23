class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        This uses o(1) extra space
        It compares the left digit and the right digit of the number
        First it calculates the division numeral from a while loop
        from this the left digit and right digit are found.
        """
        if x < 0:
            return False
        # Find division value
        div = 1
        while x / div >= 10:
            div = div * 10
        while x > 0:
            # find left digit
            left_digit = x/div
            # get right digit
            right_digit = x%10
            # slice the left digit
            x = x - (left_digit*div)
            # slice it
            x = x / 10
            div = div / 100
            if left_digit != right_digit:
                return False
        return True