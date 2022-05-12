class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        result = 0
        nums = defaultdict(int)
        for w, l in  rectangles:
            result += nums[w/l]
            nums[w/l] += 1
        return result