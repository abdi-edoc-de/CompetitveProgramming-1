class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        subsets = []
        if nums == []:
            return [[]]
        self.getSubsets(nums,[],subsets)
        return subsets
    def getSubsets(self, nums , ans, subsets):
        
        if not nums:
            subsets.append(ans)
        else:
            chosen = nums[0]
            leftItems = nums[1:]
            self.getSubsets(leftItems, ans + [chosen] , subsets)
            self.getSubsets(leftItems, ans, subsets)
        