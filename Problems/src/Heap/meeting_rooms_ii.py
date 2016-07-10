"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

For example,
Given [[0, 30],[5, 10],[15, 20]], return 2.
"""


from heapq import heappush, heappop


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals = sorted(intervals, key=lambda x: (x.start, x))
    finish_times = []
    count = 0
    for interval in intervals:
        if not finish_times or interval.start < min(finish_times):
            count += 1
        else:
            heappop(finish_times)
        heappush(finish_times, interval.end)
    return count


if __name__ == '__main__':
    TOTAL_ROOMS = min_meeting_rooms([Interval(4, 18), Interval(1, 35),
                                     Interval(12, 45), Interval(25, 46),
                                     Interval(22, 27)])
    assert TOTAL_ROOMS == 4
