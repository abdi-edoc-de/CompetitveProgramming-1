class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * (n)
        if n in (0,1):return 0
        primes[1], primes[0] = False, False
        count = 0
        for i in range(n):
            if primes[i]:
                for j in range(2*i,n, i):
                    primes[j] = False
                count += 1
        return count