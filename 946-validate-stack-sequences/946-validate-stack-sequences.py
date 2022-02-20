class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        visited = set()
        ind = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[ind]:
                stack.pop()
                ind +=1
        print(stack)
        return stack == []