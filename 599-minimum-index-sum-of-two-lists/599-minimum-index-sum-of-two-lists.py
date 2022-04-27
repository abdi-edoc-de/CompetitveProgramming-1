class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        ind1 , ind2 = {list1[i]:i for i in range(len(list1))}, {list2[i]:i for i in range(len(list2))}
        
        heap = []
        for key, value in ind1.items():
            if key in ind2:
                heappush(heap, (value + ind2[key], key))
        ans = heap[0][0]
        result = []
        while heap and heap[0][0] == ans:
            result.append(heappop(heap)[1])
        return result
            
            
        