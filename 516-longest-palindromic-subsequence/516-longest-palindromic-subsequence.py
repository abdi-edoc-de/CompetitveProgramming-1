class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.dfs(0, len(s) - 1 , s, {})
    def dfs(self, left ,right,s,memo):
        if (left, right) in memo: return memo[(left,right)]
        if left > right: return 0
        if left == right : return 1
        if s[left] == s[right]:
            left += 1
            right -= 1
            memo[(left-1,right+1)] = self.dfs(left ,right,s, memo) + 2
            return memo[(left-1, right+1)]
        l = left + 1
        r = right - 1
        memo[(left, right)] = max(self.dfs(l, right, s , memo), self.dfs(left, r, s, memo))
        return memo[(left, right)]
        
    