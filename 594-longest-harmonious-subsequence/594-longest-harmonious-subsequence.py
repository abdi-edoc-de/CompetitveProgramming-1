class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for num in nums:
            if count[num+1] != 0:
                result = max(result, count[num]+count[num+1])
        return result