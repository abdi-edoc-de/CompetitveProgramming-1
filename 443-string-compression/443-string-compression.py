class Solution:
    def compress(self, chars: List[str]) -> int:
        index , right , left = 0 , 0 , 0
        n = len(chars)
        while right < n:
            while right < n and chars[left] == chars[right]:
                right += 1
            chars[index] = chars[left]
            index += 1
            if right - left > 1:
                for i in str(right-left):
                    chars[index] = i
                    index += 1
            left = right 
                
        return index
            