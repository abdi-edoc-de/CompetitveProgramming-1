class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}
        num = n
        while num != 1:
            num = sum([int(x)**2 for x in str(num)])
            if num in visited:return False
            visited.add(num)
        return True
    