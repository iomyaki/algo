import sys


n, m = map(int, sys.stdin.readline().split())

tree = [[0, 0, -1] for _ in range(n * 4)]


def sum_tree(node, tl, tr, l, r):
    chek(node, tl, tr)
    if l > r:
        return 0

    if l == tl and r == tr:
        return tree[node][0]

    mid = (tl + tr) // 2
    l_sum = sum_tree(node * 2 + 1, tl, mid, l, min(r, mid))
    r_sum = sum_tree(node * 2 + 2, mid + 1, tr, max(l, mid + 1), r)

    return l_sum + r_sum


def chek(node, tl, tr):
    if tree[node][2] != -1:
        tree[node][0] = tree[node][2] * (tr - tl + 1)
        if tr - tl > 0:
            tree[node * 2 + 1][2] = tree[node][2]
            tree[node * 2 + 2][2] = tree[node][2]
            tree[node * 2 + 1][1] = 0
            tree[node * 2 + 2][1] = 0
        tree[node][2] = -1

    if tree[node][1] == 0:
        return

    tree[node][0] += tree[node][1] * (tr - tl + 1)
    if tr - tl > 0:
        tree[node * 2 + 1][1] += tree[node][1]
        tree[node * 2 + 2][1] += tree[node][1]
    tree[node][1] = 0


def update_tree(node, tl, tr, l, r, u, op):
    chek(node, tl, tr)
    if l > r:
        return

    if l == tl and r == tr:
        if op == 1:
            tree[node][1] += u
        elif op == 2:
            tree[node][2] = u
            # tree[node][1] = 0
        chek(node, tl, tr)
        return

    mid = (tl + tr) // 2
    update_tree(node * 2 + 1, tl, mid, l, min(r, mid), u, op)
    update_tree(node * 2 + 2, mid + 1, tr, max(l, mid + 1), r, u, op)

    tree[node][0] = tree[node * 2 + 1][0] + tree[node * 2 + 2][0]


for _ in range(m):
    op, l, r, *u = map(int, sys.stdin.readline().split())
    if op == 2:
        update_tree(0, 0, n - 1, l, r - 1, u[0], 1)
    elif op == 3:
        print(sum_tree(0, 0, n - 1, l, r - 1))
    elif op == 1:
        update_tree(0, 0, n - 1, l, r - 1, u[0], 2)
    # print(tree)
