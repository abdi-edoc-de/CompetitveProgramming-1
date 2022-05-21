class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = {}
        hoe = {1:costs[0], 7: costs[1], 30: costs[2]}
        n = len(days)
        def dfs(ind):
            if ind >= n: return 0
            if ind in dp: return dp[ind]
            value = sys.maxsize
            for key, val in hoe.items():
                right = ind
                while right < n and days[right] - days[ind] < key:
                    right += 1
                value = min(value, val+dfs(right))
            dp[ind] = value
            return value
        return dfs(0)