class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        n =len(cost)
        @cache
        def dfs(ind):
            if ind >= n :
                return 0
            dp[ind] = min(dfs(ind+1), dfs(ind+2)) + cost[ind]
            return dp[ind]
    
        return min(dfs(0),dfs(1))
    