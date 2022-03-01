class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        result = 0
        def isValid(r,c):
            return 0 <= c < n and 0 <= r < m
        for r in range(m):
            for c in range(n):
                if (isValid(r-1,c) and board[r-1][c] == 'X') or (isValid(r,c-1) and board[r][c-1] == 'X'):
                    continue
                result += int(board[r][c]=="X")
        return result