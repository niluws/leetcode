class Solution:
    def merge(self, intervals):
        j = 0
        for i in range(1, len(intervals)):
            minimum = min(intervals[j])
            maximum = max(intervals[j])

            if minimum <= intervals[i][0] <= maximum or minimum <= intervals[i][1] <= maximum:
                new_start = min(intervals[j][0], intervals[i][0])
                new_end = max(intervals[j][1], intervals[i][1])
                intervals[j] = [new_start, new_end]

            else:
                intervals[j] =intervals[i]
            j += 1
        return intervals[:j]


Solution().merge([[1,3]])
