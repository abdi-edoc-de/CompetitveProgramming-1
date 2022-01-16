class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(list)
        
        for i, num in enumerate(arr):
            graph[num].append(i)
            
        n = len(arr)
        # print(graph)
        def isValid(ind):
            return 0 <= ind < n
        
        que = deque()
        visited = set()
        visited.add(0)
        que.append((0,0))
        direction = [-1,1]
        if n==1:return 0
        while que:
            cost , node = que.popleft()
            num = arr[node]
            while graph[num]:
                ind = graph[num].pop()
                if ind == n-1:return cost + 1
                if ind in visited: continue
                que.append((cost+1, ind))
                visited.add(ind)
            for d in direction:
                n_r = node + d
                if n_r == n-1: return cost +1
                if isValid(n_r) and n_r not in visited:
                    visited.add(n_r)
                    que.append((cost+1, n_r))
            
            
            
        
        
        
        