class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        result = 0
        while left < right:
            result = max(result, min(height[left], height[right]) * (right-left))
            if min(height[left], height[right]) == height[left]:
                left += 1
            else:
                 right -= 1
        return result
        
                