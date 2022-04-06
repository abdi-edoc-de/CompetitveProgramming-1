class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        update , m, n, dire = [], len(board), len(board[0]), [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        def isValid(r,c):
            return 0 <= r < m and 0 <= c < n
        def get_num_value(r,c):
            value = 0
            for d  in dire:
                new_r, new_c  = r + d[0], c + d[1]
                if isValid(new_r, new_c):
                    value += board[new_r][new_c]
            return value
        for r in range(m):
            for c in range(n):
                value = get_num_value(r,c)
                if board[r][c] == 0:
                    if value == 3:
                        update.append([r,c,1])
                else:
                    if value < 2:
                        update.append([r,c,0])
                    elif value > 3:
                        update.append([r,c,0])
        for r,c, val in update:
            board[r][c] = val
        return board