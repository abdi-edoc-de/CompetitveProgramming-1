# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root, n = TreeNode(31), len(preorder)
        indices = {postorder[i]:i for i in range(n)}
        indices[31] = 31
        self.ind = 0
        def build(root):
            ind = self.ind

            if ind >= n or indices[root.val] < indices[preorder[ind]]: return 

            node = TreeNode(preorder[ind])
            self.ind += 1
            if not root.left:
                root.left = node
                
            elif not root.right:
                root.right = node
            build(node)
            build(node)
        build(root)
        return root.left
            