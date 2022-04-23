class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
    
        n = len(matrix)
        summ = n * (n+1)/2
        def isValid(dire, r, c):
            l_summ , arr= 0 , []
            while r < n and c < n:
                l_summ += matrix[r][c]
                arr.append(matrix[r][c])
                r , c = dire[0] + r , c + dire[1]
            return not (l_summ == summ and len(arr) == len(set(arr)))
        for i in range(n):
            if isValid((0,1) , i,0) or  isValid((1,0), 0, i):
                return False
        return True
        