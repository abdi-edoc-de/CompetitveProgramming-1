class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def rotate(r, ind, n):
            for c in range(ind, n-1):
                temp = matrix[r][c]
                temp, matrix[c][n-1] = matrix[c][n-1], temp
                temp, matrix[n-1][n-c-1+ind] = matrix[n-1][n-c-1+ind], temp
                temp, matrix[n-c-1+ind][ind] = matrix[n-c-1+ind][ind] , temp
                matrix[r][c] = temp
        for i in range(n//2):
            rotate(i,i, n-i)
    