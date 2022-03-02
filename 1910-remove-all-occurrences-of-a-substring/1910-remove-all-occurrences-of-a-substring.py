class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        lst_part = list(part)
        for char in s:
            stack.append(char)
            if stack[-len(part):] == lst_part:
                for _ in range(len(part)):
                    stack.pop()
        return ''.join(stack)