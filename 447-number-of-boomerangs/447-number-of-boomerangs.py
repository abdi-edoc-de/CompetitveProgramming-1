class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        dict = defaultdict(list)
        for x1, y1 in points:
            dist = defaultdict(list)
            for x2, y2 in points:
                if (x1,y1) == (x2,y2): continue
                dist[sqrt((x1-x2)**2 + (y1-y2)**2)].append((x1,x2))
            for _, value in dist.items():
                n = len(value)
                if n >1:
                    count += (n) * (n-1)
        return count