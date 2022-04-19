class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque()
        visited = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        n, m = len(mat), len(mat[0])
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    que.append((0,r,c))
                    visited.add((r,c))
        def isValid(r,c):
            return 0  <= r < n and 0 <= c < m and (r,c) not in visited
        while que:
            cost, r, c = que.popleft()
            mat[r][c] = cost
            for d in direction:
                nr, nc = r + d[0] , c + d[1]
                if isValid(nr,nc):
                    que.append((cost + 1, nr, nc))
                    visited.add((nr,nc))
        return mat