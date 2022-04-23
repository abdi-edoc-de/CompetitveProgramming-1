class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        summ = sum(nums)
        dif = abs(summ-goal)
        return dif//limit + int(dif % limit!=0)