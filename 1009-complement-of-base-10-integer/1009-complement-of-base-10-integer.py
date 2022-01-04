class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ int('1' * len(bin(n).replace("0b", "")) , 2)