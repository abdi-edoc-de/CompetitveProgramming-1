class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        
        for i in range(26):
            left, curr_k = 0, 0
            letter = chr(ord("A") + i)
            
            for j in range(len(s)):
                curr_k += s[j] != letter
                while curr_k > k and left <= j:
                    curr_k -= s[left] != letter
                    left += 1
                max_length = max(max_length, j - left + 1)
        
        return max_length
