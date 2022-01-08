# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         count = 0
#         n = len(grid)
#         m = len(grid[0])
#         direction = [(1,-1),(1,0), (1,1)]
        
#         def isValid(r,c):
#             return 0 <= r < n and 0 <= c < m and grid[r][c] >= 0
#         def bfs(row, col):
            
#             heap = [[grid[row][col], row, col, [[row, col]]]]
            
#             while heap:
#                 cherry , r , c, path = heappop(heap)
                
#                 if r == n - 1: return cherry , path
#                 for d in direction:
#                     nr = r + d[0]
#                     nc = c + d[1]
#                     if isValid(nr,nc):
#                         heappush(heap, [cherry + grid[row][col], nr, nc, path + [[nr,nc]]])
                
            
#         count, path = bfs(0,0)
#         print(path)
#         for r, c in path:
#             grid[r][c] = -1
#         count += bfs(0,m-1)[0]
#         return count
        
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        pos_cherry = {(0,n-1):grid[0][0]+grid[0][-1]}
        for i in range(1,m):
            new = {}
            for (x,y),val in pos_cherry.items():
                robot1 = [i for i in [x-1,x,x+1] if i>=0 and i<n]
                robot2 = [i for i in [y-1,y,y+1] if i>=0 and i<n]
                for a in robot1:
                    for b in robot2:
                        new_val = val + grid[i][a] + grid[i][b] * (a!=b)
                        if (a,b) not in new or new_val > new[(a,b)]:
                            new[(a,b)] = new_val
            pos_cherry = new
        return max(pos_cherry.values())