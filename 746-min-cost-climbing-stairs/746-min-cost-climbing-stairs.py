class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {}
        
        n = len(cost) - 1
        def recur(ind):
            if ind >n :return 0
            if ind in dp:return dp[ind]
            dp[ind] = min(recur(ind+1), recur(ind+2)) + cost[ind]
            return dp[ind]
        zero = recur(0)
        dp = {}
        one = recur(1)
        return min(zero, one)