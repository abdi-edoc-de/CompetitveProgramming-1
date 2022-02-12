class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        checkingStartRelation = [True]
        graph = defaultdict(list)
        graph = self.chageToGraph(beginWord, endWord, wordList,graph,checkingStartRelation)
        
        if checkingStartRelation[0]:
            return 0
        if endWord not in wordList:
            return 0
        # print(graph)
        return self.bfs(beginWord, endWord, graph)
    def bfs(self, beginWord, endWord, graph):
        visited = set()
        que = deque()
        
        que.append((0,beginWord))
        visited.add(beginWord) 
        while que:
            cost ,word = que.popleft()
            
            for neighbour in graph[word]:
                if neighbour == endWord:
                    return cost + 2
                if neighbour not in visited:
                    visited.add(neighbour)
                    que.append((cost + 1 , neighbour))
        return 0
            
            
        
        
    def chageToGraph(self,beginWord , endWord, wordList,graph, checkingStartRelation):
        checkList = set(wordList)
        startL = ord('a')
        lastL = ord('z')
        n = len(wordList[0])
        for word in wordList:
            for k in range(n):
                for letter in range(startL,lastL+1):
                    newWord = word[0:k] + chr(letter) + word[k+1:]
                    if newWord != word and newWord in checkList:
                        graph[word].append(newWord)
                        
                        # print(newWord) 
        for k in range(n):
            for letter in range(startL, lastL + 1):
                newWord = beginWord[0:k] + chr(letter) + beginWord[k+1:]
                if newWord != beginWord and newWord in checkList:
                    checkingStartRelation[0] = False
                    graph[beginWord].append(newWord)
                    graph[newWord].append(beginWord)
        return graph
        