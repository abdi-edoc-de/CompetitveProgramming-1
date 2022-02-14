# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret = [True]
        
        
        def isBalanced(root,level):
            if not ret[0]:return level
            if root:
                left = isBalanced(root.left, level +1)
                right = isBalanced(root.right, level +1)
                if abs(left - right) > 1:
                    ret[0] = False
                return max(left, right)
            return level
        isBalanced(root,0)
        return ret[0]