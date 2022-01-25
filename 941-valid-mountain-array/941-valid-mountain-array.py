class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag , n = False, len(arr)
        
        for i in range(1,n):
            num = arr[i]
            if flag and i > 0 and arr[i-1] <= num:return False

            if 0 < i < n-1 and arr[i-1] < num > arr[i+1]:
                flag = True
                
            if not flag and i > 0 and arr[i-1] >= num: return False
            # print(i, flag,num,arr[i-1]<num> arr[i+1])
        return flag