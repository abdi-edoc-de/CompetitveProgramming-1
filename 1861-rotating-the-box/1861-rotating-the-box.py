class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m , n = len(box), len(box[0])
        result = [['.' for x in range(m)] for x  in range(n)]
        # print(result,m,n)
        def shake(r, c, stone, left):
            if stone == 0: return 
            for i in range(c-1, left, -1):
                if stone == 0:return 
                result[i][m-r-1] = '#'
                stone -= 1
            
        
        for r in range(m): 
            left, stone = -1, 0
            
            for c in range(n):
                if box[r][c] == '#':
                    stone += 1
                elif box[r][c] == '*':
                    shake(r, c, stone, left)
                    result[c][m-r-1] = "*"
                    left = c
                    stone = 0
            shake(r, n, stone,left)
        return result


