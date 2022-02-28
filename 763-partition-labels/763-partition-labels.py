class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack = []
        for char in s:
            flag = True

            for i in range(len(stack)):
                if char in stack[i]:
                    stack = stack[:i] + [[x for buc in stack[i:] for x in buc]]
                    stack[-1].append(char)
                    flag = False
                    break
            if flag:
                stack.append([char])
        # print(stack)
        return [len(x) for x in stack]
        