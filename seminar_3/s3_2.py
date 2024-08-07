"""
In-order traversal of BST w/o recursion, memory complexity = O(1)
"""

class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, self)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value, self)
                else:
                    self.right.insert(value)
        else:
            self.value = value


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

node = root
if node:
    while node.left:
        node = node.left
    while node:
        print(node.value, end=' ')
        if node.right:
            node = node.right
            while node.L:
                node = node.L
        else:
            while node.parent and node.parent.R is node:
                node = node.parent
            node = node.parent
