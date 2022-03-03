class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(open, close, bracket):
            if open == n and close == n:
                result.append(''.join(bracket))
                return 
            if open > close and close < n:
                bracket.append(')')
                dfs(open, close+1, bracket)
                bracket.pop()
            if open < n:
                bracket.append('(')
                dfs(open + 1, close, bracket)
                bracket.pop()
        dfs(0,0,[])
        return result