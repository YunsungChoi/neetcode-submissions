class Twitter:
    def __init__(self):
        self.time = 0 
        self.tweetMap = defaultdict(list) # key - userId, value - (time, tweetId)
        self.followMap = defaultdict(set) #중복제거위함; key = userID, values = 
        # tweet객체 with userId and tweetId and 이 객체모음필요? (그럼 그게 힙이겠네)
         # 시간순? userId별? tweetId별? <- 최근이면 높은숫자로 가정하면 쉬울텐데? 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        1. 팔로우 목록 가져오기 (+ 자기 자신 추가)
        2. 각 사람의 트윗 리스트에서 "가장 최근 것"만 힙에 후보로 넣기
        3. 힙에서 10번 뽑되, 뽑을 때마다 그 사람의 "그다음 최근 것"을 힙에 보충
        '''

        heap = []
        followList = self.followMap
        followList[userId].add(userId)

        for followeeId in followList[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, (-time, tweetId, followeeId, index -1)) # for the next(second latest) tweet

        res = []
        while heap and len(res) < 10:
            negTime, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                time, nextId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, (-time, nextId, followeeId, index -1))

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId) # safer than remove - even when there's no key, no Error
