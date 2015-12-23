class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        Find the division of the number in form of 10's
        Then count the number of digits
        Get the left digit and slice it from the number
        For the left digit, identify the roman numeral
        """
        # Find the division of the given input number
        div = 1
        final_str = ""
        count = 0 
        while num/div >= 10:
            count += 1
            div = div*10
        while num > 0:
            # Get the left digit of the number
            left_digit = num/div
            left_value = left_digit*div
            # Slice the left digit
            num = num - left_value
            div = div/10
            #print "count is", count, "left digit", left_digit
            # Now check if the left digit falls in which category
            if count == 0:
                # Then the roman numerals are either I or V
                if left_digit == 4:
                    final_str += "IV"
                elif left_digit == 9:
                    final_str += "IX"
                else:
                    while left_digit > 0:
                        if left_digit >= 5:
                            final_str += "V"
                            left_digit -= 5
                        else:
                            final_str += "I"
                            left_digit -= 1
            elif count == 1:
                # Then the roman numerals are either X or L
                if left_digit == 4:
                    final_str += "XL"
                elif left_digit == 9:
                    final_str += "XC"
                else:
                    while left_digit > 0:
                        if left_digit >= 5:
                            final_str += "L"
                            left_digit -= 5
                        else:
                            final_str += "X"
                            left_digit -= 1
            elif count == 2:
                # Then the roman numerals ar either C or D
                # Special previlige for 4 and 9
                if left_digit == 4:
                    final_str += "CD"
                elif left_digit == 9:
                    final_str += "CM"
                else:
                    while left_digit > 0:
                        if left_digit >= 5:
                            final_str += "D"
                            left_digit -= 5
                        else:
                            final_str += "C"
                            left_digit -= 1
            else:
                # Then the roman numeral is M
                while left_digit > 0:
                    final_str += "M"
                    left_digit -= 1
            count -= 1
                
        return final_str                
                
                
                
                