class Twitter:

    import heapq

    def __init__(self):
        self.timestamp = 0

        self.tweets = {} # userid -> list of (time, tweetid) 
        self.following = {}  # userid -> list of followings

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets.setdefault(userId, []).append((self.timestamp, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # this is where we use the heap
        heap = []

        followees = self.following.get(userId, set())

        # build heap for user's tl by checking user and following
        for u in self.tweets:
            if u == userId or u in followees:
                for ts, tid in self.tweets[u]: # last element = most recent (oldest timestamp)
                    heapq.heappush(heap, (-ts, tid)) # min heap, oldest = most recent = negate it for min val
        
        heapq.heapify(heap)

        feed = [] # build this user's feed

        # get 10 most recent (e.g. largest timestamp)
        while heap and len(feed) < 10:
            tweet = heapq.heappop(heap)
            feed.append(tweet[1])
        
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: # check if user following themselves
            return
        self.following.setdefault(followerId, set()).add(followeeId) 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).discard(followeeId) # no array, use set and discard
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)