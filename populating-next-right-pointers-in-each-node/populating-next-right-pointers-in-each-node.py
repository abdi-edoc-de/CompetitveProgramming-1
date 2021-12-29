"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        que = deque()
        que.append(root)
        if not root:
            return
        while que:
            cur = que.popleft()
            n = len(que)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)

            for _ in range(n):
                temp = que.popleft()
                cur.next = temp
                cur = temp
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root
                