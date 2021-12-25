class Solution:
    def twoSum(self, nums, target) :
        
        n = {}
        
        for i in range(len(nums)):
            dif = target - nums[i]
            if ( dif in n and n[dif] != i):
                return [n[dif],i]
            n[nums[i]]=i
                        
        