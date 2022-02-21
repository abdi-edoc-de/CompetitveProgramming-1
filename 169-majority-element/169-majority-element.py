class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        for num in nums:
            # print(maj)
            if maj:
                if maj[0] != num:
                    maj = [maj[0],maj[1]-1]
                    if maj[1] == 0: maj = None
                else:
                    maj[1] += 1
            else:
                maj  = [num, 1]
        return maj[0]