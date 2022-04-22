# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result, arr = [], []
        def dfs(root, summ):
            if root:
                arr.append(root.val)
                if summ + root.val == targetSum and not root.left and not root.right:
                    result.append(arr.copy())
                dfs(root.left, summ+root.val)
                dfs(root.right, summ+root.val)
                arr.pop()
            
        dfs(root, 0)
        return result
                