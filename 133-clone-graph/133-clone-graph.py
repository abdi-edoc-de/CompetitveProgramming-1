class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return 
        visited = set()
        graph = {}
        self.dfs(node,visited , graph)
        # self.dfss(graph[node.val],set())
        return graph[node.val]
    def dfs(self, node,visited, graph):
        if node.val not in graph:
            graph[node.val] = Node(node.val)
        for neighbour in node.neighbors:
            if (node.val, neighbour.val) in visited or ( neighbour.val, node.val) in visited :
                continue
            if neighbour.val not in graph:
                graph[neighbour.val] = Node(neighbour.val)
            visited.add((node.val, neighbour.val))
            visited.add(( neighbour.val,node.val))
            self.dfs(neighbour, visited, graph)
            graph[node.val].neighbors.append(graph[neighbour.val])
            graph[neighbour.val].neighbors.append(graph[node.val])    