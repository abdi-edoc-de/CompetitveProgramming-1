class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n
        for r in range(1,m):
            for c in range(1,n):
                if isValid(r,c) and matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True


