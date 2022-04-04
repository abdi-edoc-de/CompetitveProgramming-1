class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        more =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for  word in words:
            arr = []
            for char in word:
                ind = ord(char) - ord('a')
                arr.append(more[ind])
            result.add(''.join(arr))
        return len(result)
                