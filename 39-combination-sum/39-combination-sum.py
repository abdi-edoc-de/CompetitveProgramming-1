sys.setrecursionlimit(2500) 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        visited = set()
        self.findCombinationSums(ret, target, [], candidates)
    
        return ret
    def findCombinationSums(self, ret, target, nums,candidates):
        nums.sort()
        if target == 0 and nums not in ret:
            ret.append(nums)
        elif target > 0:
            for i in candidates:
                self.findCombinationSums(ret,target - i, [i] + nums, candidates)
                
            