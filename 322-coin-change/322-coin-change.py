class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        dp = {x:1 for x in coins}
        coins = set(coins)
        def dfs(val):
            if val in dp:
                return dp[val]
            value = sys.maxsize
            for c in coins:
                if c <=  val:
                    value = min(value, 1 + dfs(val-c))
            dp[val] = value
            return value
        
        ans = dfs(amount)
        return ans if ans != sys.maxsize else -1
    