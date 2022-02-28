# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        ret = TreeNode(-1)
        ret.left = root
        def traverse(root, parent):
            if root:
                traverse(root.left, root)
                traverse(root.right, root)
                if not root.left and not root.right and root.val == target:
                    if parent.left == root:
                        parent.left = None
                    else:
                        parent.right = None
        traverse(root,ret)
        return ret.left
                    