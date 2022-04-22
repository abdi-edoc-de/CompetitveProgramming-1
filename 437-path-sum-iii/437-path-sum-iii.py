# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixes = []
        count = 0
        def dfs(root,summ):
            if not root: return 
            nonlocal count 
            summ = summ + root.val
            if summ == targetSum: count += 1
            for pref in prefixes:
                if summ - pref == targetSum:
                    count += 1
            prefixes.append(summ)
            dfs(root.left, summ)
            dfs(root.right, summ)
            prefixes.pop()
        dfs(root, 0)
        return count
                