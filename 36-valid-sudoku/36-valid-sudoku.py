class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isUniqueRC(dire, r, c):
            arr = []
            while r < 9 and c < 9:
                if board[r][c] != '.':
                    arr.append(board[r][c])
                r , c = r + dire[0], c + dire[1]
            return len(arr) == len(set(arr))
        def isUnique33(row,col):
            arr = []
            for r in range(row,row+3):
                for c in range(col, col+3):
                    if board[r][c] != '.':
                        arr.append(board[r][c])
            return len(arr) == len(set(arr))
        for i in range(9):
            ans = True
            ans &= isUniqueRC((0,1), i, 0)
            ans &= isUniqueRC((1,0), 0, i)
            if i % 3 == 0:
                for r in [0,3,6]:
                    ans &= isUnique33(r,i)
            if not ans: return ans
        return True
        