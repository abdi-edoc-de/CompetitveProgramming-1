class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:return 1
        n = len(nums)
        indmn,indmx = nums.index(min(nums)) , nums.index(max(nums))
        ind1, ind2 = min(indmn,indmx), max(indmn, indmx)
        return min(
                ind1+1+n-ind2,
                ind1+1+(ind2-ind1),
                n-ind2 + (ind2-ind1)
                
        )
        
            
'''
[2,10,7,5,4,1,8,6]
[0,-4,19,1,8,-2,-3,5]
[101]
[-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]
[61,21,56,58,-92,63,-8]
[0,-4,19,1,8,-2,-3,5,-5,20,3,4]
'''