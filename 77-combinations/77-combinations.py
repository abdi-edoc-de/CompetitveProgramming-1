class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(combs, ind):
            if len(combs) == k:
                result.append([x for x in combs])
                return 
            for num in range(ind,n+1):
                if num not in combs:
                    combs.append(num)
                    dfs(combs, num)
                    combs.pop()
        for num in range(1,n+1):
            dfs([num], num)
        return result