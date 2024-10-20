import sys
from math import log2, floor


class SegTree:
    def __init__(self):
        self.range = range(20, 0, -1)
        self.tree = [0 for _ in range(2097152)]
        self.prom = [-1 for _ in range(2097152)]

    def update(self, pos, val):
        self.tree[pos] = val
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
            pos //= 2

    def push(self, pos):
        for i in self.range:
            parent = pos // 2 ** i

            if parent != 0 and self.prom[parent] != -1:
                promise = self.prom[parent]
                self.prom[parent] = -1

                j = 20 - floor(log2(parent))
                ch_theor = 2 ** (j - 1)

                left_parent = parent * 2
                children = max(0, min(ch_theor,
                                      ch_theor - ((left_parent * 2 ** (j - 1) + ch_theor - 1) - 2048576)))
                self.tree[left_parent] = promise * children
                self.prom[left_parent] = promise

                right_parent = parent * 2 + 1
                children = max(0, min(ch_theor,
                                      ch_theor - ((right_parent * 2 ** (j - 1) + ch_theor - 1) - 2048576)))
                self.tree[right_parent] = promise * children
                self.prom[right_parent] = promise

    def set(self, left, right, val):
        right = left + right + 1548575
        left = left + 1548576

        while left <= right:
            if left % 2 == 1:
                level = 20 - floor(log2(left))
                ch_theor = 2 ** level
                children = max(0, min(ch_theor, ch_theor - ((left * 2 ** level + ch_theor - 1) - 2048576)))

                self.push(left)
                self.prom[left] = val
                self.update(left, val * children)
                left += 1

            if right % 2 == 0:
                level = 20 - floor(log2(right))
                ch_theor = 2 ** level
                children = max(0, min(ch_theor, ch_theor - ((left * 2 ** level + ch_theor - 1) - 2048576)))

                self.push(right)
                self.prom[right] = val
                self.update(right, val * children)
                right -= 1

            left //= 2
            right //= 2


tree = SegTree()
m = int(sys.stdin.readline())
for _ in range(m):
    q = tuple(sys.stdin.readline().split())
    if q[0] == 'W':
        tree.set(int(q[1]), int(q[2]), 0)
    else:
        tree.set(int(q[1]), int(q[2]), 1)
    print(tree.tree[1])

# not solved
