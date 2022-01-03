class Solution:
    def checkValidString(self, s: str) -> bool:
        stack =  []
        stack_star = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == "*":
                stack_star.append(i)
            else:
                if stack: stack.pop()
                elif stack_star: stack_star.pop()
                else: return False
        while stack:
            if stack_star:
                if stack_star.pop() < stack.pop():
                    return False
            else:
                return False
        return True