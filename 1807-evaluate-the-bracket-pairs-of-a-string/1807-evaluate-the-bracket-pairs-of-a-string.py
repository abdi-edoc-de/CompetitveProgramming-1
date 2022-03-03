class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        key_val = {key:value for key, value in knowledge}
        result, flag, key = [], False, []
        for char in s:
            if char == ')':
                flag = False
                key = ''.join(key)
                if key in key_val:
                    result.append(key_val[key])
                else:
                    result.append('?')
                key = []
                continue
            elif char == '(':
                flag = True
            elif flag:
                key.append(char)
            else:
                result.append(char)
        return ''.join(result)
                