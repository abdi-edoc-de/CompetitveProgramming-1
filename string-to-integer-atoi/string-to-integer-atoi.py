class Solution:
    def myAtoi(self, s: str) -> int:
        reached , sign = False , 1
        tenth = 10
        result = 0
        for i in s:
            if  not reached and i == " ": continue
            if i.isdigit():
                result *= tenth
                result += int(i)
                reached = True
            elif not reached and i== "-":
                reached = True
                sign = -1
            elif not reached and i== "+":
                reached = True
                sign = 1
            else: break
            if sign == -1 and result > 2 ** 31: return -(2**31)
            elif sign == 1 and result > (2**31) -1 : return (2**31)-1
        return sign * result