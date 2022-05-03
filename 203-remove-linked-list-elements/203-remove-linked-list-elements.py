# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(0)
        temp , ret = head, res
        while temp:
            if temp.val != val:
                ret.next = temp
                ret = ret.next
                temp = temp.next
            else:
                temp = temp.next
        if ret :ret.next = None
        return res.next  