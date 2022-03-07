class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result , l = 0, 0
        indZero = deque()
        for r in range(len(nums)):
            if nums[r] == 0:
                if k == 0:
                    if indZero:
                        l = indZero.popleft() + 1
                        indZero.append(r)
                    else:
                        l =  r + 1
                else:
                    k -= 1
                    indZero.append(r)
            result = max(result,r - l + 1)
        return result