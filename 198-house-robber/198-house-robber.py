class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        ret = max(nums)
        
        for i in range(2,n):
            if i == 2:
                nums[i] += nums[0]
            else:
                nums[i] += max(nums[i-2],nums[i-3])
            ret = max(ret,nums[i])
        return ret