class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        dp = {}
        self.helper(s, ret, [],dp)
        return ret
    
    
    def helper(self, st, ret, cur,dp):
        n = len(st)
        if n == 0:
            ret.append(cur)
        elif n == 1:
            cur += [st]
            ret.append(cur)
        else:
            for i in range(0,n+1):
                if self.isPalindrom(st[:i],dp):
                    self.helper(st[i:],ret, cur + [st[:i]],dp)
        
                    
    def isPalindrom(self, st,dp):
        n = len(st)    
        if st in dp:
            return dp[st]
        if n == 0:
            return False
        for i in range(n):
            if st[i] != st[n-i-1]:
                dp[st] = False
                return False
        dp[st] = True
        return True
                    
# "aabaaca"