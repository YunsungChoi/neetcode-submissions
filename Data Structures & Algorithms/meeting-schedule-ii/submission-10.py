"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        # res = 0 # global max # of room 
        # count = 0 # local max # of room
        # s, e = 0, 0 #two pointers

        # while s < len(intervals):
        #     if start[s] < end[e]:
        #         s += 1
        #         count += 1
        #     else:
        #         e += 1
        #         count -= 1

        #     res = max(res, count)
        # return res

        intervals.sort(key=lambda x: x.start)
        minHeap = []

        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)

        return len(minHeap)
    
        
        