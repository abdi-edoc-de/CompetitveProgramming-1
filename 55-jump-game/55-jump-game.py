class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = 0
        n = len(nums)
        if n == 1:return True
        for i in range(n):
            if i > maxx: return False
            maxx = max(maxx , i + nums[i])
            if maxx >= n-1:return True
        return False