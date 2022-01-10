class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_n = len(a)
        b_n = len(b)
        ma = max(a_n, b_n)
        a , b = ('0' * (ma - a_n) )+ a, ('0' * (ma - b_n) )+ b
        carry = 0
        result = []
        for i in range(ma-1, -1, -1):
            carry = carry + int(a[i]) + int(b[i])
            if carry == 1 or carry == 3:
                result.append('1')
            else:
                result.append('0')
            carry //= 2
        if carry == 1:result.append('1')
        return ''.join(result[::-1])
        