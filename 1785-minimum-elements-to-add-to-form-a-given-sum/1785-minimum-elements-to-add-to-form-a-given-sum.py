class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs((sum(nums))-goal))//limit + int((abs((sum(nums))-goal)) % limit!=0)