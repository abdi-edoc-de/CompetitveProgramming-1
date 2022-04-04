class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        n = len(arr)
        ind = 1
        result = []
        while ind <= n:
            index = arr.index(ind)
            i = n - (ind)
            result.append(index+1)
            arr = arr[:index+1][::-1] + arr[index+1:]
            result.append(i+1)
            arr = arr[:i+1][::-1] + arr[i+1:]
            ind += 1
        result.append(n)
        return result
