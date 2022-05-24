class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        result = 0
        count = 0
        stack = [[-1, 0]]
        for p in s:
            if p == '(':
                stack.append([1, 0])
            else:
                if stack[-1][0] == -1:
                    stack = [[-1, 0]]
                else:
                    _, prev = stack.pop()
                    stack[-1][1] += prev+2
                    result = max(result, stack[-1][1])
            # print(stack)
        return result
