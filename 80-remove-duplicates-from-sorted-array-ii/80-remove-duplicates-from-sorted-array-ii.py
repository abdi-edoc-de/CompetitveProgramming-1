class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 :return 0
        ind = 1
        flag = True
        for i in range(1,n):
            if nums[i] != nums[ind-1]:
                nums[i] , nums[ind] = nums[ind], nums[i]
                flag = True
                ind += 1
            elif nums[i] == nums[ind-1] and flag:
                nums[i] , nums[ind] = nums[ind], nums[i]
                flag = False
                ind += 1
        return ind

                