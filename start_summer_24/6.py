from collections import deque


class Node:
    def __init__(self, x, y, mode):
        self.x = x
        self.y = y
        self.children = set()
        self.level = -1
        self.mode = mode

    def get_children(self):
        if self.mode == 'knight':
            for x, y in knight_moves:
                new_x = self.x + x
                new_y = self.y + y

                if 0 <= new_x <= n - 1 and 0 <= new_y <= n - 1 and (new_x, new_y) not in coords_knight:
                    if board[new_y][new_x] == 'G':
                        mode = 'king'
                    else:
                        mode = 'knight'

                    child = Node(new_x, new_y, mode)
                    self.children.add(child)
                    nodes.append(child)

                    coords_knight.add((new_x, new_y))

        elif self.mode == 'king':
            for x, y in king_moves:
                new_x = self.x + x
                new_y = self.y + y

                if 0 <= new_x <= n - 1 and 0 <= new_y <= n - 1 and (new_x, new_y) not in coords_king:
                    if board[new_y][new_x] == 'K':
                        mode = 'knight'
                    else:
                        mode = 'king'

                    child = Node(new_x, new_y, mode)
                    self.children.add(child)
                    nodes.append(child)

                    coords_king.add((new_x, new_y))


def bfs(root):
    root.level = 0
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in v.children:
            if w.level == -1:
                queue.append(w)
                w.level = v.level + 1

                if w.x == x_2 and w.y == y_2:
                    return w.level

    return -1


knight_moves = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))
king_moves = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))

n = int(input())
board = []
x_1, y_1 = -1, -1
x_2, y_2 = -1, -1
for i in range(n):
    row = list(input())
    for j in range(n):
        if row[j] == 'S':
            x_1, y_1 = j, i
        elif row[j] == 'F':
            x_2, y_2 = j, i
    board.append(row)

root = Node(x_1, y_1, 'knight')
nodes = [root]
coords_knight = {(x_1, y_1)}
coords_king = set()

for node in nodes:
    node.get_children()

print(bfs(root))
