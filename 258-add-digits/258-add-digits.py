class Solution:
    def addDigits(self, num: int) -> int:
        result = int(sum([int(x) for x in str(num)]))
        result = int(sum([int(x) for x in str(result)]))
        if len(str(result)) > 1 :
            result = int(sum([int(x) for x in str(result)]))
    
        return result