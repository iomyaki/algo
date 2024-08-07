import sys


class DisjointSet:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.set = {}
        self.build()

    def build(self):
        for i in range(self.n):
            for j in range(self.m):
                self.set[(i, j)] = [(i, j), 1]

    def leader(self, v: tuple):
        if self.set[v][0] == v:
            return v
        else:
            self.set[v][0] = self.leader(self.set[v][0])
            return self.set[v][0]

    def union(self, a: tuple, b: tuple):
        a, b = self.leader(a), self.leader(b)

        if a == b:
            return

        if self.set[a][1] > self.set[b][1]:
            a, b = b, a

        self.set[a][0] = b
        self.set[b][1] += self.set[a][1]


def Kruskal(edges: list):
    edges.sort(key=lambda x: x[2])
    new_edges = []
    mst_weight = 0  # minimum spanning tree weight

    for a, b, weight in edges:
        if dis_set.leader(a) != dis_set.leader(b):
            dis_set.union(a, b)
            new_edges.append((a[0] + 1, a[1] + 1, weight))
            mst_weight += weight

    return mst_weight, new_edges


sys.setrecursionlimit(10 ** 9)
n, m = map(int, sys.stdin.readline().split())
dis_set = DisjointSet(n, m)
edges = []
for i in range(n):
    row = tuple(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if row[j] == 0:
            if i != n - 1:
                edges.append(((i, j), (i + 1, j), 1))
            if j != m - 1:
                edges.append(((i, j), (i, j + 1), 2))
        elif row[j] == 1:
            dis_set.union((i, j), (i + 1, j))
            if j != m - 1:
                edges.append(((i, j), (i, j + 1), 2))
        elif row[j] == 2:
            if i != n - 1:
                edges.append(((i, j), (i + 1, j), 1))
            dis_set.union((i, j), (i, j + 1))
        else:
            dis_set.union((i, j), (i + 1, j))
            dis_set.union((i, j), (i, j + 1))

mst_weight, new_edges = Kruskal(edges)
print(len(new_edges), mst_weight)
for new_edge in new_edges:
    print(*new_edge)
