"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = {}
        # print(node.val, 2, node.neighbors[0].val)
        visited = {}
        def copy(node):
            if not node:return node
            if  node.val not in nodes:
                nodes[node.val] = Node(node.val)
            new_node = nodes[node.val]
            for nei in node.neighbors:
                if nei.val in nodes:
                    new_node.neighbors.append(nodes[nei.val])
                else:
                    new_node.neighbors.append(copy(nei))
            return nodes[node.val]
        return copy(node)