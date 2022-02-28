class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [-1] * m , [-1] * n
        for r in range(m):
            for c in range(n):
                rows[r] = max(rows[r], grid[r][c])
                cols[c] = max(cols[c], grid[r][c])
        result = 0
        # print(rows, cols)
        for r in range(m):
            for c in range(n):
                if min(rows[r], cols[c]) - grid[r][c] > 0:
                    result += abs(min(rows[r],cols[c]) - grid[r][c])
        return result  