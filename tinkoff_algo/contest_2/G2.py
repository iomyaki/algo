import sys
from collections import deque


first_half = deque([])
second_half = deque([])

for _ in range(int(sys.stdin.readline())):
    query = tuple(sys.stdin.readline().split())
    if query[0] == '+':
        second_half.append(query[1])
    elif query[0] == '*':
        second_half.appendleft(query[1])
    elif query[0] == '-':
        print(first_half.popleft())

    if len(first_half) < len(second_half):
        first_half.append(second_half.popleft())
