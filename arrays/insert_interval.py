"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""


def insert(intervals, new_interval):
    result = []

    for interval in intervals:
        # case 1: new interval is after the range of the current interval
        if interval[1] < new_interval[0]:
            # add interval since there is no overlap here
            result.append(interval)
        # case 2: new interval is before the range of the current interval
        elif interval[0] > new_interval[1]:
            # add the new interval since it comes before
            result.append(new_interval)
            # the other interval becomes the "new interval"
            new_interval = interval
        # case 3: new interval is within the range of the current interval
        else:
            # merge the interval and continue checking
            new_interval = [
                min(new_interval[0], interval[0]),
                max(new_interval[1], interval[1])
            ]

    # when we reach the end of the list we still have new interval to append to the end
    result.append(new_interval)
    return result


"""
idea:

iterate through the intervals
there are 3 cases to consider given the "new interval" and the "current interval"

case 1:
new interval comes after the current interval
    - add the current interval to the result
    - continue using new interval to check further intervals


    1 --- 3     5 --- 6
    ^           ^
    current     new

case 2:
new interval comes before current interval
    - add new interval to the result
    - current interval becomes "new interval"
        - continue using current interval to check further intervals


    1 --- 3     5 --- 6
    ^           ^
    new         current


case 3:
there is some kind of overlap
    - there are several cases of overlap but we basically want to take the min and max values for the newly merged interval


    1 --- 5         =>      1 --- 6
       3 --- 6


       2 --- 6      =>      1 --- 6
    1 --- 5


    1 ------- 6     =>      1 --- 6
      2 --- 5

at the end we need to remember to add the hanging "new interval" to the result and return

---

time complexity:

every interval is read once plus the merge interval so the overall time complexity is O(n)

---

space complexity:

in the worst case, there is no overlap and the new interval is added into the original nums list
this results in a worst case of O(n) where `n` is the number of intervals
"""
