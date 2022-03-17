class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, visited = set() , set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                for k in  range(j+1, n):
                    val = target -( nums[i] + nums[k] + nums[j]) 
                    if val in visited:
                        result.add(tuple(sorted([val, nums[i], nums[k], nums[j]])))
            visited.add(nums[i])
        return result