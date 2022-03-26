# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def build(root, path):
            if root:
                if not root.left and not root.right:
                    path.append(f'{root.val}')
                    result.append(''.join(path))
                    path.pop()
                    return
                path.append(f'{root.val}->')
                build(root.left, path)
                build(root.right, path)
                path.pop()
        build(root, [])
        return result