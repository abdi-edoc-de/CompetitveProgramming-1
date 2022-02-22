class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        def binary(arr, key, flag):
            best, left, right = -1, 0 , len(arr)-1
            while left <= right:
                mid = left + (right - left)//2
                if arr[mid] == key and flag:
                       best, right = mid, mid-1
                elif arr[mid] == key and not flag:
                    best , left = mid , mid + 1
                elif arr[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            return best
        lower = binary(nums, target, True)
        if lower == -1:return []
        uper = binary(nums, target, False)
        return [x for x in range(lower, uper+1)]