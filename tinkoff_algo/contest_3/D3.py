class Heap:
    def __init__(self):
        self.body = []
        self.size = 0

    def insert(self, x):
        self.body.append(x)
        x_i = self.size  # will be 0 for the very first element etc.
        x_parent_i = x_i // 2
        x_parent = self.body[x_parent_i]
        while x < x_parent:
            self.body[x_i], self.body[x_parent_i] = self.body[x_parent_i], self.body[x_i]
            x_i = x_parent_i
            x_parent_i = x_i // 2
            x_parent = self.body[x_parent_i]

        self.size += 1

    def extract(self):
        last_parent_i = (self.size - 1) // 2
        max_elem_i = -1
        max_elem = float('-inf')
        for j in range(last_parent_i + 1, self.size):
            if self.body[j] > max_elem:
                max_elem = self.body[j]
                max_elem_i = j
        self.body[-1], self.body[max_elem_i] = self.body[max_elem_i], self.body[-1]
        x_i = max_elem_i
        x = self.body[max_elem_i]

        print(self.body.pop())
        self.size -= 1

        if self.size > 1:
            parent_i = x_i // 2
            parent = self.body[parent_i]
            while x < parent:
                self.body[parent_i], self.body[x_i] = self.body[x_i], self.body[parent_i]
                x_i = parent_i
                parent_i = x_i // 2
                parent = self.body[parent_i]


heap = Heap()

for _ in range(int(input())):
    query = input().split()
    if query[0] == '0':
        heap.insert(int(query[1]))
    else:
        heap.extract()
