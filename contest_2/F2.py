import sys
from collections import deque


n = int(sys.stdin.readline())

queue = deque([])  # (theater) — head — tail
positions = {}
shift = 0
queue_len = 0

for _ in range(n):
    query = tuple(sys.stdin.readline().split())
    if query[0] == '1':
        positions[query[1]] = queue_len + shift
        queue.append(query[1])
        queue_len += 1
    elif query[0] == '2':
        queue.popleft()
        shift += 1
        queue_len -= 1
    elif query[0] == '3':
        queue.pop()
        queue_len -= 1
    elif query[0] == '4':
        print(positions[query[1]] - shift)
    elif query[0] == '5':
        print(queue[0])
