class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dfs({}, n)
    def dfs(self, memo, n):
        if n in memo: return memo[n]
        if n == 0: return 1
        if n < 0 : return 0
        memo[n] = self.dfs(memo, n-1) + self.dfs(memo, n-2)
        return memo[n]
    
        
        
        
        