import sys
from math import floor


def insertion_sort(arr):
    if len(arr) == 1:
        return

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    t, n = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())

    cur = 0
    buckets = [[] for _ in range(n)]
    const = n / 4294967296

    for _ in range(t):
        idx, summ = 1, 0

        for _ in range(n):
            cur = (cur * a + b) % 4294967296
            x = cur >> 8
            cur = (cur * a + b) % 4294967296
            y = cur >> 8
            z = ((x << 8) ^ y) % 4294967296

            buckets[floor(const * z)].append(z)

        for bucket in buckets:
            insertion_sort(bucket)
            for x in bucket:
                summ += x * idx
                idx += 1
            del bucket[:]
        print(summ)


if __name__ == "__main__":
    main()
