class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for i in range(len(strs[0])):
            
            for j in range(1, len(strs)):
                word = strs[j]
                if i >= len(word) or strs[0][i] != word[i]:
                    return ''.join(result)
            
            result.append(strs[0][i])
        return ''.join(result)