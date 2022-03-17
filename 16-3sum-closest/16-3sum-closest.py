class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = (sys.maxsize, -1)
        
        def binarySearch(left, target):
            right = n - 1
            best = -1
            prev , cur= (sys.maxsize, sys.maxsize), (sys.maxsize, sys.maxsize)
            while left <= right:
                mid = left + (right - left)//2
                best , prev= mid, cur
                cur = (abs(nums[mid] - target), nums[mid])
                if prev < cur:
                    return prev[1]
                if nums[mid] == target:
                    return nums[mid]
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return nums[best]
        for i in range(n):
            for j in range(i+1,n-1):
                k = binarySearch(j+1, target - nums[i] - nums[j])
                val = k + nums[i] + nums[j]
                result = min(result, (abs(val - target) , val))
        return result[1]
    
    '''
[-1,2,1,-4]
1
[0,0,0]
1
[1,2,5,10,11]
12
    '''