class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        def get_perm(perms):
            if len(perms) == len(nums):
                perm.append(perms.copy())
                return 
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    get_perm(perms)
                    perms.pop()
        for num in nums:
            get_perm([num])
        return perm