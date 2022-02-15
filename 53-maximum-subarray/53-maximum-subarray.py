class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        n = len(nums)
        ret = sum
        for i in range(1,n):
            sum = max(sum + nums[i],nums[i])
            ret = max(ret,sum)
        return ret