# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head
        
        ret = head.next
        temp = head
        prev = None
        while temp:
            second = temp.next
            first = temp
            if second:
                next = temp.next.next
                first.next = second.next
                second.next = first
                if prev:
                    prev.next = second
                temp = next
            else:
                break
            prev = first      
        
        return ret