class Solution:
    def isUgly(self, n: int) -> bool:
        dividers = [2,3,5]
        ind = 0
        while ind < 3 and n != 0:
            if n % dividers[ind] != 0:
                ind += 1
            else:
                n /= dividers[ind]
        if n == 1 :return True
        return False