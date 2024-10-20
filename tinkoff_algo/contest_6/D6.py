from collections import deque


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = set()
        self.level = -1
        self.parent = None

    def get_children(self):
        for x, y in knight_moves:
            new_x = self.x + x
            new_y = self.y + y
            if 1 <= new_x <= n and 1 <= new_y <= n and (new_x, new_y) not in coords:
                children = Node(new_x, new_y)
                self.children.add(children)
                nodes.append(children)

                coords.add((new_x, new_y))


def bfs(root):
    root.level = 0
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in v.children:
            if w.level == -1:
                queue.append(w)
                w.level = v.level + 1
                w.parent = v

                if w.x == x_2 and w.y == y_2:
                    return w


n = int(input())
x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())

knight_moves = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))

root = Node(x_1, y_1)
nodes = [root]
coords = {(x_1, y_1)}

for node in nodes:
    if len(nodes) == n ** 2:
        break
    node.get_children()

target_node = bfs(root)

print(target_node.level)

path = [(x_2, y_2)]
while target_node.parent is not None:
    target_node = target_node.parent
    x = target_node.x
    y = target_node.y
    path.append((x, y))

for node in path[::-1]:
    print(*node)
