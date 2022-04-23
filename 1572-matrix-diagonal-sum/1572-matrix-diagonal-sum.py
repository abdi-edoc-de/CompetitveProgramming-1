class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        summ = 0
        for i in range(n):
            summ += (mat[i][i] + mat[i][n-i-1])
        return summ - mat[n//2][n//2] if n % 2 == 1 else summ
    
    