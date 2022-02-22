class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count , visited = Counter(arr), set()
        for item, value in count.items():
            if value in visited: return False
            visited.add(value)
        return True