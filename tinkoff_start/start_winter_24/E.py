n, m, q = map(int, input().split())
values = tuple(map(int, input().split()))

children = {}
for count, value in enumerate(values):
    children[count + 1] = value

del values

friends = {i: [] for i in range(1, m + 1)}
for _ in range(m):
    pair = tuple(map(int, input().split()))
    friends[pair[0]].append(pair[1])
    friends[pair[1]].append(pair[0])

del pair

for _ in range(q):
    event = input().split()
    if event[0] == '+':
        for friend in friends[int(event[1])]:
            children[friend] += int(event[2])
    else:
        print(children[int(event[1])])
