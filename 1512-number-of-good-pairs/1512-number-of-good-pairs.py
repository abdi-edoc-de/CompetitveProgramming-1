class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for key, value in count.items():
            num = value - 1
            result += (num*(num+1))//2
        return result