import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        arr = []
        for i in lists:
            temp = i
            while temp is not None:
                heapq.heappush(arr,temp.val)
                temp = temp.next
        ret = ListNode()
        temp = ret
        while len(arr) != 0:
            temp.next = ListNode(heapq.heappop(arr))
            temp = temp.next
            
        return ret.next
