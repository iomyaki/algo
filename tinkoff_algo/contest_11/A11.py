import sys
from math import log2, ceil


def get_adjacency_list(n, ancestors):
    graph = {i: [[], [None, None]] for i in range(n)}
    for i in range(n):
        parent = ancestors[i]
        if parent is not None:
            graph[parent][0].append(i)
            graph[i][0].append(parent)

    return graph


def dfs(v):
    global time, depth, max_depth

    max_depth = max(depth, max_depth)

    used.add(v)
    graph[v][1][0] = time
    for w in graph[v][0]:
        if w not in used:
            time += 1
            depth += 1
            dfs(w)
    graph[v][1][1] = time
    time += 1
    depth -= 1


def check_ancestry(a, b):
    a_in, a_out = graph[a][1][0], graph[a][1][1]
    b_in, b_out = graph[b][1][0], graph[b][1][1]

    return a_in <= b_in <= b_out <= a_out


def build_bin_up():
    max_pow_2 = ceil(log2(max_depth))
    bin_up = [[None for _ in range(max_pow_2 + 1)] for _ in range(n)]

    for i in range(max_pow_2 + 1):
        bin_up[0][i] = 0

    for j in range(1, n):
        bin_up[j][0] = ancestors[j]

    for v in range(1, n):
        for pow in range(1, max_pow_2 + 1):
            bin_up[v][pow] = bin_up[bin_up[v][pow - 1]][pow - 1]

    return max_pow_2, bin_up


sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
ancestors = [None] + list(map(int, sys.stdin.readline().split()))
graph = get_adjacency_list(n, ancestors)

depth = 0
max_depth = float('-inf')

# get entry and exit times for each vertex during DFS
used = set()
time = 0
dfs(0)

# get bin-up matrix
max_pow_2, bin_up = build_bin_up()

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if check_ancestry(a, b):
        print(a)
    elif check_ancestry(b, a):
        print(b)
    else:
        for pow in range(max_pow_2, -1, -1):
            ancestor_a = bin_up[a][pow]
            if not check_ancestry(ancestor_a, b):
                a = ancestor_a
        print(bin_up[a][0])
