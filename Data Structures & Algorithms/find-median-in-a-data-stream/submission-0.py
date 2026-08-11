class MedianFinder:

    def __init__(self):
        self.heapLeft = []
        self.heapRight = []
        

    def addNum(self, num: int) -> None:

        if not self.heapLeft or -self.heapLeft[0] >= num:
            heapq.heappush(self.heapLeft, -num)
        else:
            heapq.heappush(self.heapRight, num)

        self.rearrange()

    def findMedian(self) -> float:
        
        if len(self.heapLeft) > len(self.heapRight):
            return float(-self.heapLeft[0] / 1.0)
        else:
            return float((-self.heapLeft[0] + self.heapRight[0])/2.0)
        
    def rearrange(self):
        if len(self.heapLeft) > len(self.heapRight) + 1:
            heapq.heappush(self.heapRight, -heapq.heappop(self.heapLeft))
        elif len(self.heapRight) > len(self.heapLeft):
            heapq.heappush(self.heapLeft, -heapq.heappop(self.heapRight))
