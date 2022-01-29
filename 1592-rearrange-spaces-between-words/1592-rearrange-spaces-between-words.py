class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for i in text:
            if i == ' ':
                spaces+=1
        words = [x.strip() for x in text.split(" ") if x != '']
        n =len(words) 
        if n==1:return words[0] + " " * spaces
        bn_spaces = spaces//(n-1)
        left =spaces- bn_spaces*(n-1)
        result = []
        for i in range(n):
            word = words[i]
            if i == n-1:
                result.append(word)
                result.append(" " * left)
            else:
                result.append(word)
                result.append(" "* bn_spaces)
        return ''.join(result)