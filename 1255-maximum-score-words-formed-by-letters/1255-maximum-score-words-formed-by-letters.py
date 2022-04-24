class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        dp , count, n = {}, Counter(letters), len(words)
        def possible(ind):
            cnt = Counter(words[ind])
            for i in cnt:
                if count[i] < cnt[i]:
                    return False
            return True
        def getValue(ind, flag):
            value = 0
            for char in words[ind]:
                value += score[ord(char)-ord('a')]
                count[char] += flag * 1
            return value
        
        def dfs(ind):
            if ind >= n:
                return 0
            if possible(ind):
                v = getValue(ind, -1) + dfs(ind+1)
                getValue(ind, 1)
                return max(v, dfs(ind+1))
            return dfs(ind+1)
        return dfs(0)