class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(node, path):
            if node == len(graph) - 1:
                result.append(path.copy())
                return 
            for nei in graph[node]:
                if nei not in path:
                    path.append(nei)
                    dfs(nei,path)
                    path.pop()
        dfs(0,[0])
        return result