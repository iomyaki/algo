import sys
from collections import deque


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = tuple(map(int, sys.stdin.readline().split()))

    total = 0
    for i in range(n):
        right = {}
        for j in range(i, min(i + 21, n)):
            if arr[j] in right:
                right[arr[j]].append(j)
            else:
                right[arr[j]] = deque([j])

        min_right = min(i + 21, n)
        left = set()
        for mid in range(i, min(i + 21, n)):
            right[arr[mid]].popleft()
            for diam in range(-5, 6):
                if arr[mid] - diam in left and arr[mid] + diam in right and right[arr[mid] + diam]:
                    min_right = min(min_right, right[arr[mid] + diam][0])
            left.add(arr[mid])

        total += n - min_right

    print(total)


if __name__ == '__main__':
    main()
