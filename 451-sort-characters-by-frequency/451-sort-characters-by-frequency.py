class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        result = []
        for key, value in count.most_common():
            result.append(key * value)
        return ''.join(result)
        