class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.stack = [homepage]
        self.que = deque()
        
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.stack.append(url)
        self.que = deque()
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        # if len(self.stack) <= steps:return self.stack[-1] 
        for _ in range(steps):
            if len(self.stack) == 1: return self.stack[-1]
            self.que.appendleft(self.stack.pop())
        return self.stack[-1]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        # if len(self.que) <= steps:return self.stack[-1]
        for _ in range(steps):
            if len(self.que) == 0:return self.stack[-1]
            self.stack.append(self.que.popleft())
        return self.stack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)