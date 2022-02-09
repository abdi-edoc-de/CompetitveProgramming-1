class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        prev = set()
        visited = set()
        for num in nums:
            if k+num in prev:
                visited.add((num, k+num))
                visited.add((k+num, num))
            if num - k in prev:
                visited.add((num , num-k))
                visited.add((num-k, num))
            # print(visited,prev)
            prev.add(num)
        if k == 0:return len(visited)
        return len(visited)//2