import sys


def main() -> None:
    n = int(sys.stdin.readline())
    arr_a = tuple(map(int, sys.stdin.readline().split()))
    arr_b = tuple(map(int, sys.stdin.readline().split()))

    arr_sum = []
    for i in range(n):
        arr_sum.append((arr_a[i] + arr_b[i], i + 1))

    arr_sum.sort(key=lambda x: -x[0])
    if sum(arr_a) >= arr_sum[0][0]:
        print(-1)
        return

    for dwarf in arr_sum:
        print(dwarf[1], end=" ")


if __name__ == "__main__":
    main()

# Wrong algorithm — consider the following input:
# 3
# 3 4 4
# 100 2 1
