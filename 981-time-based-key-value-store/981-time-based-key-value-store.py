class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key]: return ""
        def binary(arr, key):
            left, right,best =0 , len(arr)-1  ,-1
            while left <= right:
                mid = left + ((right-left)//2)
                if arr[mid][0] == key:
                    return arr[mid][1]
                elif key > arr[mid][0]:
                    left = mid + 1
                    best = mid
                else:
                    right = mid - 1
                    # best = mid

            return '' if best == -1 else arr[best][1]
        return binary(self.store[key], timestamp)
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)