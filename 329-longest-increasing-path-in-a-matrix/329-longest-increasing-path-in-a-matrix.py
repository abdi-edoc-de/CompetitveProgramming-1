class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        result = 1
        n, m = len(matrix), len(matrix[0])
        def isValid(r,c, row, col):
            return 0 <= r < n and 0 <= c < m and matrix[r][c] < matrix[row][col]
        def dfs(r,c):
            dp[(r,c)] = 1
            for d in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r + d[0], c + d[1]
                if (nr, nc) in dp and isValid(nr,nc, r,c):
                    dp[(r,c)] = max(dp[(nr,nc)] + 1, dp[(r,c)])
                elif isValid(nr, nc, r, c):
                    dp[(r,c)] =max( 1 + dfs(nr,nc), dp[(r,c)])
            return dp[(r,c)]
        
        for r in range(n):
            for c in range(m):
                if (r,c) not in dp:
                    result = max(result, dfs(r,c))
        return result 