# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getMid(head):
            if not head or not head.next : return None
            slow, fast , prev = head, head.next, None
            while fast:
                prev = slow
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    fast = fast.next
            prev.next = None
            # print(slow)
            return slow
        def merge(head1, head2):
            ret = ListNode()
            temp = ret
            while head1 and head2:
                if head1.val > head2.val:
                    temp.next = head2
                    temp, head2 = temp.next, head2.next
                else:
                    temp.next = head1
                    temp, head1 = temp.next, head1.next
            temp.next  = head1 if head1 else head2
            return ret.next
        
            
            
        # print(head, "here")
        if not head or not head.next: return head
        mid = getMid(head)
        # print(mid)
        left = self.sortList(head)
        if not mid:return left
        right = self.sortList(mid)
        return merge(left, right)