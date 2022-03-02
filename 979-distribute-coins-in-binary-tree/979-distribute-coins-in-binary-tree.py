# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def dfs(root):
            if root:
                l, r = dfs(root.left), dfs(root.right)
                self.result += abs(l) + abs(r)
                return root.val + l + r - 1
            return 0
        dfs(root)
        return self.result