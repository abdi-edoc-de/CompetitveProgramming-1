class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        def isValid(ind, n):
            return 0 <= ind < n
        for i in range(1,rowIndex+1):
            arr = []
            for j in range(i+1):
                if not isValid(j-1, len(result[i-1])) or not isValid(j, len(result[i-1])):
                    arr.append(1)
                else:
                    arr.append(result[i-1][j-1]+result[i-1][j])
            result.append(arr)
        return result[-1]