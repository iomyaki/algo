from collections import deque


n = int(input())
marks = list(map(int, input().split()))

queue = deque([])
bad = deque([])
exc = deque([])
largest_exc = -1

i = 0
while i != min(n, 7):
    mark = marks[i]
    queue.append(mark)
    if mark == 2 or mark == 3:
        bad.append(mark)
    elif mark == 5:
        exc.append(mark)
    i += 1

if len(bad) == 0:
    largest_exc = max(largest_exc, len(exc))

if n > 7:
    for j in range(i, n):
        mark = marks[j]
        queue.append(mark)
        if mark == 2 or mark == 3:
            bad.append(mark)
        elif mark == 5:
            exc.append(mark)

        exiting = queue.popleft()
        if len(exc) != 0 and exc[0] == exiting:
            exc.popleft()
        if len(bad) != 0 and bad[0] == exiting:
            bad.popleft()

        if len(bad) == 0:
            largest_exc = max(largest_exc, len(exc))

print(largest_exc)
