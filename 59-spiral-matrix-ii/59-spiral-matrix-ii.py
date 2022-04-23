class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        val = 1
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        grid = [[0 for _ in range(n)] for _ in range(n)]
        
        def make(r,c, lower, higher):
            nonlocal grid, val
            ind = 0
            origin = (r, c)
            while ind < 4:
                while lower <= r < higher and lower <= c < higher:
                    grid[r][c] = val
                    val += 1
                    r,c = r + dir[ind][0], c + dir[ind][1]
                    if (r,c) == origin:return
                r , c = r - dir[ind][0], c - dir[ind][1]
                ind += 1
                if ind == 4: return 
                r,c = r + dir[ind][0], c + dir[ind][1]
                if (r,c) == origin:return

                        
        
        for i in range((n//2)+1):
            make(i,i,i,n-i)
        return grid

[[1, 2, 3, 4, 5, 6],
 [20,21,22,23,24,7],
 [19,32,33,34,25,8],
 [18,31,36,35,26,9],
 [17,30,29,28,27,10],
 [16,15,14,13,12,11]]