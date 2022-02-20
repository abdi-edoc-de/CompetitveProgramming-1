class StockPrice:

    def __init__(self):
        self.max = []
        self.min = []
        self.latest = (-(sys.maxsize-1), 0)
        self.log = {}
    def update(self, timestamp: int, price: int) -> None:
        heappush(self.max, (-price, timestamp))
        heappush(self.min, (price, timestamp))
        self.log[timestamp] = price
        # print(timestamp, self.latest)
        if timestamp >= self.latest[0]:
            self.latest = (timestamp, price)

    def current(self) -> int:
        return self.latest[1]

    def maximum(self) -> int:
        while self.max and self.log[self.max[0][1]] != -self.max[0][0]:
            heappop(self.max)
        return -self.max[0][0]

    def minimum(self) -> int:
        while self.min and self.log[self.min[0][1]] != self.min[0][0]:
            heappop(self.min)
        return self.min[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()