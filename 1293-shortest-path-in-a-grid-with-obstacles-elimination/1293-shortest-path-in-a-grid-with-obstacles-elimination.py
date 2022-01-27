class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        n , m = len(grid), len(grid[0])
        que = deque()
        que.append((0,0,0,k))
        self.visited = {((0,0,k))}
        # for i in grid:
        #     print(i)
        if n == 1 and m == 1: return 0
        while que:
            row, col, cost , ksum = que.popleft()
            
            for d in directions:
                nr = row + d[0]
                nc = col + d[1]
                if (nr, nc) == (n-1, m-1): return cost+1
                if self.valid(nr, nc, n ,m, ksum, grid):
                    self.visited.add((nr,nc,ksum-grid[nr][nc]))
                    que.append((nr,nc, cost+1, ksum - grid[nr][nc]))
                    grid[nr][nc] = ksum

#         for i in grid:
#             print(i)
                    
        return -1
    def valid(self, row, col, n, m , k, grid):
        return 0 <= row < n and 0 <= col < m and k - grid[row][col] >=0 and (row, col , k) not in self.visited
    