class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        stack = [points[0]]
        for start, end in points[1:]:
            if start <= stack[-1][1]: 
                stack[-1][1] = min(stack[-1][1] , end)
            else:
                stack.append([start, end])
        return len(stack)