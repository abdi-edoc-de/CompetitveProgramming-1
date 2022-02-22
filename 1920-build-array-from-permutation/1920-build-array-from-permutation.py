class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        for i in range(q):
            r = nums[i]
            b = nums[nums[i]] % q
            nums[i] = b * q + r
        for i in range(q):
            nums[i] //= q
        return nums