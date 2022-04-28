class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def dfs(perms):
            nonlocal result
            
            if len(perms) == n:
                p = [nums[i] for i in perms]
                if p not in result:
                    result.append(p)
                return
            
            for i in range(n):
                if i not in perms:
                    perms.append(i)
                    dfs(perms)
                    perms.pop()
                
        for i in range(n):
            dfs([i])
        return result