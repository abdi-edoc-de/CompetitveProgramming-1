# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        def build(parent,root):
            if root:
                if parent:
                    graph[root.val].append((parent.val,'U'))
                if root.left:
                    graph[root.val].append((root.left.val,'L'))
                    build(root, root.left)
                if root.right:
                    graph[root.val].append((root.right.val,"R"))
                    build(root, root.right)
        build(None, root)
        # print(graph)

        que = deque()
        que.append(('', startValue))
        visited = {startValue}
        while que:
            step , node = que.popleft()
            
            for n in graph[node]:
                direction = n[1]
                nei = n[0]
                if nei == destValue:
                    return step + direction
                if nei not in visited:
                    que.append((step + direction , nei))
                    visited.add(nei)
            