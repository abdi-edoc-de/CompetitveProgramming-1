class Solution:
    def findComplement(self, num: int) -> int:
        return num ^int(('1' * len(bin(num).replace('0b',''))),2)