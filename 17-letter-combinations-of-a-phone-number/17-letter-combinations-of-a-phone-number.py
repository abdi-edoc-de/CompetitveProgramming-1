class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pad = {2:"abc",
              3:"def",
              4:"ghi",
              5:"jkl",
              6:'mno',
              7:"pqrs",
              8:"tuv",
               9:'wxyz'}
        result = []
        def dfs(arr, ind):
            if ind >= len(digits):
                result.append(''.join(arr))
                return
            for char in pad[int(digits[ind])]:
                arr.append(char)
                dfs(arr, ind+1)
                arr.pop()
        dfs([],0)
        return result if len(result) > 1 else []