class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid[0]), len(grid)
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] == 1
        def dfs(r, c):
            count = 4
            visited.add((r,c))
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                
                if valid(nr, nc):
                    count -= 1
                    if (nr,nc) in visited: continue
                    count += dfs(nr,nc)
            # print(count)
            return count
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return dfs( r, c)