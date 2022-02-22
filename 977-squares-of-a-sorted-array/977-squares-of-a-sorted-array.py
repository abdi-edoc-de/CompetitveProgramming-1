class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result, right , left = [], len(nums)-1, 0
        if right == 0:return [nums[0]**2]
        
        while left <= right:
            l, r = nums[left]**2 , nums[right]**2
            # print(nums[left], nums[right], right)
            if r > l:
                result.append(r)
                right -= 1
            else:
                result.append(l)
                left += 1
        return result[::-1]