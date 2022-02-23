class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        arr = [[value, -key] for key, value in count.items()]
        arr.sort()
        result = []
        for value, key in arr:
            for _ in range(value):
                result.append(-key)
        return result