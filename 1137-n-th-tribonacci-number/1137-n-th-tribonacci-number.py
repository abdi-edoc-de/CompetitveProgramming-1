class Solution:
    def tribonacci(self, n: int) -> int:
        a, b , c = 0, 1, 1
        if n == 0:return 0
        for i in range(3,n+1):
            c, b ,a = c + a + b, c, b
        return c