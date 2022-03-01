import math as m
class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(n+1):
            if i != 0:
                j = log2(i)

            
            if i == 0:
                ret.append(0)
            elif i == 1:
                ret.append(1)
            elif i == 2:
                ret.append(1)
            elif j % 2 == 0:
                ret.append(1)
            else:
                # j = log2(i)
                
                low = i - 2**(ceil(j))
                
                ret.append(1+ret[low])
        return ret
        