class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        arr = [[nums[0],1]]
        for i in range(1,n):
            if arr[-1][0] == nums[i]:
                arr[-1][1] += 1    
            else:
                arr.append([nums[i], 1])
        ret, n = arr[0][0] * arr[0][1], len(arr)
        arr[0].append(arr[0][0] * arr[0][1])
        # print(arr)
        for i in range(1,n):
            num, freq = arr[i]
            # print(arr[i-1])
            prev, prevf, _ = arr[i-1]
            
            # print(num, prev)
            if num - prev == 1:
                if i >= 3:
                    arr[i].append( arr[i][0] * arr[i][1] + max(arr[i-2][2], arr[i-3][2]) )
                elif i == 2:
                    arr[i].append(arr[i][0] * arr[i][1] + arr[i-2][2])
                else:
                    arr[i].append( arr[i][0] * arr[i][1] )
            else:
                if i >= 3:
                    arr[i].append( arr[i][0] * arr[i][1] + max(arr[i-2][2], arr[i-3][2], arr[i-1][2])) 
                elif i == 2:
                    arr[i].append(arr[i][0] * arr[i][1] + max(arr[i-2][2], arr[i-1][2]))
                else:
                    arr[i].append(arr[i][0] * arr[i][1] + arr[i-1][2])
            ret = max(ret , arr[i][2])
        # print(arr)
        return ret

                
        