class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
            