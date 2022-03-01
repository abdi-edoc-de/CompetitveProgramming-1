class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        letters = set(s)
        
        for letter in letters:
            left, curr_k = 0, 0
            
            for j in range(len(s)):
                curr_k += s[j] != letter
                while curr_k > k and left <= j:
                    curr_k -= s[left] != letter
                    left += 1
                max_length = max(max_length, j - left + 1)
        
        return max_length
