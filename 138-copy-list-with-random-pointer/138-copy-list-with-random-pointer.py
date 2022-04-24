"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        adjusent = {}
        temp = head
        while temp:
            adjusent[temp] = Node(temp.val)
            temp = temp.next
        for old, new in adjusent.items():
            if old.next:new.next = adjusent[old.next]
            if old.random:new.random = adjusent[old.random]
        return adjusent[head] if head else None