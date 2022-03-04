class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        count = Counter(nums)
        for key, value in count.items():
            heappush(heap, [-value, key])
        result = []
        for _ in range(k):
            _, key = heappop(heap)
            result.append(key)
        return result