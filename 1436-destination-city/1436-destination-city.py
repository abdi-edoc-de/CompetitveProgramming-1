class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(list)
        for start , dest in paths:
            graph[start].append(dest)
            graph[dest]
        for city , dests in graph.items():
            if not dests: return city
    
        