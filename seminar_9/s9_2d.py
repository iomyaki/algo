from math import log2


class SegTree:
    def __init__(self, arr: list[int]) -> None:
        size = len(arr)
        tree = [0] * 2 * size
        for i in range(size):
            tree[size + i] = arr[i]

        for i in reversed(range(size)):
            tree[i] = tree[2 * i + 1] + tree[2 * i]

        self.tree = tree
        self.size = size
        self.promise_set = [[False, 0]] * 2 * size
        self.promise_add = [0] * 2 * size

    def query(self, l: int, r: int = -1) -> int:
        if r == -1:
            r = l + 1
        l += self.size
        r += self.size - 1

        sum = 0
        while l <= r:
            if l % 2 != 0:
                self.push(l)
                sum += self.tree[l]
                l += 1
            if r % 2 == 0:
                self.push(r)
                sum += self.tree[r]
                r -= 1

            l //= 2
            r //= 2
        return sum

    def push(self, pos: int) -> None:
        k = int(log2(self.size * 2 - 1))
        for i in range(k, 0, -1):
            parent = pos >> i  # l / (2 ** i)
            childs = 2 ** i  # 2 ** i
            if self.promise_set[parent][0]:
                tmp = self.promise_set[parent][1]

                self.promise_set[parent] = [False, 0]

                self.promise_set[parent * 2] = [True, tmp]
                self.promise_add[parent * 2] = 0
                self.tree[parent * 2] = int(tmp * childs / 2)

                self.promise_set[parent * 2 + 1] = [True, tmp]
                self.promise_add[parent * 2 + 1] = 0
                self.tree[parent * 2] = int(tmp * childs / 2)

            if self.promise_add[parent] != 0:
                tmp = self.promise_add[parent]
                self.promise_add[parent] = 0

                self.promise_add[parent * 2] += tmp
                self.tree[parent * 2] += int(tmp * childs / 2)

                self.promise_add[parent * 2 + 1] += tmp
                self.tree[parent * 2 + 1] += int(tmp * childs / 2)

        self.promise_set[pos] = [False, 0]
        self.promise_add[pos] = 0

        self.update(pos, self.tree[pos])

    def update(self, pos: int, new_val: int) -> None:
        self.tree[pos] = new_val
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            pos //= 2

    def set(self, l: int, r: int, new_val: int) -> None:
        l += self.size
        r += self.size - 1

        while l <= r:
            if l % 2 != 0:
                self.push(l)
                self.promise_set[l] = [True, new_val]
                self.promise_add[l] = 0
                self.update(l, new_val * int(log2(self.size / l) + 1))
                l += 1
            if r % 2 == 0:
                self.push(r)
                self.promise_set[r] = [True, new_val]
                self.promise_add[r] = 0
                self.update(r, new_val * int(log2(self.size / r) + 1))
                r -= 1

            l //= 2
            r //= 2

    def add(self, l: int, r: int, new_val: int) -> None:
        l += self.size
        r += self.size - 1

        while l <= r:
            if l % 2 != 0:
                self.push(l)
                self.promise_add[l] += new_val
                self.update(l, self.tree[l] + new_val)
                l += 1
            if r % 2 == 0:
                self.push(r)
                self.promise_add[l] += new_val
                self.update(r, self.tree[r] + new_val)
                r -= 1

            l //= 2
            r //= 2

    def print(self):
        print(self.tree)


tree = SegTree([1, 2, 3, 4, 5, -5, -4, -3])

print(tree.query(0, 8))

tree.add(0, 3, 5)
print(tree.query(2))

tree.add(0, 3, -5)
print(tree.query(2))

tree.add(2, 8, -5)
tree.set(0, 8, 2)

print(tree.query(2))

tree.set(0, 8, 2)
tree.add(2, 8, -5)

print(tree.query(2))
