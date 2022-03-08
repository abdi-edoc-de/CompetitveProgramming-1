class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.roots , self.size = {}, {}
        for frm, to in edges:
            self.roots[frm] = frm
            self.roots[to] = to
            self.size[to] = 1
            self.size[frm] = 1
        def root(node):
            root = node
            while root != self.roots[root]:
                root = self.roots[root]
            while root != self.roots[node]:
                next = self.roots[node]
                self.roots[node] = root
                node = next
            return root
        def unify(node1, node2):
            root1, root2 = root(node1), root(node2)
            if root1 == root2: return
            if self.size[root1] > self.size[root2]:
                self.roots[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.roots[root1] = root2
                self.size[root2] += self.size[root1]
        for frm , to in edges:
            if root(frm) == root(to):
                return [frm,to]
            unify(frm,to)
                