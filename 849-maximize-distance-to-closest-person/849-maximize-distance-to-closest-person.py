class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        seat_map = [0] * n
        ma = 0
        flag = True
        for i, num in enumerate(seats):
            if num == 0:
                if i == 0: seat_map[0] = 1
                else: seat_map[i] = seat_map[i-1] + 1
            else: flag = False
            if flag: ma = max(ma,i+1)
        flag = True
        # print(seat_map)
        for i in range(n-1, -1, -1):
            num = seats[i]
            if num == 0:
                if i == n-1: seat_map[i] = 1
                else: seat_map[i] = min(seat_map[i+1]+1,seat_map[i]) 
            else: flag = False
            if flag: ma = max(ma , n-i)
        # print(seat_map)
        # print(ma)
        return max(ma, max(seat_map))