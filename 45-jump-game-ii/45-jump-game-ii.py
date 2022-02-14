class Solution:
    def jump(self, nums: List[int]) -> int:
        heap = [(0,0)]
        maxx = 0
        n = len(nums)
        if n == 1: return 0
        while heap:
            step , index = heappop(heap)
            for i in range(maxx, index + nums[index]+1):
                if i >= n - 1: return step + 1
                heappush(heap, (step+1, i))
            maxx = max(maxx, index + nums[index]+1)
        
            
            