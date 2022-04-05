class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        dire = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        cr, cc = click
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
            return board
        m ,n = len(board), len(board[0])
        def isValid(r,c):
            return 0 <= r < m and 0 <= c < n
        def dfs(r,c):
            if board[r][c] != 'E': return
            value = 0
            board[r][c] = 'B'
            for d in dire:
                nr, nc = d[0] + r, d[1] + c
                if isValid(nr, nc) and board[nr][nc] == 'M':
                    value += 1
            if value != 0:
                board[r][c] = str(value)
                return 
            for d in dire:
                nr, nc = r + d[0] , c + d[1]
            
                if isValid(nr, nc):
                    dfs(nr,nc)
        dfs(cr, cc)
        return board
                
            
            
                
        
        return board        
