#User function Template for python3
from collections import defaultdict
class Solution:
    def sort012(self,arr,n):
        # code here
        ma = defaultdict(int)
        
        for num in arr: 
            ma[num] += 1
        
        ind , num = 0, 0 
        while num <= 2:
            for _ in range(ma[num]):
                arr[ind] = num
                ind += 1
            num += 1
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends