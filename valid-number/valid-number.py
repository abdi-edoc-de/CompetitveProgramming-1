class Solution:
    def isNumber(self, s: str) -> bool:
        dot, digit , e = False, False, False
        n = len(s)
        for i, c in enumerate(s):
            if c.isdigit():
                digit = True
            elif c in ["+", "-"]:
                if i==n-1 or ( i != 0 and (s[i-1] not in ["e", 'E'] or not s[i+1].isdigit())):
                    return False
            elif c in ['e', "E"]:
                if not digit or i == n-1 or e:
                    return False
                e = True
                digit = False
            elif c == '.':
                if dot or e:return False
                dot = True
            else:
                return False
        return digit