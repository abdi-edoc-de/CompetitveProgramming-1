class WordDictionary:

    def __init__(self):
        self.children = {}
    def addWord(self, word: str) -> None:
        
        n = len(word)
        temp = self.children
        for i in word:
            if i in temp:
                prev = temp
                temp = temp[i][0]
            else:
                temp[i] = [{}, False]
                prev = temp
                temp = temp[i][0]
        prev[i][1] = True
                
            
    def search(self, word: str) -> bool:
        ans = [False]
        self.searchHelper(word, 0, self.children, ans )
        return ans[0]
    def searchHelper(self, word, ind, trie, ans):
        n = len(word)
        if ans[0] == True:
            return 
        if ind == n-1:
            if word[ind] == '.':
                for i in trie:
                    if trie[i][1]:
                        ans[0] = True
                        return
                return 
                    
            elif word[ind] in trie:
                ans[0] = trie[word[ind]][1]
                return
        elif word[ind] == '.':
            for i in trie:
                self.searchHelper(word, ind+1, trie[i][0], ans)
        elif word[ind] in trie:
            self.searchHelper(word,ind+1, trie[word[ind]][0],ans)