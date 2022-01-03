class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:return 1
        trust_me = defaultdict(int)
        trust_you = defaultdict(int)
        for a, b in trust:
            trust_me[b] += 1
            trust_you[a] += 1
        for key, value in trust_me.items():
            if value == n-1 and trust_you[key] == 0:return key
        return -1