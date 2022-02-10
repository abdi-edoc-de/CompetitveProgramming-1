class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        summ ,result = 0, 0
        for num in nums:
            summ += num
            result += count[summ-k]
            count[summ] += 1

        return result
            
            