class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        perfects = []
        i = 0
        while i * i <= n:
            perfects.append(i*i)
            i += 1
        check = {n}
        count = 0
        while check:
            count += 1
            temp = set()
            for x in check:
                for y in perfects:
                    if x == y:
                        return count 
                    if x < y:
                        break
                    temp.add(x-y)
            check = temp
            
