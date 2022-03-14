class Solution:
    def sortColors(self, nums):
        max = nums[0]
        for i in nums:
            if i > max:
                max=i
        map={}
        for i in range(max+1):
            map[i]=[]

        for i in nums:
            if i in map:
                map[i].append(i)
            else:
                map[i]=[i]

            
        
        k=0
        for i in map:
            for j in map[i]:
                nums[k]=j
                k+=1
        return nums