class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        jug1, jug2 = jug1Capacity, jug2Capacity
        if jug1Capacity + jug2Capacity == targetCapacity:return True
        que, visited = deque([(0,0), (jug1,0), (0,jug2), (jug1, jug2)]), {(0,0), (jug1,0), (0,jug2), (jug1, jug2)}        
        def add(f, s):
            if (f,s) in visited:return 
            que.append((f,s))
            visited.add((f,s))
        while que:
            first , second = que.popleft()
            if first == targetCapacity or second == targetCapacity or first + second == targetCapacity:
                return True
            mn = min(jug1-first,second)
            add( first + mn, second - mn )
            mn = min(jug2-second, first)
            add(first - mn, second+mn)
            add(jug1, second)
            add(first, jug2)
            add(0,second)
            add(first, 0)
        return False
            
            