class SnapshotArray:

    def __init__(self, length: int):
        self.snapid = 0
        self.snaps = defaultdict(defaultdict)
        
        
        
    def set(self, index: int, val: int) -> None:
        self.snaps[self.snapid][index] = val

    def snap(self) -> int:
        self.snapid += 1
        self.snaps[self.snapid] = self.snaps[self.snapid-1].copy() 
        return self.snapid-1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# ["SnapshotArray","snap","snap","get","set","snap","set"]
# [[4],[],[],[3,1],[2,4],[],[1,4]]