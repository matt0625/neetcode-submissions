from collections import deque, defaultdict
class Twitter:

    def __init__(self):
        self.tweets = deque()
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        ptr = len(self.tweets) - 1
        while len(feed) < 10 and ptr >= 0:
            a, b = self.tweets[ptr]
            if a == userId or a in self.follow_map[userId]:
                feed.append(b)
            
            ptr -= 1

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
