class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        heap = [-value for value in count.values()]
        heapify(heap)
        result =0
        val = -heap[0]
        while heap:
            poped = -heappop(heap)
            if val==0:
                result += poped
            elif poped > val:
                result += poped - val
                val -= 1
            else:
                val = poped - 1
            
        return result
'''
"aab"
"aaabbbcc"
"ceabaacb"
"abcdefjlop"
'''