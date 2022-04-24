class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = defaultdict(list)
        for i, char in enumerate(s):
            dict[char].append(i)
        for i , value in dict.items():
            if len(value) == 1:
                return value.pop()
        return -1
        