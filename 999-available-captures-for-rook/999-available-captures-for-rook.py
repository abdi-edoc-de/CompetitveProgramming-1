class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def possiblePawn(r,c, d):
            
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'p':
                    return 1
                elif board[r][c] == 'B':
                    return 0
                r, c = r + d[0], c + d[1]
            return 0
            
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    print(r,c)
                    return possiblePawn(r,c,(1,0)) + possiblePawn(r,c,(0,1)) + possiblePawn(r,c,(-1,0)) + possiblePawn(r,c,(0,-1))
            