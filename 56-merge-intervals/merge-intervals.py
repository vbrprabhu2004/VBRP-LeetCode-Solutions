class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        # Step 1: Sort the intervals by start time
        sorted_intervals = sorted(intervals)

        result = []
        start, end = sorted_intervals[0]

        # Step 2: Traverse and compare
        for i in range(1, len(sorted_intervals)):
            curr_start, curr_end = sorted_intervals[i]

            if curr_start <= end:
                # Overlapping: merge by extending end
                end = max(end, curr_end)
            else:
                # No overlap: add previous and reset start/end
                result.append([start, end])
                start, end = curr_start, curr_end

        # Add the last interval
        result.append([start, end])
        return result
