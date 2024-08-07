from collections import deque


_ = input()
train_1 = deque(list(map(int, input().split())))  # head — tail
train_2 = deque([])  # tail — head

operations = []

train_len = len(train_1)

n = 1
try:
    while n <= train_len:
        i = train_1.index(n)
        move_from_1 = i + 1
        operations.append(f'1 {move_from_1}')
        while i != -1:
            train_2.append(train_1.popleft())
            i -= 1

        n = train_2.pop()
        move_from_2 = 1
        while len(train_2) != 0 and train_2[-1] == n + 1:
            n = train_2.pop()
            move_from_2 += 1
        operations.append(f'2 {move_from_2}')

        n += 1

    print(len(operations))
    print(*operations, sep='\n')
except ValueError:
    print(0)
