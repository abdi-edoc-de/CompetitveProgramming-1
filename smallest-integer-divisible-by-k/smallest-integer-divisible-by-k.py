class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        st = 1
        for i in range(1,k+1):
            st =(st *  10 ) + 1
            if st % k == 0:
                return len(str(st))
        return -1
        
            
