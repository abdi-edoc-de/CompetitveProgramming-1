# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_length(node):
            n = 0
            while node:
                n += 1
                node = node.next
            return n
        def get_dumy_nodes(n):
            start = TreeNode(0)
            end = start
            for _ in range(n-1):
                end.next = TreeNode(0)
                end = end.next
            return start,end
        n1, n2 = get_length(l1), get_length(l2)
        if n1 > n2:
            start, end = get_dumy_nodes(n1-n2)
            l2, end.next= start, l2
        elif n2 > n1:
            start, end = get_dumy_nodes(n2-n1)
            l1, end.next= start, l1
        l1, l2 = ListNode(0,l1), ListNode(0, l2)  
        def summ(l1, l2):
            if not l1 or not l2: return 0
            val = l1.val + l2.val
            val += summ(l1.next, l2.next)
            l1.val = val % 10
            return val // 10
        summ(l1,l2)
        return l1.next if l1.val == 0 else l1
    
        
        
        