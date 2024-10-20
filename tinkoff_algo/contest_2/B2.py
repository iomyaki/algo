from collections import deque


_, k = map(int, input().split())
arr = tuple(map(int, input().split()))

queue = deque()
mn = deque()

for i in arr:
    if len(queue) == k:
        print(mn[0], end=' ')

    queue.append(i)

    while len(mn) > 0 and mn[-1] > i:
        mn.pop()

    mn.append(i)

    if len(queue) > k:
        exiting = queue.popleft()
        if mn[0] == exiting:
            mn.popleft()

else:
    print(mn[0])
