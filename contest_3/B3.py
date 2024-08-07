import sys


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def balance_check(node):
    if node.L:
        depth_left = balance_check(node.L)
        if depth_left < 0:
            return -1
        depth_left += 1
    else:
        depth_left = 1

    if node.R:
        depth_right = balance_check(node.R)
        if depth_right < 0:
            return -1
        depth_right += 1
    else:
        depth_right = 1

    if abs(depth_left - depth_right) > 1:
        return -1
    else:
        return max(depth_left, depth_right)


sys.setrecursionlimit(10 ** 6)

n, r = map(int, input().split())
nodes = [BSTNode(i) for i in range(n)]

there_is_a_point = True

for i in range(n):
    left, right = map(int, input().split())
    if (
            (left == -1 and right != -1 and right < i) or
            (left != -1 and left > i and right == -1) or
            (left != -1 and right != -1 and left > i > right)
    ):
        print(0)
        there_is_a_point = False
        break

    if left != -1:
        nodes[i].left = nodes[left]

    if right != -1:
        nodes[i].right = nodes[right]

if there_is_a_point:
    if balance_check(nodes[r]) > 0:
        print(1)
    else:
        print(0)
