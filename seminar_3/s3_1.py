class BSTNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value, self)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BSTNode(value, self)
                else:
                    self.right.insert(value)
        else:
            self.value = value


def in_order_traversal(node: BSTNode) -> None:
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)


def pre_order_traversal(node: BSTNode) -> None:
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node: BSTNode) -> None:
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')


root = BSTNode(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)


print('In-order traversal:')
in_order_traversal(root)
print()
print('Pre-order traversal:')
pre_order_traversal(root)
print()
print('Post-order traversal:')
post_order_traversal(root)
print()

from math import log2


lst = [7, 4, 9, 3, 5, 8, 10, 1, '-', '-', 6, '-', '-', '-', 11, 0, 2, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

lst_length = len(lst)
h = int(log2(lst_length)) + 1
width = 2 ** h - 1

i = 0
for level in range(1, h + 1):
    spaces = width // 2 ** (level - 1)
    for _ in range(2 ** (level - 1)):
        if i < lst_length:
            print(' ' * spaces, lst[i], ' ' * spaces, ' ', sep='', end='')
            i += 1
    print()
