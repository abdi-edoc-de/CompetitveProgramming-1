class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def isPeak(ind):
            for i in [-1,1]:
                if 0 <= ind + i < n and nums[ind] < nums[ind+i]:
                    return False
            return True
        left , right = 0, n-1    
        while left <= right:
            mid = left + (right-left)//2
            if isPeak(mid):
                return mid
            elif nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
