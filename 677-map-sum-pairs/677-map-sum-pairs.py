class MapSum(object):

    def __init__(self):
        self.trie = {}
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        def delete():
            trie = self.trie
            for char in key:
                trie[char][1][self.keys[key]] -= 1
                trie = trie[char][0]
        if key in self.keys:
            delete()
        trie = self.trie
        for char in key:
            if char in trie:
                trie[char][1][val] += 1
            else:
                trie[char] = [{},defaultdict(int)]
                trie[char][1][val] += 1
            trie = trie[char][0]
        self.keys[key] =val
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        trie, result = self.trie, {}
        for char in prefix:
            if char in trie:
                result = trie[char][1]
                trie = trie[char][0]
            else:
                return 0
        return sum([key * val for key, val in result.items()])
'''
["MapSum","insert","sum","insert","sum"]
[[],["apple",3],["ap"],["app",2],["ap"]]
["MapSum","insert","sum","insert","sum"]
[[],["a",3],["ap"],["b",2],["a"]]
'''


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)