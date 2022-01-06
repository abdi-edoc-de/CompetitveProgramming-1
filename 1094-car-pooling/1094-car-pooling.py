class Solution:
    def carPooling(self, trips, capacity):
        for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
            capacity -= v
            if capacity < 0:
                return False
        return True

#     [[2,1,5],[3,3,7]]
# 4
# [[2,1,5],[3,3,7]]
# 5
# [[2,1,5],[3,5,7]]
# 3
# [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
# 23
# [[1,1,4],[9,4,9],[9,1,9],[2,3,5],[4,1,5],[10,4,5]]
# 33