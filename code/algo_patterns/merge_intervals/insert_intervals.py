class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        def overlapping_intervals(interval_1, interval_2):
            return interval_2[0] <= interval_1[1] and interval_2[1] >= interval_1[0]

        if not intervals:
            return [newInterval]

        merged_intervals = []
        tmp = newInterval
        for i in range(len(intervals)):
            if overlapping_intervals(intervals[i], tmp):
                lower = min(tmp[0], intervals[i][0])
                upper = max(tmp[1], intervals[i][1])
                tmp = [lower, upper]
            else:
                merged_intervals.append(intervals[i])
        merged_intervals.append(tmp)
        merged_intervals.sort(key=lambda x: x[0])
        return merged_intervals
