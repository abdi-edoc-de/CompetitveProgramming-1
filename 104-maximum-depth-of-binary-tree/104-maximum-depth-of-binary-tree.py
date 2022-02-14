# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 1)
    def dfs(self, root, level):
        depth = 0
        if root:
            if not root.left and not root.right:
                depth = level
            depth = max(depth, self.dfs(root.left, level+1))
            depth = max(depth, self.dfs(root.right, level + 1))
        return depth
        
        