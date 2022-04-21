# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd = head
        even = head.next
        res_ev = even
        temp = even.next if even else even
        ind = 3
        while temp:
            if ind % 2 == 0:
                even.next, even = temp, temp
            else:
                odd.next , odd = temp, temp
            ind += 1
            temp = temp.next
        odd.next = res_ev
        if even: even.next = None
        return head
            
        
        