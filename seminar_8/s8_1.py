import math


def pow_of_2(number):
    """
    Returns the closest from above power of 2 to a given number
    """

    power_of_2 = math.ceil(math.log2(number))
    return 2 ** power_of_2


a = [3, 9, 7, 10, 0, 2, 3, 1, 10]
n = len(a)
power = pow_of_2(n)  # == len / 2 of segment_tree

segment_tree = [0 for _ in range(2 * power)]

for i in range(n):
    segment_tree[power + i] = a[i]

for i in range(2 * power - 1, 2, -2):
    segment_tree[i // 2] = segment_tree[i - 1] + segment_tree[i]

print(segment_tree)


def update_tree(i, element):
    i += power
    previous = segment_tree[i]
    diff = element - previous
    segment_tree[i] = element
    while i != 1:
        i //= 2
        segment_tree[i] += diff


update_tree(3, 5)

print(segment_tree)
