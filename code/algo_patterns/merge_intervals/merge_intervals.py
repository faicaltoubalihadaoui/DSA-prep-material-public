class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        def overlapped_intervals(interval_1, interval_2):
            return interval_2[0] <= interval_1[1]

        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if overlapped_intervals(merged_intervals[-1], intervals[i]):
                lower = min(merged_intervals[-1][0], intervals[i][0])
                upper = max(merged_intervals[-1][1], intervals[i][1])
                merged_intervals[-1] = [lower, upper]
            else:
                merged_intervals.append(intervals[i])
        return merged_intervals
