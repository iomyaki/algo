from collections import deque


def create_adjacency_list(ancestors):
    n = len(ancestors)
    adj_list = {i: [] for i in range(n)}

    for i in range(n):
        parent = ancestors[i]
        if parent is not None:
            adj_list[parent].append(i)
            adj_list[i].append(parent)

    return list(adj_list.values())


def bfs(adj_list, s):
    level = [-1] * len(adj_list)

    level[s] = 0
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for w in adj_list[v]:
            if level[w] == -1:
                queue.append(w)
                level[w] = level[v] + 1

    return level


_ = input()
ancestors = [None] + list(map(int, input().split()))
adj_list = create_adjacency_list(ancestors)

depths = bfs(adj_list, 0)

v, u, w = 0, 0, 0
for i in range(len(adj_list)):
    if depths[i] > depths[u]:
        u = i

d = bfs(adj_list, u)
for j in range(len(d)):
    if d[j] > d[w]:
        w = j

print(max(depths), end=' ')  # the 1st task
print(d[w])  # the 2nd task
print(*depths)  # the 3rd task
