# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return max( self.dfs(root.left,root.val,root.val), self.dfs(root.right, root.val, root.val))

    def dfs(self, root, max_val, min_val):
        max_ans = -sys.maxsize - 1
        if root:
            max_ans = max(max_ans, abs(max_val - root.val), abs(min_val - root.val))
            max_val = max(max_val,root.val)
            min_val = min(min_val, root.val)
            max_ans = max(max_ans, self.dfs(root.left, max_val,min_val), self.dfs(root.right,max_val,min_val))
        return max_ans
            
        