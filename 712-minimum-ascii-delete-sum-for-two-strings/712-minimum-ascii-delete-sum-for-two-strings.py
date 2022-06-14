class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def count(s, ind,n):
            result = 0
            for i in range(ind, n):
                result += ord(s[i])
            return result
        dp, n1, n2 = {}, len(s1), len(s2)
        def dfs(ind1, ind2):
            if ind1 >= n1:
                return count(s2, ind2, n2)
            if ind2 >= n2:
                return count(s1, ind1, n1)
            if (ind1, ind2) in dp:return dp[(ind1, ind2)]
            if s1[ind1] == s2[ind2]:
                dp[(ind1, ind2)] = dfs(ind1+1, ind2+1)
            else:
                dp[(ind1, ind2)] = min(dfs(ind1+1, ind2) + ord(s1[ind1]), dfs(ind1, ind2+1)+ord(s2[ind2]))
            return dp[(ind1, ind2)]
        return dfs(0,0)
            
        