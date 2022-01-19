# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes , temp , ind= {}, head, 0
        while temp:
            if temp in nodes:return temp
            nodes[temp]=ind
            ind += 1
            temp = temp.next
        return 
            