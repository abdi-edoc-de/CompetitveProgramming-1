class Solution:
    def fib(self, n: int) -> int:
        if n== 0:return 0
        left, right = 0, 1
        for num in range(2,n+1):
            left , right = right , left + right
        return right 
