import math


def pow_of_2(number):
    """
    Returns the closest from above power of 2 to a given number
    """
    power_of_2 = math.ceil(math.log2(number))
    return 2 ** power_of_2


def build(a):
    n = len(a)
    p = pow_of_2(n)  # == len / 2 of segment_tree
    segment_tree = [0 for _ in range(2 * p)]

    for i in range(n):
        segment_tree[p + i] = a[i]

    for i in range(2 * p - 1, 2, -2):
        segment_tree[i // 2] = segment_tree[i - 1] + segment_tree[i]

    return segment_tree, p


def update(pos, val):
    pos += power
    diff = val - tree[pos]
    tree[pos] = val
    while pos != 1:
        pos //= 2
        tree[pos] += diff


def query(left, right):
    if left == right:
        return tree[left + power]

    left, right = left + power, right + power
    summ = 0
    while left < right:
        if left % 2 != 0:
            summ += tree[left]
            left += 1

        if right % 2 == 0:
            summ += tree[right]
            right -= 1

        left //= 2
        right //= 2

        if left == right:
            summ += tree[left]
        elif left == right - 1:
            summ += tree[left] + tree[right]
            break

    return summ


n, m = map(int, input().split())
nods = tuple(map(int, input().split()))
tree, power = build(nods)
for _ in range(m):
    tp, a, b = map(int, input().split())
    if tp == 1:
        update(a, b)
    else:
        print(query(a, b - 1))
