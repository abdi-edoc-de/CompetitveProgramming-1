class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            num = nums[i]
            while num-1 != i and num != nums[num-1]:
                nums[i], nums[num-1] = nums[num-1], nums[i]
                num = nums[i]

        result = []
        for i in range(len(nums)):
            if nums[i]-1 != i:
                result.append(nums[i])
        return result
        
                
