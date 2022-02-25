class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(map(int,version1.split('.'))),list(map(int,version2.split('.')))
        # print(v1, v2)
        n1, n2, ind = len(v1) , len(v2) , 0
        num1, num2 = 0 ,0 
        while ind < n1 or ind < n2:
            # if v1[ind] > v2[ind]:
            #     return 1
            # elif v1[ind] > v2[ind]:
            #     return -1
            # print(num1, num2)
            if ind < n1:
                num1 += v1[ind]
            if ind < n2:
                num2 += v2[ind]
            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
            ind += 1
        return 0