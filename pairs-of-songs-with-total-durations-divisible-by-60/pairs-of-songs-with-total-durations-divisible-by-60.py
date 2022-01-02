class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums = defaultdict(int)
        result = 0
        for t in time:
            left = (t - (60 * (t // 60)))
            if t % 60 == 0:
                result += nums[0]
            else:
                result += nums[60-left]
            nums[left] += 1
        print(nums)
        return result