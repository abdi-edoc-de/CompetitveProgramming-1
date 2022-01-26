# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        num = []
        def getNums(root):
            if root:
                num.append(root.val)
                getNums(root.left)
                getNums(root.right)
        getNums(root1)
        
        
        getNums(root2)
        num.sort()
        return num
