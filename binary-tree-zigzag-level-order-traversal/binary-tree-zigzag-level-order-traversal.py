# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.traverse(root, 0, result)
        flag = False 
        for i in range(len(result)):
            if flag:
                result[i] = result[i][::-1]
            flag = not flag
        return result
    def traverse(self, root, level, result):
        if root:
            if len(result) <= level: result.append([])
            result[level].append(root.val)
            self.traverse(root.left , level + 1, result)
            self.traverse(root.right, level + 1, result)
    