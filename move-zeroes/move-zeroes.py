class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        que = deque()
        for i in range(len(nums)):
            if nums[i] == 0: que.append(i)
            else:
                if que:
                    ind = que.popleft()
                    nums[i] , nums[ind] = nums[ind] , nums[i]
                    que.append(i)
        