class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [[0,0,0] for _ in range(10) ]
        count = 0
        values = {"B":1,"R":0,"G":2}
        for i in range(len(rings)):
            if rings[i].isdigit(): 
                continue
            rods[int(rings[i+1])][values[rings[i]]] = 1
        for i in rods:
            count += sum(i)//3
        return count