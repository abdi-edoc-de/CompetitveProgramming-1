# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        result = set()
        to_delete = set(to_delete)
        result.add(root)
        def dfs(root, parent):
            if root:
                if root.val in to_delete:
                    if root in result:
                        result.remove(root)
                    if root.left:
                        result.add(root.left)
                    if root.right:
                        result.add(root.right)
                    if parent:
                        if parent.left == root:
                            parent.left =None
                        else:
                            parent.right = None
                dfs(root.left, root)
                dfs(root.right, root)
        dfs(root,None)
        return list(result)
                        