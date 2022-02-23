class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0,n-1
        while left <= right:
            mid = left + (right-left)//2
            if mid == 0: 
                return 1
            elif mid == n-1:
                return n-2
            elif arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1