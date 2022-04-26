class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls , cows , secret, guess = 0 , 0,[x for x in secret], [x for x in guess]
        for i in range(len(guess)):
            # print(secret[i], guess[i])
            if secret[i] == guess[i]:
                bulls += 1
                secret[i], guess[i] = -1, -1
        count_s, count_g = Counter(secret), Counter(guess)
        for key, value in count_g.items():
            if key != -1 and key in count_s:
                cows += min(value, count_s[key])
        return f'{bulls}A{cows}B'
        
            