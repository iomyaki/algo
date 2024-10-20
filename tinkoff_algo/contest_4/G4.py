n = int(input())
num = n

events = []
current_cover = 0

for _ in range(n):
    h_1, m_1, s_1, h_2, m_2, s_2 = map(int, input().split())
    time_1 = s_1 + m_1 * 60 + h_1 * 3600
    time_2 = s_2 + m_2 * 60 + h_2 * 3600
    events.append((time_1, '+'))
    events.append((time_2, '-'))
    if time_1 == time_2:
        num -= 1
    elif time_1 > time_2:
        current_cover += 1

events.sort()

total_length = 0

if current_cover == num:
    current_left = 0

for event in events:
    if event[1] == '+':
        current_cover += 1
        if current_cover == num:
            current_left = event[0]
    elif event[1] == '-':
        current_cover -= 1
        if current_cover == num - 1:
            total_length += event[0] - current_left

if current_cover == num:
    total_length += 86400 - current_left

print(total_length)
