# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def get_length(head):
            n = 0
            while head:
                head = head.next
                n += 1
            return n
        a, b = (get_length(headA), headA), (get_length(headB), headB)
        if a[0] > b[0]:
            large, small = a,b
        else:
            large, small = b,a
        dif, large , small = large[0] - small[0], large[1], small[1]
        for _ in range(dif): large = large.next
            
        while small and large:
            if small == large:
                return large
            large, small = large.next, small.next
        
        