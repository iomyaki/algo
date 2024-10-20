import math


class SegTree:
    def __init__(self, n):
        power = math.ceil(math.log2(n))
        self.n = 2 ** power
        self.range = range(power, 0, -1)
        self.tree = [0 for _ in range(2 * self.n)]
        self.promises = [0 for _ in range(2 * self.n)]

    def update(self, pos, val):
        self.tree[pos] += val
        pos //= 2
        while pos > 0:
            self.tree[pos] = min(self.tree[pos * 2], self.tree[pos * 2 + 1])
            pos //= 2

    def push(self, pos):
        for i in self.range:
            parent = pos // 2 ** i
            if parent != 0 and self.promises[parent] != 0:
                promise = self.promises[parent]
                self.promises[parent] = 0

                self.tree[parent * 2] += promise
                self.promises[parent * 2] += promise

                self.tree[parent * 2 + 1] += promise
                self.promises[parent * 2 + 1] += promise

    def add(self, left, right, val):
        left = left + self.n
        right = right + self.n

        while left <= right:
            if left % 2 == 1:
                self.push(left)
                self.promises[left] += val
                self.update(left, val)
                left += 1

            if right % 2 == 0:
                self.push(right)
                self.promises[right] += val
                self.update(right, val)
                right -= 1

            left //= 2
            right //= 2

    def query(self, left, right):
        left = left + self.n
        right = right + self.n

        minimum = float('inf')
        while left <= right:
            if left % 2 == 1:
                self.push(left)
                minimum = min(minimum, self.tree[left])
                left += 1

            if right % 2 == 0:
                self.push(right)
                minimum = min(minimum, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        print(minimum)


n, m = map(int, input().split())
tree = SegTree(n)
for _ in range(m):
    q = tuple(map(int, input().split()))
    if q[0] == 1:
        tree.add(q[1], q[2] - 1, q[3])
    else:
        tree.query(q[1], q[2] - 1)
