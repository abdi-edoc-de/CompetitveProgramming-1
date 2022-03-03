# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(root, p , gp):
            if root:
                if gp and gp.val % 2 == 0:
                    self.result += root.val
                dfs(root.left, root,p)
                dfs(root.right,root, p)
        dfs(root, None, None)
        return self.result