class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.capacity = capacity
        self.size = 0
        self.order = 0
        self.heap = []
    def get(self, key: int) -> int:
        if key in self.keys:
            self.order += 1
            self.keys[key][1] = self.order
            self.compress()
            heappush(self.heap , (self.order,key))
            return self.keys[key][0]
        return -1
    def put(self, key: int, value: int) -> None:
        self.order += 1
        self.compress()
        if key not in self.keys:
            if self.size >= self.capacity:
                _,k = heappop(self.heap)
                del self.keys[k]
            else:
                self.size += 1
        self.keys[key] = [value, self.order]
        heappush(self.heap, (self.order, key))
    def compress(self):
        while self.heap and (self.heap[0][1] not in self.keys or ( self.keys[self.heap[0][1]][1] != self.heap[0][0])):
            heappop(self.heap)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)