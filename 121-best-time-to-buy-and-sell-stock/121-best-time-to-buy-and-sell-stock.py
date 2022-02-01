class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = prices[0]
        n = len(prices)
        for i in range(1,n):
            ans = max(ans,prices[i] - mn)
            mn = min(mn,prices[i])
        return ans
        