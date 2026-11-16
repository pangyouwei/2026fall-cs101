from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])

        ans = 0
        last_r = intervals[0][1]
        for i in range(1, n):
            l, r = intervals[i][0], intervals[i][1]
            if l < last_r:
                ans += 1
            else:
                last_r = r

        return ans
