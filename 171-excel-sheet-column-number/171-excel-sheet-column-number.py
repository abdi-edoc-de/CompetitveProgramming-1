class Solution:
    def titleToNumber(self, s):
        res = 0
        for c in s:
            res = res*26 + ord(c)-ord('A')+1
        return res
    
    
    
# 26 + 26 * 26 + 26 * 26 * 26 + 1
#26 + 26 * 26 + 26*26*26 + 26*26*26*6 + 6
# 26 + 26 * 25