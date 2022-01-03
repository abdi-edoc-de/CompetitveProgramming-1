class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        stack =  []
        for i in s:
            if i == "(":
                open += 1
            elif i == ")":
                if open > 0: open -= 1
                else: continue
            stack.append(i)
        result = []
        while stack:
            poped = stack.pop()
            if poped == '(' and open > 0:
                open -= 1
                continue
            result.append(poped)
        return "".join(result[::-1])