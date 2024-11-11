def merge(intervals: list):
    events = []
    for interval in intervals:
        events.append((interval[0], 0))
        events.append((interval[1], 1))
    events.sort(key=lambda x: (x[0], x[1]))

    n = len(events)
    non_intersecting = []
    start = -1
    opened = 0
    for i in range(len(events)):
        event = events[i]
        if event[1] == 0:
            if opened <= 0 and events[i - 1][0] != event[0]:
                start = event[0]
            opened += 1
        else:
            opened -= 1
            if opened <= 0:
                if i + 1 < n and events[i + 1][0] != event[0] or i + 1 == n:
                    non_intersecting.append([start, event[0]])

    return non_intersecting


lst = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(lst))
