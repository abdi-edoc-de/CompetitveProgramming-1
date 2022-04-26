class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = defaultdict(list)
        self.userPost = defaultdict(list)
        self.stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].add(userId)
        self.stamp -= 1
        self.userPost[userId].append((self.stamp, tweetId,userId))
        for id in self.users[userId]:
            heappush(self.posts[id], (self.stamp, tweetId,userId))
        
        # print(self.posts)
    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        
        while len(result) < 10 and self.posts[userId]:
            # print(self.posts[userId])
            stamp , tId, uId = heappop(self.posts[userId])
            if userId not in self.users[uId]: continue
            result.append((stamp,tId, uId))
        for i in result:
            heappush(self.posts[userId], i)
        ans = []
        for _, id ,_ in result:
            if id not in ans:
                ans.append(id)
        return ans
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followerId)
        self.users[followeeId].add(followeeId)
        self.users[followeeId].add(followerId)
        for post in self.userPost[followeeId]:
            heappush(self.posts[followerId], post)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users[followeeId]:
            self.users[followeeId].remove(followerId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,1],[1],[2,1],[2],[2,1],[2]]
["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed"]
[[],[1,5],[1,3],[1,101],[1,13],[1,10],[1,2],[1,94],[1,505],[1,333],[1]]