class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        temp , pre= self.trie, self.trie
        for char in word:
            if char not in temp: 
                temp[char] = [{},False]
            prev, temp = temp, temp[char][0]
        prev[char][1] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        temp , prev= self.trie, self.trie
        for char in word:
            if char not in  temp:
                return False
            prev, temp = temp, temp[char][0]
        return prev[char][1]
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        temp = self.trie
        for char in prefix:
            if char not in temp:
                return False
            temp = temp[char][0]
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)