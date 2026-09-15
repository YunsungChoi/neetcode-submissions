class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])

        # res = [intervals[0]]

        # for start, end in intervals[1:]:
        #     lastEnd = res[-1][1]
        #     if start <= lastEnd:
        #         res[-1][1] = max(end, lastEnd)
        #     else:
        #         res.append([start, end])

        # return res
            
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        while i < n: #이미 newInterval과 겹치는구간은 지났음!
            res.append(intervals[i])
            i += 1

        return res

        


        