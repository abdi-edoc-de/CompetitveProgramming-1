class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size,count = len(flowerbed), 0
        for i in range(size):
            count += int(self.isValidPlots(flowerbed, i))
            if count >= n:return True
        return False
    def isValidPlots(self, nums, ind):
        count = nums[ind]
        for d in [-1, 1]:
            new_ind = ind + d
            if 0 <= new_ind < len(nums):
                count += nums[new_ind]
        if count == 0:nums[ind] =1
        return count == 0 