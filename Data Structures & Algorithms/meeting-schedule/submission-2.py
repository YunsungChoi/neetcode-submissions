"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)
        if len(intervals) < 1:
            return True

        prevTime = intervals[0]
        prevEnd = prevTime.end
        prevSta = prevTime.start

        for cur in intervals[1:]:
            if cur.start >= prevEnd:
                prevEnd = cur.end
            else:
                return False
        
        return True
