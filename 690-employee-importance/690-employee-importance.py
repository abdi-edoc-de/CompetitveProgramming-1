"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {emp.id:emp for emp in employees}
        def traverse(root):
            val = root.importance
            for emp in root.subordinates:
                val +=  traverse(graph[emp])
            return val
        return traverse(graph[id])
        