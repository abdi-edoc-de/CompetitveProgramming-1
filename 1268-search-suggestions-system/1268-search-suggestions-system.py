class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = {}
        result = []
        def insert(word):
            temp = trie
            for char in word:
                if char in temp:
                    temp[char][1].add(word)
                else:
                    temp[char] = [{},{word}]
                temp = temp[char][0]
        
        def search(word):
            temp = trie
            for char in word:
                if char in temp:
                    result.append(sorted(list(temp[char][1]))[:3])
                    temp = temp[char][0]
                else:
                    temp = {}
                    result.append([])
                    
        for word in products:
            insert(word)
        search(searchWord)
        return result
        