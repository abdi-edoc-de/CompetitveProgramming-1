class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [x for x in nums if count[x] == 1 and count[x-1] == 0 and count[x+1] == 0]
    