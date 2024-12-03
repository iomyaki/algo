import sys


class DisjointSet:
    def __init__(self, n: int):
        self.n = n
        self.set = {i: [i, 1] for i in range(1, n + 1)}

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

        if self.set[a][1] > self.set[b][1]:
            a, b = b, a

        self.set[a][0] = b
        self.set[b][1] += self.set[a][1]


def main() -> None:
    n, m, k = map(int, sys.stdin.readline().split())
    for _ in range(m):
        sys.stdin.readline()
    events = []
    for _ in range(k):
        typ, a, b = sys.stdin.readline().split()
        events.append((typ, int(a), int(b)))

    dis_set = DisjointSet(n)
    events.reverse()
    answers = []
    for typ, a, b in events:
        if typ == "ask":
            if dis_set.leader(a) == dis_set.leader(b):
                answers.append("YES")
            else:
                answers.append("NO")
        else:
            dis_set.union(a, b)

    answers.reverse()
    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()
