class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = [[arr[0],arr[1]]]
        mn , n= abs(arr[0] - arr[1]), len(arr)
        for i in range(2,n):
            num = abs(arr[i] - arr[i-1])
            if mn == num:
                result.append([arr[i-1],arr[i]])
            elif mn > num:
                result = [[arr[i-1], arr[i]]]
                mn = abs(arr[i-1]- arr[i])
        return result
    
    
11, 26