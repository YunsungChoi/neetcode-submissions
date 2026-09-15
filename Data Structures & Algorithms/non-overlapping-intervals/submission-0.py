class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])
        res = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if prev > start: #겹치는경우
                res += 1
                prev = min(end, prev)
            else:
                prev = end

        return res


        