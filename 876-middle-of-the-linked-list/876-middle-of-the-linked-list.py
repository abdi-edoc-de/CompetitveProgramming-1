# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        fast, slow = head.next , head

        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
            # prev = slow
            slow = slow.next
        return slow
    
            