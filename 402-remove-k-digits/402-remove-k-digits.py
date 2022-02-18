class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # print(len(num) , k)
        def deletPreviousZero(arr):
            stack , check  = [],False
            for i in arr:
                if i != '0':
                    check = True
                if check:
                    stack.append(i)
            if stack:return ''.join(stack)
            return '0'
        stack = [num[0]]
        for n in num[1:]:
            while k>0 and stack and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        # print(stack,k)
        for i in range(k): stack.pop()
        return deletPreviousZero(stack)