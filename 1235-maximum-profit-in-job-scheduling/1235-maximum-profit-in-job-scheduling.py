class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n= len(profit)
        nums = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        nums.sort()
        def findNext(start, target):
            left , right = start+1, n-1
            next = -1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid][0] >= target:
                    next = mid
                    right = mid - 1
                else:
                    left = mid +1
            return next
        dp = {}
        def dfs(postion):
            if postion == n or postion == -1: return 0
            if postion in dp: return dp[postion]
            next = findNext(postion, nums[postion][1])
            dp[postion] = max(dfs(postion+1),dfs(next) + nums[postion][2])
            return dp[postion]
        return dfs(0)