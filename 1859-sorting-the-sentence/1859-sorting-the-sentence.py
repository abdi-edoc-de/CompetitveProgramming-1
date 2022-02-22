class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        n = len(words)
        result = [0] * n
        # print(words)
        for i in range(n):
            # print(words[i], words[i][-1])
            result[int(words[i][-1])-1] = words[i][:len(words[i])-1]
        return ' '.join(result)