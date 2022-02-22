class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack , op = [], {'+',"-","*","/"}
        def calculate(num2, num1,op):
            if op == "+":return num1 + num2
            elif op == '-': return num1-num2
            elif op == "*":return num1 * num2
            else:
                if num1 > 0 and num2 > 0 or num1 <0 and num2 < 0:
                    return num1//num2
                else:
                    return math.ceil(num1/num2)
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                stack.append(calculate(stack.pop(), stack.pop(), token))
        return stack.pop()
    