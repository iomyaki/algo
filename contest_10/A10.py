import sys


class DisjointSet:
    def __init__(self, n: int):
        self.n = n
        self.set = {i: [i, i, i, 1] for i in range(1, n + 1)}

    def leader(self, v: int):
        if self.set[v][0] == v:
            return v
        else:
            self.set[v][0] = self.leader(self.set[v][0])
            return self.set[v][0]

    def union(self, a: int, b: int):
        a, b = self.leader(a), self.leader(b)

        if a == b:
            return

        if self.set[a][3] > self.set[b][3]:
            a, b = b, a

        self.set[a][0] = b
        self.set[b][1] = min(self.set[a][1], self.set[b][1])
        self.set[b][2] = max(self.set[a][2], self.set[b][2])
        self.set[b][3] += self.set[a][3]

    def get(self, v: int):
        answer = self.set[self.leader(v)]
        print(answer[1], answer[2], answer[3])


sys.setrecursionlimit(10 ** 9)
n, m = map(int, sys.stdin.readline().split())
dis_set = DisjointSet(n)
for _ in range(m):
    query = sys.stdin.readline().split()
    if query[0] == 'union':
        dis_set.union(int(query[1]), int(query[2]))
    else:
        dis_set.get(int(query[1]))
