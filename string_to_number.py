
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        
        Conditions that are taken care of:
        1. Removing white spaces 
        2. Null Strring -- > return 0
        3. If first number is non-numeric -- > return 0
        4. If any number is non-numeric in between --> break the string
        5. If number is higher than int_max or lesser than int_min return int_max or int_min
        6. check number is positive or negative
        """
        s = str.strip()
        if len(s) == 0:
            return 0
        numerals = range(10)
        final_num = 0
        flag = False
        if s[0] == "-":
            flag = True
            s = s[1:]
        elif s[0] == "+":
            s= s[1:]
        preprocess = ""
        for each_char in s:
            value  = ord(each_char) - ord('0')
            if value in numerals:
                preprocess += each_char
            else:
                if len(preprocess) == 0:
                    return 0
                else:
                    break
        s_len = len(preprocess)
        for each_char in preprocess:
            value  = ord(each_char) - ord('0')
            if value in numerals:
                final_num += value * (10 ** (s_len-1))
                s_len -= 1
        int_max = 2147483647
        int_min = -2147483648
        if final_num > int_max:
            if flag:
                return int_min
            else:
                return int_max
        else:
            return final_num*-1 if flag else final_num
        
    
        