import sys


def kth_statistic(array, left, right, k):
    if right <= left:
        return

    # partition
    x = array[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while array[i] < x:
            i += 1
        while array[j] > x:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j < k < i:
        return

    if k <= j:
        kth_statistic(array, left, j, k)
    else:
        kth_statistic(array, i, right, k)


def main():
    n, q = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())

    # build random array
    array = []
    cur = 0
    for _ in range(n):
        cur = (cur * a + b) % 4294967296
        x = cur >> 8
        cur = (cur * a + b) % 4294967296
        y = cur >> 8
        array.append(((x << 8) ^ y) % 4294967296)

    kth_statistic(array, 0, n - 1, q - 1)
    print(array[q - 1])


if __name__ == "__main__":
    main()
