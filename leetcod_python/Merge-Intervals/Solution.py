# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        pre = intervals[0]
        res = []
        curIdx = 0
        res.append(intervals[0])
        for interval in intervals[1:]:
            if interval.start <= pre.end:
                right = max(pre.end, interval.end)
                res[curIdx].end = right
            else:
                res.append(interval)
                pre = interval
                curIdx += 1
        return res
        
