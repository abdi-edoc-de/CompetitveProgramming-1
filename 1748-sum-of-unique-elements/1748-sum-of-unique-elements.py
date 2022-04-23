class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum([x for x in nums if count[x] == 1])