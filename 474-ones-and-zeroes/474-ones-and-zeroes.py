class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        @cache
        def dfs(ind, z, o):
            
            if (z == 0 and o == 0) or ind >= len(strs):
                return 0
            zeros = strs[ind].count('0')
            ones = strs[ind].count('1')
            if zeros <= z and ones <= o:
                return max(dfs(ind+1, z-zeros, o-ones)+1, dfs(ind+1, z, o))
            else:
                return  dfs(ind+1, z, o)
        return dfs(0, m, n)
        