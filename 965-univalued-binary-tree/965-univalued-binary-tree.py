# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        nodes = set()
        def traverse(root):
            if len(nodes) > 1:return 
            if root:
                nodes.add(root.val)
                traverse(root.left)
                traverse(root.right)
                
        traverse(root)
        return len(nodes) == 1
            