# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.result = [-1,0]
        def dfs(root, level):
            if root:
                if level > self.result[0]:
                    self.result = [level, root.val]
                elif level == self.result[0]:
                    self.result[1] += root.val
                dfs(root.left,level+1)
                dfs(root.right, level+1)
        dfs(root,0)
        return self.result[1]
        