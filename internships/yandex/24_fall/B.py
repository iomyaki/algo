import sys


def prefix(start: int, end: int, diff: list) -> int:
    prev_sum = {}
    res = 0
    curr_sum = 0

    for i in range(start, end):
        curr_sum += diff[i]

        if curr_sum == 0:
            res += 1

        res += prev_sum.get(curr_sum, 0)
        prev_sum[curr_sum] = prev_sum.get(curr_sum, 0) + 1

    return res


def num_of_subarrays(n: int, b: int, array: tuple) -> int:
    k = array.index(b)

    smaller = [0 for _ in range(n)]
    greater = [0 for _ in range(n)]
    for i in range(n):
        smaller[i] = array[i] < b
        greater[i] = array[i] > b

    diff = [0 for _ in range(n)]
    for i in range(n):
        diff[i] = smaller[i] - greater[i]

    val_1 = prefix(0, n, diff)
    val_2 = prefix(0, k, diff)
    val_3 = prefix(k + 1, n, diff)

    return val_1 - val_2 - val_3


def main() -> None:
    n, b = map(int, sys.stdin.readline().split())
    array = tuple(map(int, sys.stdin.readline().split()))
    print(num_of_subarrays(n, b, array))


if __name__ == "__main__":
    main()
