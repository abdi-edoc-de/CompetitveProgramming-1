class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed.sort(reverse=True)
        orgi = []
        count = defaultdict(int)
        for num in changed:
            if count[num*2] > 0:
                count[num*2] -= 1
                orgi.append(num)
            else:
                count[num] += 1
        for i in count:
            if count[i] != 0:return []
        return orgi

    
# 1 , 2, 0, 4, 5, 0 ,0

# 0 0 0 1 2 4 5

# 0:3
# 1:1
# 2:1
# 4:1
# 5:1