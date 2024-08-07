n = int(input())

events = []

for _ in range(n):
    start, end = map(int, input().split())
    events.append((start, '+'))
    events.append((end, '-'))

events.sort()

current_length = 0
total_length = 0
for event in events:
    if event[1] == '+':
        current_length += 1
        if current_length == 1:
            current_left = event[0]
    elif event[1] == '-':
        current_length -= 1
        if current_length == 0:
            total_length += event[0] - current_left

print(total_length)
