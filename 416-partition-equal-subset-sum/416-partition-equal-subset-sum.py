class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_up = sum(nums)
        if sum_up % 2 != 0 :return False
        return self.canBePartition(0 , nums, sum_up/2, 0,{})
    def canBePartition(self, ind, nums , target, group_sum,dp):
        if group_sum == target: return True
        if ind == len(nums) : return False
        if (ind , group_sum) in dp: return dp[(ind, group_sum)]
        ans = self.canBePartition(ind+1, nums, target, group_sum + nums[ind], dp) or self.canBePartition(ind + 1, nums, target, group_sum, dp)
        dp[(ind, group_sum)] = ans
        return ans  
    
    
        