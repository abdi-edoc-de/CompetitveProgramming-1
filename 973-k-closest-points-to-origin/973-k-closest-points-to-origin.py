class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def get__distance(x,y):
            return math.sqrt(x**2 + y**2)
        self.heap = []
        for x , y in points:
            heappush(self.heap, (get__distance(x, y), x, y))
        result = []
        for _ in range(k):
            _, x, y = heappop(self.heap)
            result.append([x,y])
        return result