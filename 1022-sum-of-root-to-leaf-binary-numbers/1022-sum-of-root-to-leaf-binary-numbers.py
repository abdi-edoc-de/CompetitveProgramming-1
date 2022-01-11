# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def calculate(root, bi):
            if root:
                bi = bi + str(root.val)
                if not root.left and not root.right:
                    return int(bi, 2)
                return calculate(root.left, bi ) + calculate(root.right , bi)
            return 0
        return calculate(root, "0")