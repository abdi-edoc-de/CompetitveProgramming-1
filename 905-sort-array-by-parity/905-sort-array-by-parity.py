class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        que = deque()
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 != 0:
                que.append(i)
            elif que:
                ind = que.popleft()
                nums[ind], nums[i] = nums[i] , nums[ind]
                que.append(i)
        return nums