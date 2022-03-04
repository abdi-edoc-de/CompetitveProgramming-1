class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, result = [],[]
        for i,char in enumerate(s):
            if char == '(':
                stack.append(len(result))
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    continue
            result.append(char)
        while stack:
            poped = stack.pop()
            result[poped] = ''
        return ''.join(x for x in result if x != '')
        