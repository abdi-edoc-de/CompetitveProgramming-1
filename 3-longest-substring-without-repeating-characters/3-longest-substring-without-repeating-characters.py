class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars, left = {}, 0
        result = 0
        for i, char in enumerate(s):
            if char in chars and chars[char] >= left:
                left = chars[char] +1
            chars[char] = i
            result = max(result, i - left + 1)
        return result
            