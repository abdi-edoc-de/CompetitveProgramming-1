class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        low = nums[0]
        for i in range(n):
            nums[i] = [nums[i], low]
            low = min(low,nums[i][0])
        low = sys.maxsize
        for i in range(n):
            if low < nums[i][0]:
                return True
            if nums[i][1] < nums[i][0]:
                low = min(nums[i][0], low)
        return False
            