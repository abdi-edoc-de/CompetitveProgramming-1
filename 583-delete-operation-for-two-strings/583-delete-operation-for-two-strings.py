class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp, n1, n2 = {}, len(word1), len(word2)
        def dfs(ind1, ind2):
            if ind1 >= n1 or ind2 >= n2:
                return max(n1-ind1, n2-ind2,0)
            if (ind1, ind2) in dp:return dp[(ind1,ind2)]
            if word1[ind1] == word2[ind2]:
                dp[(ind1, ind2)] = dfs(ind1+1,ind2+1)
            else:
                dp[(ind1, ind2)] = min(dfs(ind1+1, ind2) +1 , dfs(ind1, ind2+1)+1)
            return dp[(ind1, ind2)]
        return dfs(0,0)