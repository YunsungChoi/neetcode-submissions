"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #guard 조건은 맨 위에!
        if len(intervals) < 1:
            return True

        intervals.sort(key=lambda x: x.start)
        prevEnd = intervals[0].end
    
        for cur in intervals[1:]:
            if cur.start >= prevEnd:
                prevEnd = cur.end
            else:
                return False
        
        return True
