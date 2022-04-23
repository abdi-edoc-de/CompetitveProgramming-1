class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        result = 0
        visited = set()
        n ,m = len(mentors) , len(mentors[0])
        def getValue(ment):
            value = 0
            for i in range(n):
                for j in range(m):
                    value += int(ment[i][j] == students[i][j])
            return value
        
        def permtuation(ment:List[List[int]]):
            nonlocal result
            if len(ment) == n:
                result = max(result, getValue(ment))
                return
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    ment.append(mentors[i])
                    permtuation(ment)
                    ment.pop()
                    visited.remove(i)   
        
        for i in range(n):
            visited.add(i)
            permtuation([mentors[i]])
            visited.remove(i)
            
        return result