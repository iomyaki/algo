import sys


def lower_bound(array, target):
    l, r = -1, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m][1] < target:
            l = m
        else:
            r = m

    return r


def upper_bound(array, target):
    l, r = -1, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m][1] <= target:
            l = m
        else:
            r = m

    return r


def bin_search(array, lb, ub, left, right, target):
    l, r = lb - 1, ub
    while r - l > 1:
        m = (l + r) // 2
        if array[m][0] < left:
            l = m
        else:
            r = m

    return r < len(array) and array[r][1] == target and left <= array[r][0] <= right


def main():
    input()
    array = sorted(enumerate(map(int, sys.stdin.readline().split()), start=1), key=lambda y: y[1])
    for _ in range(int(input())):
        l, r, x = map(int, sys.stdin.readline().split())
        if bin_search(array, lower_bound(array, x), upper_bound(array, x), l, r, x):
            print(1, end="")
        else:
            print(0, end="")


if __name__ == "__main__":
    main()
