class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor < 0) or (divisor > 0 and dividend > 0):
            sign = 1
        else:
            sign = -1
        result, cary = [], "0"
        bit_num = bin(abs(dividend)).replace('0b',"")
        
        for bit in bit_num:
            ream = cary + f'{bit}'
            ream_num = int(ream,2)
            if ream_num >= abs(divisor):
                result.append("1")
                cary = bin(ream_num - abs(divisor)).replace('0b',"")
            else:
                result.append('0')
                cary += f'{bit}'
        value = sign * int(''.join(result),2)
        if value > (2**31) - 1:
            return (2**31) - 1
        elif value < -(2**31):
            return -(2**31)
        return value
    
            
        