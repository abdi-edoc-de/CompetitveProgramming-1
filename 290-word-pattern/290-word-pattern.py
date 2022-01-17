class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):return False
        word = defaultdict(list)
        patt = defaultdict(list)
        for i in range(len(words)):
            word[words[i]].append(i)
            patt[pattern[i]].append(i)
        for i in range(len(word)):
            if word[words[i]] != patt[pattern[i]]:return False
        return True
        