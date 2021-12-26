class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        for i in s:
            if i == " ":continue
            if i == '-' and not arr:
                arr.append("0")
                arr.append('-')
            elif i.isdigit():
                if arr and arr[-1].isdigit():
                    arr[-1] += i
                else:
                    arr.append(i)                
            else:
                arr.append(i)
        # print(arr)
        stack = []
        for i in arr:
            if i == '-' and (not stack or not str(stack[-1])[-1].isnumeric()):
                stack.append(0); stack.append("-")
            elif i.isnumeric():
                if stack and stack[-1] in ["-", "+"]:
                    stack.append(self.cal(stack.pop(),stack.pop(),int(i)))
                else:
                    stack.append(int(i))
            elif i in ["-", "+"]:
                stack.append(i)
            elif i == ')':
                val = stack.pop(); stack.pop()
                if stack and stack[-1] in ["-", "+"]:
                    stack.append(self.cal(stack.pop(),stack.pop(),val))
                else:
                    stack.append(val)
            else:
                stack.append(i)
            # print(stack)
        # print('-2'.isnumeric())
        return int(stack.pop())
    def cal(self, op, oper1, oper2):
        if op == '-': return oper1 - oper2
        else: return oper1 + oper2
        
        