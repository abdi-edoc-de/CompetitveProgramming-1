class Solution:
    def rob(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        nums2 = nums2[::-1]
        n = len(nums)
        
        if n < 4:return max(nums)
        nums[2] += nums[0]
        for i in range(3, n-1):
            nums[i] += max(nums[i-3],nums[i-2])
        nums2[2] += nums2[0]
        for i in range(3, n-1):
            nums2[i] += max(nums2[i-3],nums2[i-2])
        return max(max(nums),max(nums2))        