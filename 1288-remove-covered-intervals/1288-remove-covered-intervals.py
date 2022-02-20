class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a:a[1])
        stack = [intervals[0]]
        for start, end in intervals[1:]:
            if stack[-1][0] <= start and stack[-1][1] >= end:
                stack[-1] = [start,end]
            elif start <= stack[-1][0] and end >= stack[-1][1]:
                while stack and start <= stack[-1][0] and end >= stack[-1][1]:
                    stack.pop()
                stack.append([start,end])
            else:
                stack.append([start, end])
        return len(stack)