class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n
    
        def dfs(r,c):
            grid[r][c] = 1
            ret = True
            for d in direction:
                nr = d[0] + r
                nc = d[1] + c
                ret &= isValid(nr,nc)
                if isValid(nr,nc) and grid[nr][nc] == 0:
                    ret &= dfs(nr,nc)
            return ret
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    rc = r
                    cc = c
                    if dfs(r, c):
                        # print(count, r, c, grid[r][c])
                        count += 1
                        # print(count,r,c)
        return count
# [[0,0,1,1,0,1,0,0,1,0],
#  [1,1,0,1,1,0,1,1,1,0],
#  [1,0,1,1,1,0,0,1,1,0],
#  [0,1,1,0,0,0,0,1,0,1],
#  [0,0,0,0,0,0,1,1,1,0],
#  [0,1,0,1,0,1,0,1,1,1],
#  [1,0,1,0,1,1,0,0,0,1],
#  [1,1,1,1,1,1,0,0,0,0],
#  [1,1,1,0,0,1,0,1,0,1],
#  [1,1,1,0,1,1,0,1,1,0]]

# [[0,0,1,1,0,1,0,0,1,0], [1,1,0,1,1,0,1,1,1,0], [1,0,1,1,1,0,0,1,1,0], [0,1,1,0,0,0,0,1,0,1], [0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1], [1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0]]