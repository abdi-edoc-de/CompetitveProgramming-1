class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    count += matrix[r][c]
                else:
                    if matrix[r][c] == 0:continue
                    matrix[r][c] += min(matrix[r-1][c],matrix[r][c-1], matrix[r-1][c-1])
                    count += matrix[r][c]
        print(matrix)
        return count