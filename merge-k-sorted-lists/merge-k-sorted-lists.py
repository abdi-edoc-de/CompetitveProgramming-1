# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode(sys.maxsize)
        mod = result
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heappush(heap, (node.val,i))
        while heap:
            val, index = heappop(heap)
            mod.next = ListNode(val)
            mod = mod.next
            lists[index] = lists[index].next
            if lists[index]:
                heappush(heap,(lists[index].val, index))
        return result.next