import sys


class DisjointSet:
    def __init__(self, n: int):
        self.n = n
        self.set = {i: i for i in range(1, n + 1)}

    def leader(self, v: int):
        curr, reassign = v, []
        while not self.set[curr] == curr:
            reassign.append(curr)
            curr = self.set[curr]

        for v in reassign:
            self.set[v] = curr

        return curr

    def union(self, a: int, b: int):
        a, b = self.leader(a), self.leader(b)

        if a == b:
            return
        if self.set[a] > self.set[b]:
            a, b = b, a

        self.set[b] = a


def main() -> None:
    t = int(sys.stdin.readline())
    events = []
    sick = set()
    answers = []
    for _ in range(t):
        n, q = map(int, sys.stdin.readline().split())
        ancestors = dict(enumerate((map(int, sys.stdin.readline().split())), start=2))
        ancestors[1] = 1

        for _ in range(q):
            typ, v = sys.stdin.readline().split()
            if typ == "-":
                sick.add(int(v))
            events.append((typ, int(v)))

        dis_set = DisjointSet(n)
        for v in ancestors:
            if v not in sick:
                dis_set.union(ancestors[v], v)

        events.reverse()
        for typ, v in events:
            if typ == "-":
                dis_set.union(v, ancestors[v])
                sick.remove(v)
            else:
                if dis_set.leader(v) in sick:
                    answers.append(dis_set.leader(v))
                else:
                    answers.append(-1)

        answers.reverse()
        print(*answers)

        del events[:]
        del answers[:]
        sick.clear()


if __name__ == "__main__":
    main()
