class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        # if n==2:return 1
        def dfs(n, k):
            if n == 1 or n == 0 : 
                return 1
            if n in dp: return dp[n]
            mx = 0
            limit = 0 if k < 2 else 1
            for i in range(1,n+limit):
                mx = max(mx, i * dfs(n-i, k+1))
            dp[n] = mx
            return mx
        return dfs(n, 0)