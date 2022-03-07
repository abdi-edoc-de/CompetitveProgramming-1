class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.store = defaultdict(list)
        for i, item in enumerate(nums):
            self.store[item].append(i)
        
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        arr = self.store[target]
        left, right = 0, len(arr)-1
        return arr[random.randint(left, right)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)