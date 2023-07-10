from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    l = []
    s = intervals[0][0]
    e = intervals[0][1]
    for i in intervals:
        if i[0] <= e:
            e = max(e, i[1])
        else:
            l.append([s, e])
            s = i[0]
            e = i[1]
    l.append([s, e])
    return l


intervals = [[1,3],[2,6],[8,10],[15,18]]
res = merge(intervals)
print("After merging : ", res)