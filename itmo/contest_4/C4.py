import sys


def sift_down(i: int, n: int, p: list[int], swaps: list[tuple[int, int]]) -> None:
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and p[left] < p[min_index]:
        min_index = left
    if right < n and p[right] < p[min_index]:
        min_index = right
    if i != min_index:
        p[i], p[min_index] = p[min_index], p[i]
        swaps.append((min_index, i))
        sift_down(min_index, n, p, swaps)


def heapify(n: int, p: list[int]) -> list[tuple[int, int]]:
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n, p, swaps)

    return swaps


def main() -> None:
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    swaps = heapify(n, p)
    print(len(swaps))
    for i, j in swaps:
        print(i + 1, j + 1)


if __name__ == "__main__":
    main()
