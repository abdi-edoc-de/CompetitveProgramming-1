class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 , node2, carry,result = l1, l2, 0, ListNode(-1)
        temp = result
        while node1 and node2:
            val = node1.val + node2.val + carry
            carry = val //10
            result.next = ListNode(val%10)
            node1 , node2 , result = node1.next , node2.next , result.next
        node = node1 if node1 else node2
        while node:
            val = node.val + carry
            carry = val // 10
            result.next = ListNode(val%10)
            node , result = node.next , result.next
        if carry == 1: result.next = ListNode(carry)
        return temp.next