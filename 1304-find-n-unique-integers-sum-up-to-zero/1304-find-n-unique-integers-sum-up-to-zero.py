class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0] if n % 2 != 0 else []
        ind = 1
        while ind <= n//2:
            result.append(ind)
            result.append(-ind)
            ind += 1
        return result
        