class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        result = [[1]]
        def get_value(row, col):
            if 0 <= col < len(result[row]):
                return result[row][col]
            else:
                return 0
        
        for i in range(2, numRows+1):
            cur = []
            for j in range(i):
                cur.append(get_value(i-2, j) +get_value(i-2, j-1) )
            result.append(cur)
        return result
            

        
[[1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]]