class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)
        best = 0
        while left <= right:
            mid = left+ (right-left)//2
            cap, res = 0, 1
            for wt in weights:
                cap += wt
                if cap > mid:
                    cap = wt
                    res +=1
            if res > days:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
        return best