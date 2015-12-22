class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        Time complexity is O(n)
        space complexity 2*O(numRows) which is costly
        """
        size = len(s)
        zig_zag = list()
        extra =  numRows-2 if numRows > 2 else 0 #numRows > 2 ? numRows-2 : 0
        for idx in range(numRows):
            zig_zag.append(idx)
        for idy in range(extra,0, -1):
            zig_zag.append(idy)
        #print zig_zag
        final_str = [""]*numRows
        z_len = len(zig_zag)
        count = 0
        idx = 0 
        while True:
            if idx == z_len:
                idx = 0
            if count == size:
                break
            num = zig_zag[idx]
            #print num+1, count, s[count]
            final_str[num] += s[count]
            idx += 1
            count += 1
        return "".join(final_str)
            
            
        