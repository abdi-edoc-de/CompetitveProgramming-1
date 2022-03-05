class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnas = set()
        n = len(s)
        hashed = 0
        for i in range(min(10,n)):
            hashed += ord(s[i]) * 10**(9-i)
        dnas.add(hashed)
        result = set()
        for i in range(10,len(s)):
            hashed -= ord(s[i-10]) * 10**9
            hashed *= 10
            hashed += ord(s[i]) * 10**0
            if hashed in dnas:
                result.add(s[i-9:i+1])
            dnas.add(hashed)
        return result
            
            